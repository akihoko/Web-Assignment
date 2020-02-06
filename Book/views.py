from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from Book.models import items, movies


def book(request):
    obj=items.objects.all()
    return render(request,"Website/Items.html",{"Hotel":obj})
@login_required(login_url="/Home/login")
def show(request,pid):
    obj=movies.objects.get(hotel=pid)
    return render(request,"Website/Booking.html",{"Link":obj})

