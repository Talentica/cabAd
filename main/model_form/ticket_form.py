from django.forms import ModelForm
from main.models.ticket import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["pickup_location", "pickup_time", "drop_location", "number_of_seats", "ac_required"]
