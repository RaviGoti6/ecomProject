from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username", "class": "form-control ps-2 border-start-0 fs-7 inbg form-control-lg mb-0"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "class": "form-control ps-2 border-start-0 fs-7 inbg form-control-lg mb-0"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password", "class": "form-control ps-2 border-start-0 fs-7 inbg form-control-lg mb-0"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", "class": "form-control ps-2 border-start-0 fs-7 inbg form-control-lg mb-0"}))

    class Meta:
        model = User
        fields = ['username', 'email']