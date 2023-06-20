from django import forms
from .models import Employee


class Employee_Creation(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=20)
    email = forms.EmailField(label="E-mail", max_length=20, required=True)
    phone = forms.CharField(max_length=13)
    query = forms.CharField(widget=forms.Textarea)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'salary', 'age', 'address']