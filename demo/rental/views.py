from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Reservation


class RentalView(TemplateView):
    template = "stats.html"

    def get(self, request):

        return render(
            request, self.template, {"data": Reservation.get_previous_reservations()}
        )
