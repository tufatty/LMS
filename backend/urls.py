from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'backend'

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'custom_password_reset_email.html'
    success_url = '/password_reset_done'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'custom_password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'custom_password_reset_confirm.html'
    success_url = '/password_reset_complete'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'custom_password_reset_complete.html'

urlpatterns = [
    path('home/', views.home, name ='home'),
    path('', views.index, name ='index'),
    #path('students/', views.Students, name = 'students'),
    path('registration/', views.register_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_request, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('update/', views.update, name='update'),
    path('inbox/', views.inbox, name='inbox'),
    path('settings/', views.settings, name='settings'),
    

    #FOR PASSWORD RESETTING OR LET'S SAY FORGOT PASSWORD

    path('password_reset/', CustomPasswordResetView.as_view(),  name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

] 