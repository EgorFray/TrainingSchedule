from rest_framework import serializers

from .models import Schedule


class ScheduleSerialier(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'date', 'exercise']