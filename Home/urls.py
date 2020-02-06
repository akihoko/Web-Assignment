from django.urls import path

from Home import views

urlpatterns=[
    path('',views.show),
    path("register/", views.register),
    path("login/", views.login),
    path("logout/",views.logout)

]