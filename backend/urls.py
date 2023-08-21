from django.urls import path
from . import views

app_name = 'backend'
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

    path('password_reset/', views.CustomPasswordResetView.as_view(),  name='password_reset'),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

] 