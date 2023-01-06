from django.urls import path

from basim import views

urlpatterns=[
    path('',views.index,name='index')
]