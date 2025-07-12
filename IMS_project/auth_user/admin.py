from django.contrib import admin
from auth_user.models import*

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(PandingModel)
