from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
   # created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    pickup_location = models.CharField(max_length=100)
    pickup_time = models.DateTimeField()
    drop_location = models.CharField(max_length=100)
    number_of_seats = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    ac_required = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    total_fare = models.DecimalField(max_digits=5, decimal_places=2)
    distance_travelled = models.DecimalField(max_digits=4, decimal_places=2)
    cab_feedback = models.CharField(max_length=200)

    class Meta:
        db_table = "ticket"
