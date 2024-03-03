from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'main'),
    path('enter/<int:id>', enter, name = 'enter')
]