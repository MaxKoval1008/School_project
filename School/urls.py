from django.urls import path

from .views import *

app_name = 'School'

urlpatterns = [
    path('school/create', SchoolCreateView.as_view()),
    path('group/create', GroupCreateView.as_view()),
    path('student/create', StudentCreateView.as_view()),
    path('school/list/', SchoolListView.as_view()),
    path('group/list/', GroupListView.as_view()),
    path('student/performance/<int:pk>', StudentProgressView.as_view()),
]
