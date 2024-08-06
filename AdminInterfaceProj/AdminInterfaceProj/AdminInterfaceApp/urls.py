from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a simple view for the root of your app
]
