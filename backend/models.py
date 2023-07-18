from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class UserProfile(models.Model):
    Male = "M"
    Female = "F"

    gender = [
        (Male,"M"),
        (Female,"F"),
    ]


    
    AB='Abia'
    AD='Adamawa'
    AI='Akwa Ibom'
    AN='Anambra'
    BU='Bauchi'
    BY='Bayelsa'
    BN='Benue'
    BO='Borno'
    CR='Cross River'
    DL='Delta'
    EB='Ebonyi'
    ED='Edo'
    EK='Ekiti'
    EN='Enugu'
    GO='Gombe'
    IM='Imo'
    JI='Jigawa'
    KD='Kaduna'
    KN='Kano'
    KT='Katsina'
    KB='Kebbi'
    KG='Kogi'
    KW='Kwara'
    LG='Lagos'
    NS='Nasarawa'
    NG='Niger'
    OG='Ogun'
    ON='Ondo'
    OS='Osun'
    OY='Oyo'
    PL='Plateau'
    RS='Rivers'
    SK='Sokoto'
    TR='Taraba'
    YB='Yobe'
    ZM='Zamfara'


    state=[
            (AB,'Abia'),
            (AD,'Adamawa'),
            (AI,'Akwa Ibom'),
            (AN,'Anambra'),
            (BU,'Bauchi'),
            (BY,'Bayelsa'),
            (BN,'Benue'),
            (BO,'Borno'),
            (CR,'Cross River'),
            (DL,'Delta'),
            (EB,'Ebonyi'),
            (ED,'Edo'),
            (EK,'Ekiti'),
            (EN,'Enugu'),
            (GO,'Gombe'),
            (IM,'Imo'),
            (JI,'Jigawa'),
            (KD,'Kaduna'),
            (KN,'Kano'),
            (KT,'Katsina'),
            (KB,'Kebbi'),
            (KG,'Kogi'),
            (KW,'Kwara'),
            (LG,'Lagos'),
            (NS,'Nasarawa'),
            (NG,'Niger'),
            (OG,'Ogun'),
            (ON,'Ondo'),
            (OS,'Osun'),
            (OY,'Oyo'),
            (PL,'Plateau'),
            (RS,'Rivers'),
            (SK,'Sokoto'),
            (TR,'Taraba'),
            (YB,'Yobe'),
            (ZM,'Zamfara')

    ]



    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=10, null=True, blank=True)
    
    state = models.CharField(max_length=11, choices=state, default=AB, null=True, blank=False)
    
    gender = models.CharField(max_length=1, 
                              choices=gender, default=Male)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')    


    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
