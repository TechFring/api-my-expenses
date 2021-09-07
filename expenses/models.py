from django.contrib.auth import get_user_model
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Expense(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    value = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.id)
