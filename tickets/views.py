from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from Book.models import Room


@login_required(login_url='/Home/login')
def show(request):
    if request.method=="POST":
        mid=request.POST['id']
        obj=Room.objects.get(id=mid)
        obj.Room_type=request.POST['type']
        obj.Numberofguests=request.POST['no']
        obj.Numberofrooms=request.POST['noR']
        obj.Price=request.POST['price']
        obj.Bookedfor=request.POST['date']
        obj.Duration=request.POST['duration']
        obj.save()
    obj1=Room.objects.filter(user=request.user)
    return render(request,"Website/mybooking.html",{"Room":obj1})

def delete(request,pid):
    obj=Room.objects.get(id=pid)
    obj.delete()
    val=Room.objects.filter(user=request.user)
    return render(request,"Website/mybooking.html",{"Room":val})
