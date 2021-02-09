from apps.activities.serializers import ActivityPeriodSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    def get_activity_periods(self, user_obj):
        return ActivityPeriodSerializer(user_obj.activity_periods.all(), many=True).data