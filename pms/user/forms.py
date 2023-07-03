from django.contrib.auth.forms import UserCreationForm
from .models import User, Client, Trainer, Electronics
from django import forms


class TrainerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'diet_plan']

    def save(self):
        user = super().save(commit=False)
        user.is_trainer = True
        user.save()
        return user

class ClientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile']

    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        return user
    

class ElectronicsForm(forms.ModelForm):
        class Meta:
            model = Electronics
            fields = '__all__'
    