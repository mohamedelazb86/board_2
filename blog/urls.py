
from django.urls import path
from . import views

# api
from . import api


app_name='blog'

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('<slug:slug>',views.post_detail,name='post-detail'),

    # api url
    path('postapi/api',api.PostApi.as_view()),
    path('postapi/<int:pk>',api.PostDetailApi.as_view()),
    path('postall/all/<int:pk>',api.PostAllApi.as_view()),
   
]
