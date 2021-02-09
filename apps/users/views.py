from apps.users.serializers import UserSerializer
from apps.users.models import User
from rest_framework import generics
from rest_framework.response import Response

class UsersActivitiesView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        response = {
            'ok': True,
            'members': serializer.data
        }
        return Response(response)