from django.urls import path
from courseApp.views import *

urlpatterns = [
    path('create-course/', create_course, name='create_course'),
    path('courses/', courses_page, name='courses_page'),
    path('admitted-courses-list/', admitted_courses_list, name='admitted_courses_list'),
    path('admitted-courses/', admitted_courses, name='admitted_courses'),
]
