from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "icon",
            "color",
        )


class ExpenseReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = (
            "id",
            "category",
            "datetime",
            "value",
            "description",
            "created_at",
            "updated_at",
        )


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "id",
            "category",
            "datetime",
            "value",
            "description",
            "created_at",
            "updated_at",
        )
