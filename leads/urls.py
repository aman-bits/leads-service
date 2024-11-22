from rest_framework.routers import DefaultRouter
from .views import StageViewSet, LeadViewSet, LeadActivityViewSet

router = DefaultRouter()
router.register(r'stages', StageViewSet, basename='stage')
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'activities', LeadActivityViewSet, basename='activity')

urlpatterns = router.urls
