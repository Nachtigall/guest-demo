from django.urls import path

from .views import RentalView

urlpatterns = [
    path("", RentalView.as_view(), name="stats"),
]
