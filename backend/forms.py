from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
#create your forms

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ENTER YOUR USERNAME',}))
    email = forms.EmailField(max_length=20, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ENTER YOUR E-MAIL',}))
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'ENTER YOUR PASSWORD',}))
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'CONFRIM YOUR PASSWORD',}))
   

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")
        labels = {
            'username':'.',
            'email':'',
            'password1':'.',
            'password2':'.',
        }
    '''
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'     

       # def save(self, commit=True):
           # User = super(NewUserForm, self).save(commit=False)
            #User.email = self.cleaned_data ['email']

            #if commit:
               # User.save()
           # return User
    '''
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile    
        fields = ('phone', 'dob', 'address', )
