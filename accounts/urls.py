from django.urls import path

from . import views
app_name='accounts'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('<str:username>/activate',views.actiavte,name='activate'),
    path('candidator',views.candidater,name='candidater'),
    path('contact',views.contact,name='contact'),
]
