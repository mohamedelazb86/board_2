from django.urls import path
from . import views
from . import api



app_name= 'job'

urlpatterns = [

     # api

    path('jobs_api/all',api.JobApi.as_view()),
    path('job_api/<int:pk>',api.JobDetailApi.as_view()),


    path('',views.job_list,name='job-list'),
   
    path('<slug:slug>/',views.job_detail,name='job-detail'),

     path('add_job',views.add_job,name='add-job'),

    

    
   
]
