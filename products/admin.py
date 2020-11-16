from django.contrib import admin
from .models import ProductCategory, Product, Images, ProductComment


class CategoryAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'slug']
    fieldsets = (
        (None, {'fields': ('name', 'slug')}),

    )

    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(ProductCategory)


class ProductAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['title', 'slug', 'updated', 'created']
    search_fields = ('title', 'updated', 'created',)
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'updated', 'created')}),

    )


admin.site.register(Product)


admin.site.register(Images)


class CommentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['comment', 'product', 'author']


admin.site.register(ProductComment, CommentAdmin)
