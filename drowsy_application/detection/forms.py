from django.forms import ModelForm 
from . models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserFrom(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

        labels = {
            "first_name":"name"
        }



    