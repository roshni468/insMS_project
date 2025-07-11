from django.contrib import admin
from auth_user.models import CustomUser, TeacherModel, StudentModel

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
