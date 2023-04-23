from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.attendanceclass,name='attendanceclass'),
    path('viewattendanceclass/<int:id>',views.viewattendanceclass,name='viewattendanceclass'),       
    path('addattendance/<int:id>',views.addattendance,name='addattendance'),
    path('attendanceentry/<int:cid>/<int:did>',views.attendanceentry,name='attendanceentry')
]
