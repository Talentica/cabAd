from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    pickup_location = models.TextField()
    pickup_time = models.DateTimeField()
    drop_location = models.TextField()
    number_of_seats = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    ac_required = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    total_fare = models.DecimalField(max_digits=5, decimal_places=2)
    distance_travelled = models.DecimalField(max_digits=4, decimal_places=2)
    cab_feedback = models.TextField()

    class Meta:
        db_table = "ticket"
