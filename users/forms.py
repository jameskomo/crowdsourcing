
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, FreelancerData, Grade

availability = (
        ('1', 'Contract'),
        ('2', 'Hourly'),
        ('3', 'Fixed'),)

grades = (
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('2', 'Grade 3'),
        ('3', 'Grade 4'),)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'role']

class FreelancerDataForm(forms.ModelForm):

    bio=forms.CharField(max_length=100)
    skills=forms.CharField(max_length=200)
    Availability = forms.ChoiceField(choices=availability)
    completed=forms.BooleanField()
    grades=forms.ModelMultipleChoiceField(queryset = Grade.objects.all())
    documents=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = FreelancerData
        fields = ['user']