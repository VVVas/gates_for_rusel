from rest_framework import mixins, viewsets

from .models import Gate, UserOS, Visit
from .serializers import GateSerializer, UserOSSerializer, VisitSerializer


class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class UserOSViewSet(viewsets.ModelViewSet):
    queryset = UserOS.objects.all()
    serializer_class = UserOSSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class VisitViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
