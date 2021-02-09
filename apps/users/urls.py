
from apps.users.views import UsersActivitiesView
from django.urls import path


urlpatterns = [
    path('v1/users_activities', UsersActivitiesView.as_view()),
]
