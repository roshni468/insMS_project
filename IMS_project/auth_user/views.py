from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import * # make sure this is your custom user model

# Register view
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # customuser model name 
            CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                user_type='admin'
        )
        return redirect('login_page')

    return render(request, 'register.html')


# Login view
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

# home_page
def home_page(request):
   
    return render(request, 'home_page.html')


# teacher_list
def teacher_list(request):
    teacher_data = TeacherModel.objects.all()
    context = {
        'teacher_data': teacher_data
    }

    return render(request, 'teacher_list.html', context)

# rgister_teacher
def register_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        teacher_name = request.POST.get('teacher_name')
        phone_number = request.POST.get('phone_number')
        profile_picture = request.FILES.get('profile_picture')

        teacher_data = CustomUser.objects.create_user(
            username=username,
            password=phone_number,
            email=email,
            user_type='teacher'
            )
        if  teacher_data:
            TeacherModel.objects.create(
                T_user=teacher_data,
                teacher_name=teacher_name,
                phone_number=phone_number,
                profile_picture=profile_picture,
            )
            return redirect('teacher_list')


       

    return render(request, 'register_teacher.html')


# student_list
def student_list(request):
    student_data = StudentModel.objects.all()
    context = {
        'student_data': student_data
    }

    return render(request, 'student_list.html', context)



# rgister_student
def student_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        student_name = request.POST.get('student_name')
        phone_number = request.POST.get('phone_number')
        profile_picture = request.FILES.get('profile_picture')

        student_data = CustomUser.objects.create_user(
            username=username,
            password=phone_number,
            email=email,
            user_type='student'
            )
        if  student_data:
            StudentModel.objects.create(
                S_user=student_data,
                student_name=student_name,
                phone_number=phone_number,
                profile_picture=profile_picture,
            )
            return redirect('student_list')


       

    return render(request, 'student_register.html')




