from typing import ContextManager
from sign.forms import UserLoginForm, UsersModelForm
from sign.models import Users
from django.http.response import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User


# Create your views here.


def login(request):
    # user = User.objects.create_user('john1', 'lennon@thebeatles.com', 'johnpassword')
    # print(type(user))
    login_form = UserLoginForm()
    context={"form":login_form}
    return render(request,"sign/login.html",context)



def register(request):
    register_user=UsersModelForm()
    context={"form":register_user}
    return render(request,"sign/register.html",context)