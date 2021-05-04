from rest_framework import serializers

from .models import Orders, OrderProduct

from product.models import Products


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Products
        fields = ('id', 'name', 'price', )


class OrderProductSerializer(serializers.Serializer):

    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'product_quantity', )


class OrderSerializer(serializers.Serializer):

    class Meta:
        model = Orders
        fields = ('id', 'date', 'address', 'total', 'status', 'product_order_product')

    def create(self, validated_data):
        print(validated_data)
        product = validated_data.pop('product_order_product')
        print(validated_data)
        order = Orders.objects.create(**validated_data)
        for product in product:
            product_order = OrderProduct.objects.create(**product)
            product_order.order = order
            product_order.save()
        order.set_total_price()
        return order