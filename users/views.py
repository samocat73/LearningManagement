from rest_framework import filters, viewsets

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ["course", "lesson", "payment_method"]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["payment_dates"]
