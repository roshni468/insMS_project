from django.urls import path
from .views import*

urlpatterns = [
    path('register_page/', register_page, name='register_page'),
    path('', login_page, name='login_page'),
    path('home/', home_page, name='home_page'),
    # {% comment %} Teacher url {% endcomment %}
    path('teacher/', teacher_list, name='teacher_list'),
    path('register_teacher/', register_teacher, name='register_teacher'),
    # {% comment %} student url {% endcomment %}
    path('student_list/', student_list, name='student_list'),
    path('student_register/', student_register, name='student_register'),


   
]