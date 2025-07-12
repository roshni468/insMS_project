from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = [
      ('student', 'student'),
      ('teacher', 'teacher'),
      ('admin', 'admin'),
   ]


 
    user_type = models.CharField(max_length=10, choices=USER_TYPE, )
    
    def __str__(self):
        return self.username
    


class TeacherModel(models.Model):
    T_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,related_name='teacher_info')
    teacher_name =models.CharField(max_length=100, null=True)
    phone_number =models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to='teacher_profile/pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.teacher_name


class StudentModel(models.Model):
    S_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,related_name='student_info')
    student_name =models.CharField(max_length=100, null=True)
    phone_number =models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to='student_profile/pictures/', null=True, blank=True)




class PandingModel(models.Model):
    username = models.CharField(max_length=150, null=True)
    email= models.EmailField(max_length=254, null=True)
    full_name =models.CharField(max_length=100, null=True)
    phone_number =models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to='student_profile/pictures/', null=True, blank=True)


    def __str__(self):
        return self.full_name

  