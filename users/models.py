from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from multiselectfield import MultiSelectField


role = (
        ('1', 'Admin'),
        ('2', 'Freelancer'),
        ('3', 'Project Owner'),)

grades = (
        ('1', 'Grade One'),
        ('2', 'Grade Two'),
        ('3', 'Grade Three'),
        ('4', 'Grade Four'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number=models.CharField(default='DEFAULT VALUE', unique=True, max_length=14)
    email=models.EmailField(unique=True, default='DEFAULT EMAIL')
    location=models.CharField(default='DEFAULT VALUE', max_length=30)
    Age=models.PositiveIntegerField(default=0)
    skills=models.TextField(default='DEFAULT VALUE', max_length=100)
    experience=models.TextField(max_length=100, default='DEFAULT VALUE')
    resume=models.FileField(default='DEFAULT VALUE', upload_to='freelancer_docs')
    certificates=models.FileField(default='DEFAULT VALUE', upload_to='freelancer_certs')
    interested_grades=MultiSelectField(choices=grades,max_choices=2,max_length=3, default=1)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'

class Grade(models.Model):
    grade_name = models.CharField(max_length=20, choices=role, default='Freelancer')

    def __str__(self):
        return self.grade_name