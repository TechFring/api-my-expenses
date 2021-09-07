from rest_framework.routers import DefaultRouter

from .views import AuthTokenView, AuthUserView

router = DefaultRouter()
router.register("token", AuthTokenView)
router.register("user", AuthUserView)

urlpatterns = router.urls
