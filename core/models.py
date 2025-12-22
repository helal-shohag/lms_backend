from django.db import models
from users.models import UserModel

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    category = models.ForeignKey(Category,related_name='courses', on_delete=models.CASCADE)
    instructor = models.ForeignKey(UserModel,related_name='courses', on_delete=models.CASCADE)
    image =models.ImageField(upload_to='course_images/')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course,related_name='Lessons',on_delete=models.CASCADE)
    is_active= models.BooleanField(default=True)
    durations = models.FloatField()
    title = models.CharField(max_length=200)
    description = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Material(models.Model):
    lesson = models.ForeignKey(Lesson,related_name='materials',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='lesson_materials/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    course = models.ForeignKey(Course,related_name='enrollments',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField()
    enrolled_at = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return f"{self.student_name} - {self.course.title}" 
