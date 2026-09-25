from django.contrib import admin
from .models import Categories, Product
# Register your models here.
admin.site.register(Categories)
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'price', 'stock','categories', 'image')