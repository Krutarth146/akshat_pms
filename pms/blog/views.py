from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.db.models import Min,Max,Avg,Count,Sum
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


def getAllData(request):
    # Django ORM lookups
    # students = Student.objects.all().values()
    # students = Student.objects.filter(age__gte = 50).values()
    # students = Student.objects.filter(age__lte = 50).values()
    # students = Student.objects.filter(name__istartswith = 'A').values()
    # students = Student.objects.filter(name__endswith = 'h').values()
    # students = Student.objects.filter(name__contains = 'f').values()
    # students = Student.objects.filter(age__range = (30,60)).values()
    # students = Student.objects.filter(age__in = [32,89]).values()
    # students = Student.objects.all().order_by('-age').values()
    # students = Student.objects.filter(age__gt = 50).order_by('-age').values()
    # students = Student.objects.exclude(age__gt = 50).order_by('-age').values()
    # students = Student.objects.all().reverse().values()
    # students = Student.objects.filter(age__lt = 50, name__istartswith = 'A').values()
    # students = Student.objects.annotate(total=Min('age')).values()
    students = Student.objects.annotate(total=Min('age'))
    x = Student.objects.count()
    print(x)  # 4
    # print(students)
    return render(request, 'blog/getalldata.html',{'students' : students})


def createOrm(request):
    student = Student(name= "Dhiraj Sir", age = 25, isActive = False)
    student.save()
    print("Student Saved...")
    return render(request,'blog/createorm.html')


def deleteRecord(request):
    student = Student.objects.filter(name="Akshat")
    student.delete()
    print("Record Deleted")
    return render(request,'blog/deleteorm.html')

def updateRecord(request):
    student = Student.objects.get(id=2)
    student.name = "Akshat Bhai"
    student.age = 18
    student.save()
    print("Record Updtaed")
    return render(request,'blog/updateorm.html')

def Home(request):
    return render(request, 'index.html')

