from django.db import models
from django.contrib.auth.models import User
from PIL import Image


role = (
        ('1', 'Admin'),
        ('2', 'Freelancer'),
        ('3', 'Project Owner'),)

grades = (
        ('1', 'Grade One'),
        ('2', 'Grade Two'),
        ('2', 'Grade Three'),
        ('2', 'Grade Four'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=25,choices=role, default='Freelancer')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class FreelancerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Freelancer'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Grade(models.Model):
    grade_name = models.CharField(max_length=20, choices=role, default='Freelancer')

    def __str__(self):
        return self.grade_name