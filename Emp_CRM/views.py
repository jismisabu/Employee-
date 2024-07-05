from django.shortcuts import render
from django.views.generic import View
from Emp_CRM.forms import Employeeform,Empmodel_form
from Emp_CRM.models import Empmodel


class Register(View):
    def get(self,request):
        
        form=Employeeform()

        return render(request,"index.html",{"form":form})
    
    def post(self,request):

        form=Employeeform(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("emp_name"))
            Empmodel.objects.create(**form.cleaned_data)
            #name=form.cleaned_data.get("emp_name")
           # place=form.cleaned_data.get("emp_place")
           #age=form.cleaned_data.get("emp_age")
           # Empmodel.objects.create(emp_name=name,emp_place=place,emp_age=age)
            return render(request,"index.html")
        else:
          return render(request,"index.html")
        
class Empmodelview(View):
    def get(self,request):
        form=Empmodel_form()
        return render(request,"index2.html",{'form':form})
    
    def post(self,request):
        form=Empmodel_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"index.html")
    
class Employees(View):
    def get(self,request):
        data=Empmodel.objects.all()
        print(data)
        return render(request,"index3.html",{"data":data})
    
# delete particular
class EmpDelete(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        Empmodel.objects.get(id=id).delete()
        print("deleted successfully")
        return render(request,"index.html")
    
class EmpUpdate(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)
        form=Empmodel_form(instance=data)
        return render(request,"index5.html",{'form':form})
    
    def post (self,request,**kwargs):
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)
        form=Empmodel_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            form=Empmodel_form()
        return render(request,"index5.html",{"form":form})
    print("update successfully")

#to fetch a unique data
class EmpDetail(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)





    
