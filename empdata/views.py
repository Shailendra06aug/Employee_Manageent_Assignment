from django.shortcuts import render,redirect
from .models import EmployeeInfo
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
  if request.method=="POST":
    company_name = request.POST.get('company_name', '')
    role = request.POST.get('role', '')
    date_of_join = request.POST.get('date_of_join', '')
    last_date =  request.POST.get('last_date', '')
    print(company_name,role,date_of_join,last_date)
    employeeInfo = EmployeeInfo(company_name=company_name, role=role, date_of_join=date_of_join, last_date=last_date)
    employeeInfo.save()
    thank= True
  return render(request,"shop/addmore.html")

# def index(request):
  
#   if request.method=="POST":
#     company_name = request.POST.get('company_name', '')
#     role = request.POST.get('role', '')
#     date_of_join = request.POST.get('date_of_join', '')
#     last_date =  request.POST.get('last_date', '')
#     print(company_name,role,date_of_join,last_date)
#     employeeInfo = EmployeeInfo(company_name=company_name, role=role, date_of_join=date_of_join, last_date=last_date)
#     employeeInfo.save()
#     thank= True
#   return render(request,"shop/addmore.html")

def showEmployee(request):
   
  mydata = EmployeeInfo.objects.all()
  for i in mydata:
    print(i.company_name)
    print(i.role)
    
    data={
      'mydata':mydata
    }
    
  return render(request,"shop/showemployee.html",data)


# def Logout(request):
#     logout(request)
#     return redirect('login')