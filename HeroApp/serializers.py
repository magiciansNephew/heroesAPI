from rest_framework import serializers
from HeroApp.models import Departments, Heroes


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = ('HeroId',
                  'HeroName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName',
                  'Rank'
                  )
