from django.db import models
import random
import string
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    """generate random number """
    return ''.join(random.choice(chars) for _ in range(size))


class User(models.Model):
    """ User model with all tz as choice """
    id = models.CharField(primary_key=True, default=id_generator, editable=False, max_length=100)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=32, choices=TIMEZONES)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "user"

    def __str__(self):
        return self.real_name


