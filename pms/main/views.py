from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'main/login.html')
    
def signup(request):
    return render(request, 'main/signup.html')

def equipment(request):
    return render(request, 'main/equipment.html')

def contact(request):
    return render(request, 'main/contact.html')


