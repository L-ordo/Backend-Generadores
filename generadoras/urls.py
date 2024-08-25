from django.urls import path
from .views import GetOfGenerations

urlpatterns = [
    path('api/generadoras', GetOfGenerations.as_view())  
]
