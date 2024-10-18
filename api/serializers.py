from rest_framework import serializers

from .models import Gate


class GateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gate
        fields = ('id', 'title',)
