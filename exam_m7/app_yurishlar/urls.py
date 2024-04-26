from rest_framework import routers

from .views  import SalibViewSet

router = routers.DefaultRouter()
router.register(r'', SalibViewSet, basename= 'salib')

urlpatterns = router.urls