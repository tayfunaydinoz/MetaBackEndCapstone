from django.db import models

# Create your models here.
class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.IntegerField(default=1)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingDate=models.DateField()
