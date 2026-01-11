from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

from .views import PaymentViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payment", PaymentViewSet)

urlpatterns = []
urlpatterns += router.urls
