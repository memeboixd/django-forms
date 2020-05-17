from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.main ,name='main'),
    path('form/',views.form_view,name='form')


]


