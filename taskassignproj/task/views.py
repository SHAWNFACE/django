from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from rest_framework import generics
from . import models
from . permissions import IsAdmin
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import  permission_classes
# Create your views here.


def home(request):
    name = "shawn"
    args = {"my_name":name}
    return render(request,"home.html",args)
def login(request):
    #if request.method == 'GET':
    logout(request) 
    return render(request,"login.html")


usernamelist = []

def myloginform(request):
    username=''
    password=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result_list = []

    user = authenticate(username=username, password=password)
    if user is not None:
        m = models.UserProfile.objects.all()
        usr = None
        for m1 in m:
            if str(m1.user.username) == str(user):
                usr = m1
                break
        if user.is_active:
            dj_login(request, user)
            if usr.user_type == "Admin":
                global usernamelist
                usernamelist = User.objects.exclude(username = username)
                return render(request, "adminpage.html",{"usernamelist" : usernamelist})
        
            elif usr.user_type == "Consumer":
                cons = models.TaskDetails.objects.all()
                for cu in cons:
                    us = cu.users.all()
                    for u in us:    
                        if str(u.username) == str(user):
                           result_list.append((str(cu.task_name)))
                return render(request, "customerpage.html", {"task_list" : result_list}) 
            else:
                return render(request, "login.html")
    # Return a 'disabled account' error message
    else:
        return render(request, "login.html")
    # Return an 'invalid login' error message.

@login_required(login_url='/login/')
@permission_classes((IsAdmin, ))
def admininsert(request):
    
    if request.method == 'POST':
        try:
            text = request.POST['Text1']
            userlist = request.POST.getlist('selmul')
            task = models.TaskDetails()
            task.task_name = text
            task.save()
            userobj = User.objects.all()
            for userl in userobj:
                if userl.username in userlist:
                    task.users.add(userl)    
            return render(request,"adminpage.html",{"inser_msg":"Task assigned successfully","usernamelist" : usernamelist})
        except Exception as e:
            print(str(e))
    else:
        return HttpResponseRedirect("/login/")

    
