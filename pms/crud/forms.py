from django import forms



class Employee_Creation(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=20)
    email = forms.EmailField(label="E-mail", max_length=20)