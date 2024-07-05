from django import forms
from  Emp_CRM.models import Empmodel

class Employeeform(forms.Form):
    emp_name=forms.CharField(max_length=100)
    emp_position=forms.CharField(max_length=100)
    emp_place=forms.CharField(max_length=100)
    emp_age=forms.CharField(max_length=10)

class Empmodel_form(forms.ModelForm):
    class Meta:
        model=Empmodel
        fields="__all__"

#class ABC(forms.ModelForm):
 #   class Meta:
 #       model=Empmodel
  #      fields="__all__"

