from rest_framework import serializers

from .models import Gate, UserOS


class GateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gate
        fields = ('id', 'title',)


class UserOSSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserOS
        fields = ('id', 'login', 'add_date', 'num_pass', 'is_working',)
        read_only_fields = ('add_date', 'num_pass', 'is_working',)
