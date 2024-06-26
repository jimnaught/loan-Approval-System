from django.urls import path
from . import views


app_name = 'predictions'

urlpatterns = [   
    path('', views.home, name='home'),
    path('apply', views.apply, name='apply'),
    path('applications', views.applications, name='applications'),
]