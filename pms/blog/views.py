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


def learnforloop(request):
    context = {}

    context['name'] = "Akshat"
    context['address'] = [
                    {'state' : "Gujarat", 'city' : 'Gandhinagar'},
                    {'state' : "Rajasthan", 'city' : 'Ajmer'},
                    {'state' : "Kashmir", 'city' : 'kumbalgagh'},
                ]
    context['money'] = [10,90,89,5666,300]
    context['Institute'] = 'ROyal Techno'

    return render(request, 'blog/for.html', context)