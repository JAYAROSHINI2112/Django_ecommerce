from django.urls import path,include
from . import views
urlpatterns = [
    path('viewclasses',views.viewclasses,name='viewclasses'),
    path('addclasses',views.addclasses,name='addclasses'),
    path('editclasses/<int:id>',views.editclasses,name='editclasses'),
    path('deleteclasses/<int:id>',views.deleteclasses,name="deleteclasses"),
]