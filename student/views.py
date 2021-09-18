from django.shortcuts import redirect, render

# Create your views here.

def studenthome(request,std_id):
    return render(request, 'student/studenthome.html')

def studentprofile(request,std_id):
    return render(request,'student/studentprofile.html')

def viewstudents(request):
    return render(request , 'student/allstudents.html')
 
def viewbooks(request):
    return render(request,'student/stdbooks.html')


def stdborrowedbooks(request):
    return render(request,"student/stdborrowedbooks.html")

def editprofile(request):
    return render(request,'student/editprofile.html')