from django.urls import path
from api.views import Employee

urlpatterns=[
    path('employee/', Employee.as_view(),name="emp")

]