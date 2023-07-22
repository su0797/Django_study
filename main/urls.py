from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    path('', views.contact, name='contact'),
    path('', views.test, name='test'),
]

