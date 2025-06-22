from django.urls import path
from . import views


app_name= 'job'

urlpatterns = [
    path('',views.job_list,name='job-list'),
   
    path('<slug:slug>/',views.job_detail,name='job-detail'),

     path('add_job',views.add_job,name='add-job'),
   
]
