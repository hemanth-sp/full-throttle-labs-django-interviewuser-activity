from apps.users.models import User
from django.db import models

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
 
    class Meta:
        verbose_name = "activity_period"
        verbose_name_plural = "activity_periods"
        db_table = "activity_period"
    
    def __str__(self):
        return self.user.real_name


