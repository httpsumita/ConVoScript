from django.forms import ModelForm
from .models import Room, User 
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User 


class myUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['name','username','email','password1','password']

class RoomForm(ModelForm):
    class Meta:
        model=Room #specifying the model we are creating the form for 
        fields='__all__'

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['avatar','name','username','email','bio']