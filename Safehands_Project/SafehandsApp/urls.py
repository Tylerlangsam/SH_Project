from django.urls import path
from . import views

urlpatterns = [
   # child profiles homepage
    path('', views.profiles, name='profiles'),
    #create child profile page
    path('createprofile/', views.createprofile, name='createprofile'),
    #report page
    path('report/', views.report, name='report'),
    #edit report page
    path('edit/<int:report_id>', views.edit, name='edit'),
    #edit child profile page
    path('editchild/<int:child_id>', views.editchild, name='editchild'),
    #edit babysitter page
    path('editsitter/<int:babysitter_id>', views.editsitter, name='editsitter')

  ] 