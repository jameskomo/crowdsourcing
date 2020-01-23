
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Grade


availability = (
        ('1', 'Contract'),
        ('2', 'Hourly'),
        ('3', 'Fixed'),)


class ProfileUpdateForm(forms.ModelForm):
    success_url='/kinetic-projects/'
    class Meta:
        model = Profile
        fields = ['image','phone_number','email', 'location', 'Age','skills','experience','resume', 'certificates', 'interested_grades']

