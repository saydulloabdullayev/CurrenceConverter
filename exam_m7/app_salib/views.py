
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView, 
    RetrieveUpdateAPIView,
)

from django_filters import rest_framework as filters

from .models import Salib, Theme
from .serializers import SalibDetailSerializer, SalibSerializer


class SalibFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', field_name='nomi')
    yil = filters.CharFilter(lookup_expr='icontains', field_name='yil')

class SalibListAPIView(ListAPIView):
    queryset = Salib.objects.all()
    serializer_class = SalibSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SalibFilter


    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return Salib.objects.filter(nomi__icontains= self.request.query_params['keyword'])
        return Salib.objects.all()


class SalibDetailAPIView(RetrieveAPIView):
    queryset = Salib.objects.all()
    serializer_class = SalibDetailSerializer


class SalibCreateAPIView(CreateAPIView):
    queryset = Salib.objects.all()
    serializer_class = SalibDetailSerializer
    permission_classes = [IsAuthenticated]

class SalibDeleteAPIView(DestroyAPIView):
    queryset = Salib.objects.all()
    serializer_class = SalibDetailSerializer

class SalibUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Salib.objects.all()
    serializer_class = SalibDetailSerializer






