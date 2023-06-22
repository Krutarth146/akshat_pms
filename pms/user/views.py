from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.views.generic.edit import CreateView
from .forms import *
from django.contrib.auth import login

# Create your views here.
class TrainerSignupView(CreateView):
    model = User
    form_class = TrainerCreationView
    template_name = 'user/signup_form.html'


    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'Trainer'
        return super().get_context_data(**kwargs)
    

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('/admin')