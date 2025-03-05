from rest_framework import viewsets

from net.models import NetMember
from net.permissions import IsActiveUser
from net.serializers import NetMemberSerializer


class NetMemberViewSet(viewsets.ModelViewSet):
    """
    Набор представлений сети.
    """

    queryset = NetMember.objects.all().order_by("-created_at")
    serializer_class = NetMemberSerializer
    permission_classes = [IsActiveUser]  # Доступ есть только у активных пользователей

    def get_queryset(self):
        # забираем страну для фильтрации
        country = self.request.query_params.get("country", None)

        if country:
            return NetMember.objects.filter(contacts__country__icontains=country.lower())
        return super().get_queryset()
