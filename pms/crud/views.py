from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .forms import Employee_Creation 
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
            return HttpResponseRedirect("/cbv/list/")
    else:
        data = Employee_Creation()

    return render(request, 'crud/create_em.html', {'form' : data})