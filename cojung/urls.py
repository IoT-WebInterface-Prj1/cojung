from django.urls import path
from . import views

app_name = 'cojung'

urlpatterns = [
    path('', views.index, name='index'),
]