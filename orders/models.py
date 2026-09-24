from django.db import models
from products.models import Product

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField()
    customer_email = models.EmailField()
    customer_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


# fields of order==================
    # Order
    # ----------------
    # id
    # order_number
    # customer
    # order_status
    # sub_total
    # discount_price
    # total_price
    # created_at
    # updated_at
# fields of order==================
# customer model have relationship with Order model

class Order(models.Model):
    class status_choice(models.TextChoices):
        pending = 'pending'
        arrived = 'arrived'
        completed = 'completed'
    order_number = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name="customer")
    status = models.CharField(choices= status_choice, default= status_choice.pending)
    sub_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    discount_percent = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.order_number
    

# fields of order==================
    # OrderItem
    # ----------------
    # id
    # order
    # product
    # quantity
    # unit_price
    # subtotal
# fields of order==================
# orderItem have relationship with order and product (one to many)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product
    