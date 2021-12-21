from django.urls import path
from . import views

urlpatterns = [
   # child profiles homepage
    path('', views.profiles, name="profiles"),
    #create child profile page
    path('createprofile/', views.createprofile, name='createprofile'),
    #report page
    path('report/', views.report, name='report'),

  ]