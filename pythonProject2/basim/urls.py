from django.urls import path

from basim import views

urlpatterns=[
    path('',views.index1,name='index1'),
    path('hello',views.hello,name='hello'),
    path('hi',views.hi,name='hi')
]