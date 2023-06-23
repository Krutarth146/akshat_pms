from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.views.generic.edit import CreateView
from .forms import *
from django.contrib.auth import login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

# Create your views here.
class TrainerSignupView(CreateView):
    model = User
    form_class = TrainerCreationForm
    template_name = 'user/signup_form.html'


    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'Trainer'
        return super().get_context_data(**kwargs)
    

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('/admin')
    

class ClientSignupView(CreateView):
    model = User
    form_class = ClientCreationForm
    template_name = 'user/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Client'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):

        email = form.cleaned_data.get('email')
        print(email)

        res = sendMail(email)

        if res > 0:
            user = form.save()
            login(self.request, user)
        return redirect('/admin')
    

class LoginView(LoginView):
    template_name = 'user/login.html'

    def get(self,request, *args, **kwargs):
        print(self.request.user)
        return self.render_to_response(self.get_context_data())



def sendMail(mailid):
    subject = "Welcome to Akshat's GYM"
    message = "Thank you for Register"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject, message, email_from, recipient_list)
    print(res)
    return res
