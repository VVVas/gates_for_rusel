from rest_framework import viewsets

from .models import Gate

from .serializers import GateSerializer


class GateViewSet(viewsets.ModelViewSet):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
