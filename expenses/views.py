from datetime import datetime

from rest_framework import mixins
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseReadSerializer, ExpenseSerializer


class CategoryView(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseView(ModelViewSet):
    queryset = Expense.objects.all()

    def get_serializer_class(self):
        is_read = self.request.method == "GET"
        if is_read:
            return ExpenseReadSerializer
        return ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        try:
            date_string = self.request.GET["date"]
            date = datetime.strptime(date_string, "%Y-%m")
            return Expense.objects.filter(
                user=user,
                datetime__year=date.year,
                datetime__month=date.month,
            )
        except:
            return Expense.objects.filter(user=user)
