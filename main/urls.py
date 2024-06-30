
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('1/',views.srimareddi),
]
