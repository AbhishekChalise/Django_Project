"""
URL configuration for crud_operation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from student.views import student,show
from student.views import edit_students
from student.views import delete
from teacher.views import Teachers
from teacher.views import Show_teacher,edit_teacher,delete_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name = 'student'),
    path('student/show/',show,name = 'show'),
    path('student/edit/<int:id>/', edit_students , name = 'edit_student'),
    path('student/delete/<int:id>/',delete,name = 'delete_student'),
    path('teacher/',Teachers,name = 'teacher_info'),
    path('teacher/show/', Show_teacher , name = 'showTeacher'),
    path('teacher/edit/<int:id>/',edit_teacher,name = 'edit_teacher'),
    path('teacher/delete/<int:id>/',delete_teacher,name = 'delete_teacher'),
]

