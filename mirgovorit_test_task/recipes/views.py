from django.db.models import F, Q
from django.http import HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from recipes.models import Product, Recipe, RecipeProduct


@require_http_methods(["GET"])
def add_product_to_recipe(request):
    """Добавляет новый продукт к рецепту"""
    template = 'recipes/product_addition.html'

    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe_id, product=product_id,
                                                                  defaults={'weight': weight})

    recipe_product = RecipeProduct.objects.select_related('recipe', 'product').get(
        recipe_id=recipe_id, product_id=product_id
    )
    if not created:
        recipe_product.weight = weight
        recipe_product.save()

    context = {
        'recipe_name': recipe_product.recipe.name,
        'product_name': recipe_product.product.name,
        'weight': recipe_product.weight,
        'created': created,
    }

    return render(request, template, context)


@require_http_methods(["GET"])
def cook_recipe(request):
    """Готовит блюдо и обновляет счетчик использования у продуктов"""
    template = 'recipes/cook_recipe.html'

    recipe_id = request.GET.get('recipe_id')

    recipe_name = Recipe.objects.get(id=recipe_id).name
    product_ids = Recipe.objects.get(id=recipe_id).products.values_list('id', flat=True)
    products_to_update = Product.objects.filter(id__in=product_ids)
    products_to_update.update(times_used=F('times_used') + 1)

    context = {
        'recipe_name': recipe_name,
    }
    return render(request, template, context)


@require_http_methods(["GET"])
def show_recipes_without_product(request):
    """Выводит в таблицу рецепты без продукта или,
    если кол-во меньше 10 грамм"""
    template = 'recipes/recipes_table.html'

    product_id = request.GET.get('product_id')

    if not product_id:
        message = "Необходимо указать product_id в качестве query-параметра!"
        err_template = 'recipes/error_message.html'
        error_message = loader.render_to_string(err_template, {'message': message})
        return HttpResponseBadRequest(error_message)

    product_name = Product.objects.get(id=product_id).name
    print(product_name)

    recipes = Recipe.objects.filter(
        ~Q(products__id=product_id) |
        Q(products__id=product_id, recipeproduct__weight__lt=10)
    ).distinct()

    context = {
        'recipes': recipes,
        'product_name': product_name,
    }
    return render(request, template, context)
