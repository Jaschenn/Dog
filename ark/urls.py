from django.urls import path
from . import views

urlpatterns = [
    path('EventsList', views.AllAvaliableEvents.as_view(), name='EventsList')
]
