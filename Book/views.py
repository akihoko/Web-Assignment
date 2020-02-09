from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Book.models import items, Hotels, Room


def book(request):
    obj=items.objects.all()
    return render(request,"Website/Items.html",{"Hotel":obj})
@login_required(login_url="/Home/login")
def show(request,pid):
    if request.method=="POST":
        hotel=items.objects.get(id=pid)
        user=request.user
        room_type=request.POST['type']
        numberofguests=request.POST['no']
        numberofrooms=request.POST['noR']
        price=request.POST['price']
        duration=request.POST['duration']
        bookeddate=datetime.now()
        bookedfor=request.POST['date']

        book=Room(hotel=hotel,user=user,Room_type=room_type,Numberofguests=numberofguests,Numberofrooms=numberofrooms,Price=price,Duration=duration,BookedDate=bookeddate,BookedFor=bookedfor)
        book.save()
        return redirect('/tickets')

    obj=Hotels.objects.get(hotel=pid)
    return render(request,"Website/Booking.html",{"Link":obj})

