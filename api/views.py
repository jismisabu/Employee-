from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import Empmodel,Employeeserializer


class Employee(APIView):

    def get(self,request,*args,**kwargs):
        qs=Empmodel.objects.all()
        serializer=Employeeserializer(qs,many=True)
        return Response (serializer.data)
