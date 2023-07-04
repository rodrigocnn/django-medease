
from django.urls import path
from services.api import api

urlpatterns = [
    path('', api.urls),
]
