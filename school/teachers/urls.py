from django.urls import path,include
from . import views
urlpatterns = [
    path('viewteachers',views.viewteachers,name='viewteachers'),
    path('addteachers',views.addteachers,name='addteachers'),
    path('editteachers/<int:id>/<int:cid>',views.editteachers,name='editteachers'),
    path('deleteteachers/<int:id>',views.deleteteachers,name="deleteteachers"),
]