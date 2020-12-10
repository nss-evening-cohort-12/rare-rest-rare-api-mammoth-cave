from rest_framework import viewsets
from rareapi.models import Category
from rareapi.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer