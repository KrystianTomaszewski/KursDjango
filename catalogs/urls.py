from django.urls import path

from . import views

app_name = 'catalogs'

urlpatterns = [
    path('', views.index, name='list'),
]
