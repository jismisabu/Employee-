from rest_framework import serializers
from Emp_CRM.models import Empmodel

class Employeeserializer(serializers.ModelSerializer):

    class Meta:

        model=Empmodel
        
        fields='__all__'