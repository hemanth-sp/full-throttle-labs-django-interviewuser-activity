from rest_framework import serializers
from .models import ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

    def get_start_time(self, obj):
        format = '%b %d %Y %H:%M %p'
        return obj.start_time.strftime(format)
    
    def get_end_time(self, obj):
        format = '%b %d %Y %H:%M %p'
        return obj.end_time.strftime(format)