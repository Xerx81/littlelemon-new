from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} on {self.booking_date.strftime('%Y/%m/%d at %H:%M')}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return f"{self.title} : ${self.price}"
