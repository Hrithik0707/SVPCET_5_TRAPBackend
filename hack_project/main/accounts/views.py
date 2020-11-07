from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import User
import datetime
from django.shortcuts import render

def index(request):
    return render(request,'accounts/index.html')

def register(request):
    
    if request.method == 'POST':

        # Accepting all the fields from html page
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        phone_number = request.POST['phone_number']
        

        # Check - password n confirm password are same
        if password==cpassword:
            
            # Check - If the user with this phone no. already exists
            if User.objects.filter(phone_number=phone_number).exists():
                messages.info(request,'Phone number already available')
                return redirect('register')
            else:

                # Check - If the user with this email already exists
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                else:

                    # Creating user by creating object of 'User' Model
                    user = User.objects.create_user(phone_number=phone_number,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save();
                
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Passwords not matching...')
            return redirect('register')

    else:
        return render(request,'accounts/register.html') 

# Authenticating user and loging him/her in
def login(request):
    if request.method=='POST':

        # Accepting phone no. n password from html page
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user =auth.authenticate(phone_number=phone_number,password=password)

        # Check - If the user exists
        if user is not None:
            auth.login(request,user)
            return redirect('accounts/')
        else:
            messages.info(request,'invalid credentials')
            return HttpResponse("invalid credentials")

    else:
       return render(request,'accounts/login.html')  

# For logging the user out
def logout(request):
    auth.logout(request)
    return redirect('/')