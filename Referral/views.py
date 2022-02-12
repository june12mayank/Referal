from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Person

def DashBoard(request):
    return render(request, 'Referral/Dashboard.html')
    #return HttpResponse("<h1>This is the main Dashboard for Referral Site.</h1>")

def Job(request,Job_Id):
    return HttpResponse("This Page Job id is: %s." %Job_Id)


