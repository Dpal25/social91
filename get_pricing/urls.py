from django.urls import path
from get_pricing import views

urlpatterns = [
    path('', views.GetPricing.as_view()),
]