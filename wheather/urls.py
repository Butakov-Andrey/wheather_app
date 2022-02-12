from django.urls import path
from .views import WheatherView

urlpatterns = [
    path('', WheatherView.as_view(), name='wheather'),
]
