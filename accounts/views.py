from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

    
def register(request):
    if request.method == 'POST':
        F_name = request.POST['F_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password==conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=F_name, username=username, email=email, password=password)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html') 

def logout(request):
    auth.logout(request)
    return redirect('/')
