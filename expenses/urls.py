from rest_framework.routers import DefaultRouter

from .views import CategoryView, ExpenseView

router = DefaultRouter()
router.register("category", CategoryView)
router.register("expense", ExpenseView)

urlpatterns = router.urls
