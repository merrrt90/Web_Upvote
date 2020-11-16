from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost, BlogComment


class CategoryAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'slug']
    fieldsets = (
        (None, {'fields': ('name', 'slug')}),

    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('name')}),)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

#test
#test2
admin.site.register(BlogCategory, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'slug']
    search_fields = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'slug')}),

    )


admin.site.register(BlogTag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['title', 'publish_on', 'slug']


admin.site.register(BlogPost, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['comment', 'post_date', 'author']


admin.site.register(BlogComment, CommentAdmin)
