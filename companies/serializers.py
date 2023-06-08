from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'type_company',
        )


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'type_company',
            'email',
            'country',
            'city',
            'street',
            'house_number',
            'products',
            'provider',
            'dept',
            'time_of_creation',
        )
