from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from companies.models import Company
from companies.serializers import CompanySerializer, CompanyListSerializer, CompanyDetailSerializer
from users.permissions import ActiveUserPerms


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    default_serializer = CompanySerializer
    serializers = {
        'list': CompanyListSerializer,
        'retrieve': CompanyDetailSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [ActiveUserPerms]
