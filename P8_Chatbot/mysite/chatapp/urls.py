from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),


]