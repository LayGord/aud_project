from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('task', views.task, name='task'),
]