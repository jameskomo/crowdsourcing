from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account import *
from users.models import Profile




class ProfileUpdateForm(forms.ModelForm):
    # role = forms.ChoiceField(choices=role)

    class Meta:
        model = Profile
        fields = ['image', 'role']