from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView, Response

from .models import Products, ProductMark
from .serializers import ProductSerializer, ProductMarkSerializer
from .permissions import IsProductOrReadOnly, IsCommentOwnerOrReadOnly
from .service import ProductFilter


class ProductView(ModelViewSet):
    queryset = Products.objects.prefetch_related('created_at', 'product_marks', 'user_marks')
    serializer_class = ProductSerializer
    permission_classes = (IsProductOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = ProductFilter


class ProductMarkView(ModelViewSet):
    queryset = ProductMark.objects.all()
    serializer_class = ProductMarkSerializer
    permission_classes = (IsCommentOwnerOrReadOnly, )
    lookup_field = 'pk'