from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def show(request):



    return render(request,"Website/index.html")

def register(request):
    if request.method=='POST':
        fn=request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        un = request.POST['un']
        password = request.POST['pw']
        user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=un,password=password)
        user.save()
        return redirect("Home/login")
    return render(request,"Website/register.html")

def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("/Home")

            return redirect('/about')
    return render(request,"Website/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/Home")