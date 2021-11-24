from .views import *
from django.urls import path, include

app_name = 'first'

urlpatterns = [
    path('',main, name='home'),
    path('ajax/ajax_filter', ajax_filter, name='ajax_filter'),
]

