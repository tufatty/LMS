from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm, UserUpdateForm, ProfileForm #NewRegistration
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #login and logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {'title':'Home'})

def index(request):
    return render(request, 'index.html', {'title':'Home'})

def about(request):
    return render(request, 'about.html', {'title':'About'})

def contact(request):
    return render(request, 'contact.html', {'title':'Contact Us'}),

@login_required(login_url='login/')
def courses(request):
    return render(request, 'courses.html', {'title':'Courses'}),

#FOR SEARCH BAR

#creating a registration form
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, User)
            messages.success(request, ("Registration successful."))
            return redirect("backend:login")
        else:
            messages.error(request, ("Unsuccessful Registration. Invalid Information"))
    form = NewUserForm()
    template = loader.get_template("register.html")
    context = {
        'register_form': form,
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
                messages.error(request, ("Invalid username or "  + "password."))
                return redirect('backend:login')
        else:
            messages.error(request, ("Invalid username or password"))
            return redirect('backend:login')
    form = AuthenticationForm()
    template = loader.get_template("login.html")
    context = {
        "login_form": form,
    }
    return HttpResponse(template.render(context, request))
    
@login_required(login_url='login/')
def update(request):
    #user_id = request.User.id 
    #mydashboard = User.objects.filter(id=user_id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        #validate the form
        if user_form.is_valid() and profile_form.is_valid():      
            user_form.save()
            profile_form.save()
            messages.success(request, ('update successful'))
            return redirect('backend:dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)

    template = loader.get_template('update.html')
    context = {

        'user' : request.user,
        'user_form': user_form,
        'profile_form': profile_form,

    }
    return HttpResponse(template.render(context, request))



@login_required(login_url='login/')
def logout_request(request):
    logout(request)
    messages.info(request, ("You have successfully logged out."))
    return redirect('backend:home')

@login_required(login_url='login/')
def dashboard(request):
    return render(request, 'dashboard.html', {'title':'Dashboard'})