from django.urls import path

from Deals import views

urlpatterns=[
    path('',views.show)
]