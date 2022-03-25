from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.map),
    path('predict/', views.predict),
    path('contact/', views.contact),
    path('feedback/', views.feedback),

    path('contact/doin/', views.doin),
    path('contact/dona/', views.dona),
    path('contact/ryu/', views.ryu),
    path('contact/song/', views.song),
    path('contact/mimi/', views.mimi),

    path('developer/', views.engineer_detail)
]