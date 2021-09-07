from django.contrib import admin

from .forms import CategoryForm
from .models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("name", "icon", "color", "created_at", "updated_at")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("category", "user", "datetime", "value")
    fields = ("category", "user", "datetime", "value", "description")
