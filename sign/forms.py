from django import forms
from django.db import models
from django.forms import fields

from sign.models import Users

class UsersModelForm(forms.ModelForm):
    class Meta:
        model= Users

        fields=["name","email","password","role"]



class UserLoginForm(forms.ModelForm):
    class Meta:
        model= Users
        fields=  {
            "email":model.email,
            'password': forms.PasswordInput(),

        }
