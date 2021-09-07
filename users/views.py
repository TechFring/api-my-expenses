from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.settings import api_settings

from .models import CustomUser
from .serializers import CustomUserSerializer


class AuthTokenView(mixins.CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid()

        try:
            email = request.data["email"]
            username = request.data["username"]
        except:
            serializer.is_valid(raise_exception=True)

        user, created = CustomUser.objects.get_or_create(
            email=email, defaults={**serializer.data}
        )

        if not created and user.username != username:
            return Response(status=status.HTTP_404_NOT_FOUND)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        serializer = CustomUserSerializer(user)
        data = serializer.data
        data["token"] = token

        return Response(data, status=status.HTTP_200_OK)


class AuthUserView(mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
