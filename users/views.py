from rest_framework import viewsets

from users.models import User
from users.permissions import ActiveUserPerms
from users.serializers import UserSerializer, UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'list': UserListSerializer,
        'retrieve': UserSerializer,
    }
    permission_classes = [ActiveUserPerms]
