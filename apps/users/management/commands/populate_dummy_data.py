from apps.activities.models import ActivityPeriod
from apps.users.models import User, id_generator
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
import factory  
import factory.django
import faker
import pytz


class UserFactory(factory.django.DjangoModelFactory): 
    """ fake user factory """ 
    class Meta:
        model = User

    real_name = factory.Faker('first_name')


class ActivityFactory(factory.django.DjangoModelFactory):
    """ fake activity factory """ 
    class Meta:
        model = ActivityPeriod


class Command(BaseCommand):
    help = "populate the dummy user activity data"

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=5,
            type=int,
            help='The number of fake users to create')

    def handle(self, *args, **options):
        # delete user before create
        User.objects.all().delete()
        fake = faker.Faker()
        for user_index in range(options['users']):
            user = UserFactory.create(id=id_generator(), tz=fake.timezone())
            
            for activity_index in range(3):
                current_date = timezone.now()
                days = int(str(activity_index)+str(user_index))
                next_date = current_date + timedelta(days=days)
                is_not_time_sorted = True
                while is_not_time_sorted:
                    try:
                        # check start time and end time validation error
                        start_time, end_time = self.generate_st_et_time(fake, current_date, next_date)
                        ActivityFactory.create(user=user, start_time=start_time, end_time=end_time)
                        is_not_time_sorted = False
                    except:
                        is_not_time_sorted = True
        self.stdout.write(self.style.SUCCESS("created {} users with activities".format(options['users'])))

    def generate_st_et_time(self,fake, first_date, second_date):
        start_time = fake.date_time_ad(start_datetime=first_date, end_datetime=second_date, tzinfo=pytz.UTC)
        end_time = fake.date_time_ad(start_datetime=first_date, end_datetime=second_date, tzinfo=pytz.UTC)
        end_time = datetime.combine(start_time.date(), end_time.time(),  tzinfo=pytz.UTC)
        return start_time, end_time
