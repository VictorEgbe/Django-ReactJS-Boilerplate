from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import ProfileImage

User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    add_fieldsets = (
        ('Main Information', {
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')
        })
    )

    fieldsets = (
        ('Main Information', {
            'fields': ('password', 'email', 'username', 'first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')
        }),
        ('Others', {
            'fields': ('date_joined', 'last_login'),
        })
    )
    
    search_fields = ('username', 'email')
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff', 'is_active')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('date_joined', )


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['profile_picture', 'user', 'date_created']
    search_fields = ['profile_picture', 'user__username', 'user__email']
    list_filter = ['date_created']


admin.site.register(User, UserAdmin)
admin.site.register(ProfileImage, ProfileImageAdmin)
admin.site.unregister(Group)
