from apps.activities.serializers import ActivityPeriodSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')