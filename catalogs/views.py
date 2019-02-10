from django.views import generic
from .models import Category
from rest_framework import viewsets
from .serializers import CategorySerializer

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generic.ListView):
    model = Category
