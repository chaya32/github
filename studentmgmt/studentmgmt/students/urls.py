from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students_list, name='students_list'),
    path('courses/', views.courses_list, name='courses_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/<int:student_id>/update/', views.update_student, name='update_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('add_student/', views.add_students, name='add_student'),
    path('add_course/', views.add_courses, name='add_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/update/', views.update_course, name='update_course'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
]