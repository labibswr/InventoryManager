from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    program = models.CharField(max_length=50)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.student.username}'
