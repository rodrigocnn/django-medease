
from django.urls import path
from roles.api import api

urlpatterns = [
    path('', api.urls),

]
