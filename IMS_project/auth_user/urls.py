from django.urls import path
from .views import*

urlpatterns = [
    path('register_page/', register_page, name='register_page'),
    path('', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('home/', home_page, name='home_page'),
    # {% comment %} Teacher url {% endcomment %}
    path('teacher/', teacher_list, name='teacher_list'),
    path('register_teacher/', register_teacher, name='register_teacher'),
    # {% comment %} student url {% endcomment %}
    path('student_list/', student_list, name='student_list'),
    path('student_register/', student_register, name='student_register'),
    # {% comment %} pending student url {% endcomment %}
    path('pending_student_register/', pending_student_register, name='pending_student_register'),
    path('pending_student_list/', pending_student_list, name='pending_student_list'),
    path('accept_pending_student/<str:myid>/', accept_pending_student, name='accept_pending_student'),
    path('delete_pending_student/<str:myid>/', delete_pending_student, name='delete_pending_student'),
]