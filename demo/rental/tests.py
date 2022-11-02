from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Rental, Reservation


class TemplateTestCase(TestCase):
    def test_stats_view(self):
        response = self.client.get(reverse("stats"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stats.html")


class ReservationTestCase(TestCase):
    def setUp(self):
        self.rental = Rental(name="test-rental-1")
        self.rental.save()

        self.reservations_1, self.reservations_2 = Reservation.objects.bulk_create(
            [
                Reservation(
                    rental=self.rental,
                    checkin=datetime.today(),
                    checkout=datetime.today() + timedelta(days=1),
                ),
                Reservation(
                    rental=self.rental,
                    checkin=datetime.today() + timedelta(days=3),
                    checkout=datetime.today() + timedelta(days=10),
                ),
            ]
        )

    def test_reservation_previous_id_non_exist(self):
        res = Reservation.get_previous_reservations().get(id=self.reservations_1.id)
        self.assertIsNone(res.previous_id)

    def test_reservation_previous_id_exist(self):
        res = Reservation.get_previous_reservations().get(id=self.reservations_2.id)
        self.assertEqual(res.previous_id, self.rental.id)
