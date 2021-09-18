from admindash.views import addbook, adminHome, books, borrowedbooks, changepass, deletebook, editbook
from django.urls import path


urlpatterns = [
   path('home',adminHome,name='adminhome'),
   # path('student',studnetHome,name='studenthome'),
   # path("allstudents",viewstudents,name='allstudents'),
   # path('allstudents/<int:std_id>',studentprofile,name='studentprofile'),
   path('books',books,name="books"),
   path('books/<int:book_id>',editbook,name='editbook'),
   path('addbook',addbook,name='addbook'),
   path('changepassword',changepass,name='changepassword'),
   path('borrowedbooks',borrowedbooks,name='borrowedbooks'),
   path('delete/<int:book_id>',deletebook,name='deletebook')
]