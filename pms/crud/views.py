from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Employee
from django.views.generic import TemplateView

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



# def Rendering_data(request):
#     name =  "Akshat"
#     age = 19
#     context = {}
#     context['name'] = name
#     context['age'] = age
#     return render(request, 'crud/render1.html', context)


class Render_data(TemplateView):
    template_name = 'crud/render1.html'

    def get_context_data(self, **kwargs):
        age = 10
        name = ['Akshat', 'Priyank']
        dict = {'1' : 'one', '2' : 'second'}
        context_old = super().get_context_data(**kwargs)
        context = {'age' : age, 'name' : name, 'dict' : dict, 'context' : context_old}

        return context
    

def contactus(request):
    if request.method == 'POST':
        form = Employee_Creation(request.POST)
        if form.is_valid():
            
            return HttpResponse("Thank You")
        else:
            return render(request, 'crud/contactus.html',{'form' : form})
    return render(request, 'crud/contactus.html', {'form' : Employee_Creation})