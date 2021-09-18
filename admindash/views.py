
# Create your views here.
from typing import ContextManager
from django.shortcuts import redirect, render

# Create your views here.




def adminHome(request):
    return render(request,"admindash/admin.html")





# def viewstudents(request):
#     return render(request,"student/allstudents.html")


# def studentprofile(request,std_id):
#     context={"std":std_id}
#     return render(request,"student/studentprofile.html",context)


def books(request):
    return render(request,"admindash/books.html")


def editbook(request,book_id):
    context={"book_id":book_id}
    return render(request,'admindash/editbook.html',context)



def addbook(request):
    return render(request,'admindash/addbook.html')



def changepass(request):
    return render(request,'admindash/changepass.html')

def borrowedbooks(request):
    return render(request,'admindash/borrowedbooks.html')
    

def deletebook(request,book_id):
    return redirect("books")