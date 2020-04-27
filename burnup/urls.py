from django.urls import path, re_path
from django.conf.urls import url
from burnup import views


app_name="burnup"
urlpatterns = [
    #re_path('showburnup/(<int:real>)?', views.showburnup, name='showburnup'),
    path('showburnup/', views.showburnup, name='showburnup'),
    path('register/', views.register, name='register')
]