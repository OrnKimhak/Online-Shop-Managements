from django.db import models

# Create your models here.

# Categories
    # id
    # name
    # description

# Product
    # id
    # ├── name
    # ├── description
    # ├── price
    # ├── stock
    # ├── image
    # ├── category
    # ├── created_at
    # └── updated_at

# Categories Model
class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

# Product model for database
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to="products/",
        blank=True,
        null=True
    )
    categories = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name="products"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    