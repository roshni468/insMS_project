from django.db import models
from auth_user.models import StudentModel ,TeacherModel


# Create your models here.
class CourseModel(models.Model):
    course_Title = models.CharField(max_length=100, null=True)
    course_duration = models.CharField(max_length=10, null=True)
    course_description = models.TextField(null=True, blank=True)
    course_start_date = models.DateTimeField(auto_now_add=True, null=True)
    course_fee = models.PositiveIntegerField(null=True)
    assign_course = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True, related_name='assigned_courses')
   

    def __str__(self):
        return self.course_Title
    


class AdmittedcourseModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, related_name='admitted_courses')
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, null=True, related_name='admitted_courses')
    admission_date = models.DateTimeField(auto_now_add=True, null=True)
    course_fee = models.PositiveIntegerField(null=True)
    payment= models.PositiveIntegerField(null=True)
    due= models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.student.student_name



class payment_historyModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, null=True, related_name='payment_history')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, related_name='payment_history')
    payment_date = models.DateTimeField(auto_now_add=True, null=True)
    amount_paid = models.PositiveIntegerField(null=True)
    due= models.PositiveIntegerField(null=True)

  

    def __str__(self):
        return f"{self.student.student_name} - {self.course.course_Title} - {self.amount_paid}"