from django.shortcuts import render,redirect
from user.models import UserInfo
from django.contrib import auth

from user.forms import LoginForm,RegisterForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=auth.authenticate(username=form.username,password=form.password)
            if user:
                auth.login(request,user)
                return redirect('index')




    form = LoginForm()
    context={
        'form':form,
    }
    return render(request,'user/login.html',context)




def register(request):
    pass