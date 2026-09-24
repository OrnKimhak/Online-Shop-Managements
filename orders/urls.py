from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet,OrderViewSet, CustomerViewSet


router = DefaultRouter()

# router for products ==========================================
router.register(r"orders", OrderViewSet, basename="orders")

# router for customer ==========================================
router.register(r'customer', CustomerViewSet, basename="customer")
# router for categories ========================================
router.register(r'orderItem', OrderItemViewSet, basename="orderItem")
urlpatterns = router.urls
# urlpatterns = [
#     path('edit/<int:pk>/', EditProduct ,name="edit-products")
# ]