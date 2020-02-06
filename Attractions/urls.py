from django.urls import path

from Attractions import views

urlpatterns=[
    path('',views.show)
]