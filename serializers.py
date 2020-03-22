from rest_framework import serializers
from API.models import employee


class employeeSerializer(serializers.ModelSerializer):
    Department = serializers.CharField(required=False)

    class Meta:
        model = employee
        fields='__all__'
