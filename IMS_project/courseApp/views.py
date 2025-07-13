from django.shortcuts import render ,redirect
from courseApp.models import CourseModel
from courseApp.models import*
# create_coursereate your views here.
def create_course(request):
    teacher_data =TeacherModel.objects.all()
    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_duration = request.POST.get('course_duration')
        course_description = request.POST.get('course_description')
        course_fee = request.POST.get('course_fee')
        assign_course = request.POST.get('assign_course')

        teacher_data = TeacherModel.objects.get(id=assign_course)

        CourseModel.objects.create(
            course_Title=course_title,
            course_duration=course_duration,
            course_description=course_description,
            course_fee=course_fee,
            assign_course=teacher_data
        )
        return redirect('courses_page')
    context={
        'teacher_data': teacher_data,
    }
   
    return render(request, 'courses/create_course.html', context)

# courses_page
def courses_page(request):
    courses = CourseModel.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)

# admitted_courses_list
def admitted_courses_list(request):
    admitted_courses = AdmittedcourseModel.objects.all()
    context = {
        'admitted_courses': admitted_courses
    }
    return render(request, 'courses/admit_course_list.html', context)


# admitted_courses 
def admitted_courses(request):
    student_list = StudentModel.objects.all()
    course_list = CourseModel.objects.all()
    if request.method == 'POST':
        Student = request.POST.get('Student')
        course = request.POST.get('course')
        payment = request.POST.get('payment')
       

        student_data = StudentModel.objects.get(id=Student)
        course_data = CourseModel.objects.get(id=course)

        admit_course_data= AdmittedcourseModel.objects.create(
            student=student_data,
            course=course_data,
            payment=payment,
            course_fee=course_data.course_fee,
            due=course_data.course_fee - payment,
        )
        payment_historyModel.objects.create(
            course=admit_course_data,
            amount_paid=payment,
            due=admit_course_data.due
        )
        return redirect('admitted_courses_list')
    context = {
        'student_list': student_list,
        'course_list': course_list
    }
    return render(request, 'courses/admit_course.html', context)


# AdmittedcourseModel
def AdmittedcourseModel(request):
    admitted_courses = AdmittedcourseModel.objects.all()
    context = {
        'admitted_courses': admitted_courses
    }
    return render(request, 'courses/admitted_course_model.html', context)


# make payment
def make_payment(request):
    courses = AdmittedcourseModel.objects.all()
    if request.method == 'POST':
        payment = request.POST.get('payment')
        for course in courses:
            course.payment = payment
            course.due = course.course_fee - int(payment)
            course.save()

        payment_historyModel.objects.create(
            course=course,
            amount_paid=payment,
            due=course.due
        )
        return redirect('admitted_courses_list')

    context = {
        'course': course
    }
    return render(request, 'payment/make_payment.html', context)
