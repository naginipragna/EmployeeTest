from django.shortcuts import render
from . models import Employee
from .forms import EmployeeForm

# Create your views here.
def employeelist(request):
    emp = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            render(request,'index.html',{'emps':emp})
    return render(request,'index.html',{'emps':emp})

def emloyeedata(request):
    emp = Employee.objects.all()
    return render(request,'out.html',{'out':emp})