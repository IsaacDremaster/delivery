from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Orders, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer


class OrderView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
