from typing import List

from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, ListAPIView, GenericAPIView, RetrieveAPIView
)
from .models import School, Group, Student
from .serializers import StudentSerializer, GroupSerializer, SchoolSerializer


class SchoolCreateView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupCreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolListView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentProgressView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
