from rest_framework import serializers
from .models import Order, OrderItem, Customer, Product

# OrderItemSerializer ==================================== 
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

# OrderSerializer ==================================== 
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True
    )
    class Meta:
        model = Order 
        fields = [
            'id',
            'order_number',
            'customer',
            'status',
            'sub_total',
            'discount_price',
            'discount_percent',
            'created_at',
            'updated_at',
            'items',
        ]
        # read only fields can read can't write =============
        read_only_fields = [
            "sub_total",
            "total_price",
            "created_at",
        ]

    # function create for orderItem ==========================
    def create(self, validated_data):
        items_data = validated_data.pop("items")

        products = Product.objects.all()
        order = Order.objects.create(
            **validated_data
        )

        sub_total = 0

        for item_data in items_data:
            product = item_data["product"]
            quantity = item_data["quantity"]

            unit_price = products.price

            sub_total = unit_price * quantity

            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity,
                unit_price = unit_price,
                sub_total = sub_total
            )
            # sum total of item together in OrderList
            sub_total += sub_total
        discount_percent = order.discount_percent
        order.sub_total = sub_total,
        discount_price = sub_total * (discount_percent / 100)
        
        # this is for find total price of item ===========
        # if customer order item up to ( 5$-10$ discount 5%) and (> 10$ <= 20$ discount 10%) and up to > 20$ discount 20%
        order.total_price = (
            sub_total - discount_price
        )
        order.save()
            
        return order

# OrderSerializer =====================================
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'