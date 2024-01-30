from django.urls import path

from .views import (add_product_to_recipe, cook_recipe,
                    show_recipes_without_product)

urlpatterns = [
    path('add-product-to-recipe/', add_product_to_recipe,
         name='add_product_to_recipe'),
    path('cook-recipe/', cook_recipe,
         name='cook_recipe'),
    path('show-recipes-without-product/', show_recipes_without_product,
         name='show_recipes_without_product'),
]