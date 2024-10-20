import logging

from django.db import transaction
from rest_framework import serializers

from .models import Gate, UserOS, Visit

logging.basicConfig(
    level=logging.INFO,
    filename='log.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s'
)
logger = logging.getLogger(__name__)


class GateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gate
        fields = ('id', 'title', 'working_hours_up_to',)


class UserOSSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserOS
        fields = ('id', 'login', 'add_date', 'num_pass', 'is_working',)
        read_only_fields = ('add_date', 'num_pass', 'is_working',)


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=32, label='Пользователь ОС')
    gate = serializers.CharField(max_length=32, label='КПП')

    class Meta:
        model = Visit
        fields = ('id', 'user', 'is_enter', 'gate', 'num_pass', 'date',)
        read_only_fields = ('is_enter', 'date',)

    def validate_user(self, user):
        if not user.isdigit():
            logger.info(
                f'Попытка прохода несушествующим пользователем: {user}'
            )
            raise serializers.ValidationError('Передайте ID пользователя ОС')
        if not UserOS.objects.filter(id=user).exists():
            logger.info(
                f'Попытка прохода несушествующим пользователем: {user}'
            )
            raise serializers.ValidationError('Пользователь ОС не существует')
        return user

    def validate_gate(self, gate):
        if not gate.isdigit():
            logger.info(
                f'Попытка прохода на несушествующем КПП: {gate}'
            )
            raise serializers.ValidationError('Передайте ID КПП')
        if not Gate.objects.filter(id=gate).exists():
            logger.info(
                f'Попытка прохода на несушествующем КПП: {gate}'
            )
            raise serializers.ValidationError('КПП не существует')
        return gate

    def validate(self, data):
        useros = UserOS.objects.get(id=data.get('user'))
        if useros.num_pass != data.get('num_pass'):
            logger.info(
                'Попытка прохода c чужим пропуском: '
                f'Пользователь {data.get("user")} '
                f'Пропуск {data.get("num_pass")} '
                f'КПП {data.get("gate")} '
            )
            raise serializers.ValidationError(
                'Пропуск не принадлежит пользователю ОС'
            )
        return data

    @transaction.atomic
    def create(self, validated_data):
        useros_id = validated_data.pop('user')
        gate_id = validated_data.pop('gate')
        useros = UserOS.objects.get(id=useros_id)
        gate = Gate.objects.get(id=gate_id)
        if useros.is_working:
            validated_data['is_enter'] = False
            useros.is_working = False
        elif not useros.is_working:
            validated_data['is_enter'] = True
            useros.is_working = True
        useros.save()
        validated_data['user'] = useros
        validated_data['gate'] = gate
        return super().create(validated_data)
