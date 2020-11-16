from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'is_staff',
                    'last_login', 'username',)
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',
                           'first_name', 'last_name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            'avatar',
            'product_limit',

        )}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


"""from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password',
                           'first_name', 'last_name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            'avatar',
            'product_limit',

        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'is_staff', 'last_login', 'avatar')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(CustomUser, CustomUserAdmin)"""
