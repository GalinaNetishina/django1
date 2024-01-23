from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner, IsNotOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.filter(~Q(status="DRAFT"))
    serializer_class = AdvertisementSerializer

    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator']

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if IsAuthenticated():
            self.queryset = self.queryset | Advertisement.objects.filter(Q(status="DRAFT") & Q(creator=self.request.user.id))
        if self.action == "mark_favorite":
            return [IsAuthenticated(), IsNotOwner()]
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsOwner()]

        return [IsAuthenticatedOrReadOnly()]

    @action(methods=['post'], detail=True, url_path='toggle-mark')
    def mark_favorite(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        mark = user.favorites.filter(id=post.id).exists()
        if mark:
            user.favorites.remove(post)
        else:
            user.favorites.add(post)
        return Response({'status': "Removed" if mark else "Added"})

    @action(methods=['get'], detail=False, url_path='favorites')
    def get_favorite(self, request, *args, **kwargs):
        queryset = request.user.favorites.all()
        return Response({'Favorites': AdvertisementSerializer(queryset, many=True).data})