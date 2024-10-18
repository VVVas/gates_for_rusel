from rest_framework import viewsets

from .models import Gate, UserOS
from .serializers import GateSerializer, UserOSSerializer


class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class UserOSViewSet(viewsets.ModelViewSet):
    queryset = UserOS.objects.all()
    serializer_class = UserOSSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
