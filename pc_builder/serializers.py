from rest_framework import serializers
from .models import Monitor, Mouse, Keyboard


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'

