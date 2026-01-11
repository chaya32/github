from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course


def dashboard(request):
    """Display dashboard with student and course statistics."""
    return render(request, 'dashboard.html', {
        'students_count': Student.objects.count(),
        'courses': Course.objects.count()
    })


def students_list(request):
    """Display list of all students."""
    students = Student.objects.select_related('course').all()
    return render(request, 'students_list.html', {'students': students})


def courses_list(request):
    """Display list of all courses."""
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})


def student_detail(request, student_id):
    """Display details of a specific student."""
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})


def add_students(request):
    """Add a new student."""
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        age = request.POST.get('age')
        course_id = request.POST.get('course')
        
        if full_name and email and age and course_id:
            try:
                course_instance = Course.objects.get(id=course_id)
                Student.objects.create(
                    full_name=full_name,
                    email=email,
                    age=int(age),
                    course=course_instance
                )
                return redirect('students_list')
            except (Course.DoesNotExist, ValueError):
                pass
    
    courses = Course.objects.all()
    return render(request, 'add_student.html', {'courses': courses})


def add_courses(request):
    """Add a new course."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Course.objects.create(name=name)
            return redirect('courses_list')
    
    return render(request, 'add_course.html')


def course_detail(request, course_id):
    """Display details of a specific course."""
    course_instance = get_object_or_404(Course, id=course_id)
    students_in_course = Student.objects.filter(course=course_instance)
    return render(request, 'course_detail.html', {
        'course': course_instance,
        'students': students_in_course
    })


def delete_student(request, student_id):
    """Delete a student."""
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students_list')


def delete_course(request, course_id):
    """Delete a course."""
    course_instance = get_object_or_404(Course, id=course_id)
    course_instance.delete()
    return redirect('courses_list')


def update_student(request, student_id):
    """Update student information."""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.full_name = request.POST.get('full_name', student.full_name).strip()
        student.email = request.POST.get('email', student.email).strip()
        age = request.POST.get('age')
        course_id = request.POST.get('course')
        
        if age:
            student.age = int(age)
        
        if course_id:
            student.course = get_object_or_404(Course, id=course_id)
        
        student.save()
        return redirect('student_detail', student_id=student.id)
    
    courses = Course.objects.all()
    return render(request, 'update_student.html', {
        'student': student,
        'courses': courses
    })


def update_course(request, course_id):
    """Update course information."""
    course_instance = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            course_instance.name = name
            course_instance.save()
            return redirect('course_detail', course_id=course_id)
    
    return render(request, 'update_course.html', {'course': course_instance})
