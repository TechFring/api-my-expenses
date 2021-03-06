from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            "Custom fields",
            {"fields": ("salary",)},
        ),
    )
