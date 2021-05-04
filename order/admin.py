from django.contrib import admin

from .models import Orders, OrderProduct


admin.site.register(Orders)
admin.site.register(OrderProduct)
