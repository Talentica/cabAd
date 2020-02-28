from django import forms
from main.models.ticket import Ticket


class TicketForm(forms.ModelForm):
    pickup_time = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Ticket
        fields = ["pickup_location", "pickup_time", "drop_location", "number_of_seats", "ac_required"]
