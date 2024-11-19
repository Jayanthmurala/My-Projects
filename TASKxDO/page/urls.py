from django.urls import path
from .views import *
urlpatterns = [
    
    path('',home_page,name='home_page'),
    path('add_task/',add_task,name='add_task'),
    path('edit_task/<int:pk>/',edit_task,name='edit_task'),
    path('view_task/<int:pk>/',view_task,name='view_task'),
    path('delete_task/<int:pk>/',delete_task,name='delete_task'),
    
]