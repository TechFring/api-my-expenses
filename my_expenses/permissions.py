from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        is_user = type(obj) == get_user_model()
        if is_user:
            return obj == request.user
        return obj.user == request.user
