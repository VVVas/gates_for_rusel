from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GateViewSet, UserOSViewSet, VisitViewSet

app_name = 'api'

router = DefaultRouter()
router.register('gate', GateViewSet, basename='gate')
router.register('useros', UserOSViewSet, basename='useros')
router.register('visit', VisitViewSet, basename='visit')

urlpatterns = [
    path('v1/', include(router.urls)),
]
