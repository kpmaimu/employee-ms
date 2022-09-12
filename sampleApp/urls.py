from django.urls import path
from sampleApp import views

urlpatterns=[path('list/',views.EmployeeList.as_view()),
# path('upload/',views.ImageUpload.as_view()),
# path('upload/',views.ImageUpload.as_view()),



]