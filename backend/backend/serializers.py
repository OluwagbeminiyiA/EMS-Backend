from rest_framework import serializers
from .models import Employee
from .models import Projects


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'gender', 'marital_status', 'highest_education', 'skills', 'manager', 'date_joined']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project_id', 'project_name', 'client_name',]
