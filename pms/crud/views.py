from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Employee

# Create your views here.


def employee_creation_view(request):
    # if request.method == "GET":
    #     first_name = request.GET['fname']
    #     # last_name = request.GET['lname']
    #     last_name = request.GET.get('lname')

    #     print(first_name, last_name)

    if request.method == "POST":
        data = Employee_Creation(request.POST)

        if data.is_valid():
            return HttpResponseRedirect("/crud/list/")
    else:
        data = Employee_Creation()

    return render(request, 'crud/create_em.html', {'form' : data})


def em_create(request):
    context = {}

    form = EmployeeForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/crud/list/')
    
    context['form'] = form

    return render(request, 'crud/create.html', context)


def em_list(request):
    context = {}
    employee = Employee.objects.all().values()
    context['employee'] = employee

    return render(request, 'crud/list.html', context)


def em_update(request,id):
    context = {}
    employee = Employee.objects.get(id=id)
    # print(employee)
    form = EmployeeForm(request.POST or None,instance=employee)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/crud/list/")
    
    
    context['form'] = form


    return render(request,'crud/update.html',context)


def em_detail(request,id):
    context = {}
    employee = Employee.objects.get(id = id)

    context['employee'] = employee


    return render(request,'crud/detail.html',context)


def em_delete(request,id):
    context = {}
    employee = Employee.objects.get(id = id)

    if request.method == "POST":
        employee.delete()
        return HttpResponseRedirect("/crud/list/")

    # context['employee'] = employee


    return render(request,'crud/delete.html',context)