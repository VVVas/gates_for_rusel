from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GateViewSet

app_name = 'api'

router = DefaultRouter()
router.register('gate', GateViewSet, basename='gate')

urlpatterns = [
    path('v1/', include(router.urls)),
]
