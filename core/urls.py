from django.urls import path
from .views import categoryview


urlpatterns = [    
    
    path("categories/", categoryview, name="categories"),
]