from django.urls import path
from . import views


app_name= 'job'

urlpatterns = [
    path('',views.job_list,name='job-list'),
]
