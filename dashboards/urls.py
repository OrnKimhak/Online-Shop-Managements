from django.urls import path
from .views import dashboard
from dashboards import views
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard-page")
]
