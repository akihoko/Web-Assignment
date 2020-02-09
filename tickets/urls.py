from django.urls import path

from tickets import views

urlpatterns=[
    path("",views.show),
    path("delete/<pid>",views.delete)
]