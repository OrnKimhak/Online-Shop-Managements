from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoriesViewSet, EditProduct


router = DefaultRouter()

# router for products ==========================================
router.register(r"products", ProductViewSet, basename="products")

# router for categories ========================================
router.register(r'categories', CategoriesViewSet, basename="categories")
urlpatterns = router.urls
# urlpatterns = [
#     path('edit/<int:pk>/', EditProduct ,name="edit-products")
# ]