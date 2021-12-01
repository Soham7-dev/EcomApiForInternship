from django.urls import path
from .views import *

urlpatterns = [
    path('', ReadCategories, name="ReadCategories"),
    path('items', ReadItems, name="ReadItems"),
]
