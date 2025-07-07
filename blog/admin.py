from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, BlogPost, Category

# Display the User model in the admin interface
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)
admin.site.register(BlogPost)
admin.site.register(Category)
