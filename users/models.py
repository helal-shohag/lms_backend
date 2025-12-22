from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ROLE = (
    ('student', 'Student'),
    ('instructor', 'Instructor'),   
    ('admin', 'Admin'),
)

class UserModel(AbstractUser):
     role = models.CharField(choices=ROLE,default='student')
     mobile_no = models.CharField(max_length=15)


     def __str__(self):
          return f"{self.username} - {self.role}"