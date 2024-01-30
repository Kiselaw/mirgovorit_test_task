from django.contrib import admin

from recipes.models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)
    list_editable = ('name',)
    list_filter = ('name',)
    inlines = (RecipeProductInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'times_used',)
    list_editable = ('name', 'times_used',)
    list_filter = ('name', 'times_used',)


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    search_fields = ('recipe', 'product', 'weight')
    list_display = ('id', 'recipe', 'product', 'weight',)
    list_editable = ('weight',)
    list_filter = ('weight',)
