from django.urls import path

from .import views
urlpatterns = [
    path('signup',views.signmeup, name ='signuphi'),
    path('login',views.logmein, name='login'),
    path('logout',views.logmeout, name='logout'),
]
