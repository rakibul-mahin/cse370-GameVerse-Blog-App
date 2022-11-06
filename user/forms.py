from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, CompRank

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username','password1','password2']

class CustomAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username','password1','password2']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['user','username']

class CreateRankForm(ModelForm):
    class Meta:
        model = CompRank
        # fields = '__all__'
        exclude = ['id', 'owner']