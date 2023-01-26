from django.shortcuts import render,redirect
from requests import request
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('user name already existed')
            elif User.objects.filter(email=email).exists():
                print('email already existed')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
            
        else:
            print('password not matched')
        return redirect('/travello')
    else:
        return render(request, 'account/register.html')