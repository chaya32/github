"""
URL configuration for studentmgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('students/',include('students.urls')),
    path('courses/', include('students.urls')),
    path('student/<int:student_id>/', include('students.urls')),
    path('add_student/', include('students.urls')),
    path('add_course/', include('students.urls')),
    path('course/<int:course_id>/', include('students.urls')),
    path('delete_student/<int:student_id>/', include('students.urls')),
    path('delete_course/<int:course_id>/', include('students.urls')), 
    path('student_deleted/', include('students.urls')),
    path('course_deleted/', include('students.urls')),
    path('student_detail/', include('students.urls')),
    path('course_detail/', include('students.urls')),
    path('students_list/', include('students.urls')),
    path('courses_list/', include('students.urls')),
    path('dashboard/', include('students.urls')),
]