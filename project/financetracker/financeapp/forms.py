from django import forms
from .models import user

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = user
        fields =['name','email','password','phonenumber']
        widgets={
            'email':forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'name':forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'phonenumber':forms.TextInput(attrs={'placeholder': 'phonenumber'}),
        }