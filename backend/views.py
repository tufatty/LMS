from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm, UserUpdateForm, ProfileForm, ContactForm #NewRegistration
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #login and logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordResetForm, SetPasswordForm
import datetime
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


today_date = datetime.date.today()
current_year = today_date.strftime('%Y')


# Create your views here.

def home(request):
    return render(request, 'home.html', {'title':'Home','current_year':current_year})

def index(request):
    return render(request, 'index.html', {'title':'Home','current_year':current_year})

def about(request):
    return render(request, 'about.html', {'title':'About','current_year':current_year})

def inbox(request):
    return render(request, 'about.html', {'title':'About','current_year':current_year})

def settings(request):
    return render(request, 'settings.html', {'title':'settings','current_year':current_year})

def contact(request):
    if request.method == 'POST':
      
        form = ContactForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            phone_num = form.cleaned_data.get('phone_num')
            email =form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')   
            form.save()
            messages.success(request, 'THANKS FOR THE INFO, WE WILL GET BACK TO YOU')
            send_mail(
                subject= full_name,
                message= text,
                from_email= email,
                recipient_list=['ugonjokubarthlomew@gmail.com','mccathly@gmail.com'],
                fail_silently=False,
            )
            return redirect("backend:contact")
        else:
            messages.error(request, "PLEASE FILL UP YOUR INFO")
    form = ContactForm()
    template = loader.get_template("contact.html")
    context = {
        'contact_form':form,
        'current_year': current_year,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login/')
def courses(request):
    return render(request, 'courses.html', {'title':'Courses','current_year':current_year})

#FOR SEARCH BAR

#creating a registration form
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = form.save()
            #login(request, User)
            messages.success(request, "Registration successful.")
            
            return redirect("backend:login")
        else:
            messages.error(request, "Unsuccessful Registration. Invalid Information")
    form = NewUserForm()
    template = loader.get_template("register.html")
    context = {
        'register_form': form,
        'current_year':current_year,
    }
    return HttpResponse(template.render(context, request))

#LOGIN

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                #what you have here is app name : patter/link name
                return redirect('backend:dashboard')
            else:
                messages.error(request, "Invalid username or "  + "password.")
                return redirect('backend:login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('backend:login')
    form = AuthenticationForm()
    template = loader.get_template("login.html")
    context = {
        "login_form": form,
        'current_year':current_year,
    }
    return HttpResponse(template.render(context, request))
    
@login_required(login_url='login/')
def update(request):
    #user_id = request.User.id 
    #mydashboard = User.objects.filter(id=user_id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        #validate the form
        if user_form.is_valid() and profile_form.is_valid():      
            user_form.save()
            profile_form.save()
            messages.success(request, 'update successful')
            return redirect('backend:dashboard')
        else:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            messages.error(request, "please check your form")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)

    template = loader.get_template('update.html')
    context = {

        'user' : request.user,
        'user_form': user_form,
        'profile_form': profile_form,
        'current_year':current_year,

    }
    return HttpResponse(template.render(context, request))



@login_required(login_url='login/')
def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('backend:login')

@login_required(login_url='login/')
def dashboard(request):
    return render(request, 'dashboard.html', {'title':'Dashboard','current_year':current_year})




#FOR PASSWORD RESETTING OR FORGOT PASSWORD


class CustomPasswordResetView(PasswordResetView):
    success_url = '/password_reset_done'
    email_template_name = 'password/custom_password_reset_email.html'
    template_name = 'password/custom_password_reset_form.html'
    subject_template_name = 'password/custom_password_reset_subject.txt'
    from_email = 'ugonjokubarthlomew@gmail.com'
    form_class = PasswordResetForm
    token_generator = PasswordResetTokenGenerator
    extra_context = {
        'title':'title',
        'form':form_class,
    }
    extra_email_context ={
   
    }
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_valid(form)
        return response
        
        
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password/custom_password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password/custom_password_reset_confirm.html'
    success_url = reverse_lazy('/password_reset_complete')
    token_generator = PasswordResetTokenGenerator
    post_reset_login = False
    post_reset_login_backend = ''
    form_class = SetPasswordForm
    extra_context = {
        'form':form_class,
        'title':'password reset'

    }
    reset_url_token = 'set-password'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    def form_invalid(self, form):

        return super().form_invalid(form)

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password/custom_password_reset_complete.html'
