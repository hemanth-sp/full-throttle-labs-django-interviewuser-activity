from apps.users.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity_periods', blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    
    class Meta:
        verbose_name = "activity_period"
        verbose_name_plural = "activity_periods"
        db_table = "activity_period"

    def full_clean(self):
        # start time hould be less than end time.
        if self.start_time > self.end_time:
            raise ValidationError({'start_time': _('start time should be less than end time')})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ActivityPeriod, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.real_name


