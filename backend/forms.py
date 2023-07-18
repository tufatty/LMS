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
        fields = ('phone', 'dob', 'address', 'city','state','gender','image')
        





    '''
    Abia='AB'
    Adamawa='AD'
    Akwa_Ibom='AI'
    Anambra='AN'
    Bauchi='BU'
    Bayelsa='BY'
    Benue='BE'
    Borno='BO'
    Cross_River='CR'
    Delta='DL'
    Ebonyi='EB'
    Edo='ED'
    Ekiti='EK'
    Enugu='EN'
    Gombe='GO'
    Imo='IM'
    Jigawa='JI'
    Kaduna='KD'
    Kano='KN'
    Katsina='KT'
    Kebbi='KB'
    Kogi='KG'
    Kwara='KW'
    Lagos='LG'
    Nasarawa='NS'
    Niger='NG'
    Ogun='OG'
    Ondo='ON'
    Osun='OS'
    Oyo='OY'
    Plateau='PL'
    Rivers='RS'
    Sokoto='SK'
    Taraba='TR'
    Yobe='YB'
    Zamfara='ZM'


    state=[
        (Abia,'AB'),
        (Adamawa,'AD'),
        (Akwa_Ibom,'AI'),
        (Anambra,'AN'),
        (Bauchi,'BU'),
        (Bayelsa,'BY'),
        (Benue,'BE'),
        (Borno,'BO'),
        (Cross_River,'CR'),
        (Delta,'DL'),
        (Ebonyi,'EB'),
        (Edo,'ED'),
        (Ekiti,'EK'),
        (Enugu,'EN'),
        (Gombe,'GO'),
        (Imo,'IM'),
        (Jigawa,'JI'),
        (Kaduna,'KD'),
        (Kano,'KN'),
        (Katsina,'KT'),
        (Kebbi,'KB'),
        (Kogi,'KG'),
        (Kwara,'KW'),
        (Lagos,'LG'),
        (Nasarawa,'NS'),
        (Niger,'NG'),
        (Ogun,'OG'),
        (Ondo,'ON'),
        (Osun,'OS'),
        (Oyo,'OY'),
        (Plateau,'PL'),
        (Rivers,'RS'),
        (Sokoto,'SK'),
        (Taraba,'TR'),
        (Yobe,'YB'),
        (Zamfara,'ZM'),

    ]

    Male = "M"
    Female = "F"

    gender = [

        (Male,"M"),
        (Female,"F"),
    ]


    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ENTER YOUR PHONE NUMBER','size':'4px'}))
    dob=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'ENTER YOUR DATE OF BIRTH'}))
    address=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ENTER YOUR ADDRESS'}))
    city=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ENTER YOUR CITY'}))
    state=forms.Select(attrs={'class':'special'},choices=state)
    gender=forms.Select(attrs={'class':'special'},choices=gender)
   
    '''

