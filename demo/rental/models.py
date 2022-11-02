from django.db import models
from django.db.models import OuterRef, Subquery


class Rental(models.Model):
    name = models.CharField(max_length=255)


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def get_previous_reservations():
        sub = Reservation.objects.filter(
            rental=OuterRef("rental"), checkin__lt=OuterRef("checkin")
        ).order_by("-checkin")
        reservations = Reservation.objects.annotate(
            previous_id=Subquery(sub.values("id")[:1])
        )

        return reservations
