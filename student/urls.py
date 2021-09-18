from admindash.views import books
from student.views import editprofile, stdborrowedbooks, studenthome, studentprofile, viewbooks, viewstudents 

from django.urls import path




urlpatterns = [
    path('home/<int:std_id>',studenthome,name='studenthome'),
   
    path("allstudents",viewstudents,name='allstudents'),
    path('allstudents/<int:std_id>',studentprofile,name='studentprofile'),
    path('books',viewbooks,name="stdbooks"),
    path('borrowedbooks',stdborrowedbooks,name='stdborrowedbooks'),
    path('editprofile',editprofile,name='editprofile')
   
]