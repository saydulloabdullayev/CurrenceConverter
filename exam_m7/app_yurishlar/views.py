from rest_framework import viewsets

from app_salib.models import Salib
from app_salib.serializers import  SalibDetailSerializer

class SalibViewSet(viewsets.ModelViewSet):
    queryset = Salib.objects.all()
    serializer_class = SalibDetailSerializer

