from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ["course", "lesson", "payment_method"]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["payment_dates"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
