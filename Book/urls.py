from django.contrib.auth.decorators import login_required
from django.urls import path

from Book import views



urlpatterns=[
    path("<pid>", views.show),
    path("",views.book),



]