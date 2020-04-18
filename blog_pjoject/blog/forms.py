from django import forms
from .models import ContactUs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(forms.Form):
    name = forms.CharField()
    pswd = forms.CharField(widget=forms.PasswordInput)

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"