from django.shortcuts import render,redirect
from django.contrib import messages,auth
from contacts.models import Contact
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from .models import *

# def login(request):
#     form = LoginForm(request.POST or None)

#     msg = None

#     if request.method == "POST":

#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("/")
#             else:    
#                 msg = 'Invalid credentials'    
#         else:
#             msg = 'Error validating the form'    

#     return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('home')
        else:
            messages.error(request,'invalid credantials')
            return redirect('login')
        #return redirect('login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'logout successfully')
        return redirect('home')
def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
    'contacts': user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
def register(request):
    # import pdb
    # pdb.set_trace()
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        contact_number=request.POST['contact_number']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            #check Username
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already being used')
                    return redirect('register')
                else:
                    #looks like good
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=username,password=password,email=email)
                    #login after registration
                    #auth.login(request,user)
                    #messages.success(request,'you are logged in')
                    #return redirect('home')
                    user.save()
                    user_details=UserPersonalDetails.objects.create(phone_no=contact_number,user_id=user.id)

                    user_details.save()
                    messages.success(request,'you are successfully registered ')
                    return redirect('login')
        else:
            messages.error(request,'password did not match')
            return render(request,'accounts/register.html')
    else:
        return render(request,'accounts/register.html')


# class PasswordsChangeView(PasswordChangeView):
#     form_class=PasswordChangeForm
#     success_url=reverse_lazy('home')