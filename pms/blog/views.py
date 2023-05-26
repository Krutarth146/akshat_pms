from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def simple(request):
    return HttpResponse("Hello Akshat Bhaii!!")


def aboutus(request):
    return render(request,'blog/aboutus.html')


def data(request):
    context = {}
    name = "Akshat"
    college = "PDPU"
    coding = "Royal"

    context['Name'] = name
    context['College'] = college
    context['Coding'] = coding
    context['Guru'] = "Dhiraj Sir"

    return render(request,'blog/data_print.html', context)


def contactus(request):
    return render(request, 'blog/contactus.html', {
        'Std' : 9,
        'Address' : {"State" : "Gujarat", 'Country' : "India"}
    })