from rest_framework import serializers
from .models import School, Group, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_number', 'address', 'school_characteristic')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_number', 'course', 'motto', 'school')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'eng', 'math', 'bio', 'phis', 'chem', 'group')

