from django.urls import path
from rest_framework import routers
from . import views

app_name = 'catalogs'

router = routers.SimpleRouter()
router.register(r'category',views.CategoryViewsets)


urlpatterns = [
    path('', views.CategoryList.as_view(), name='list'),
]
