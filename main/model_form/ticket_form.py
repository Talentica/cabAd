from django import forms
from main.models.ticket import Ticket
from django.conf.global_settings import DATETIME_INPUT_FORMATS


class TicketForm(forms.ModelForm):
    pickup_time = forms.DateTimeField(
        input_formats=[DATETIME_INPUT_FORMATS[2]],
        widget=forms.widgets.DateTimeInput(attrs={'placeholder': 'yyyy-mm-dd hh:mm'})
    )

    class Meta:
        model = Ticket
        fields = ["pickup_location", "pickup_time", "drop_location", "number_of_seats", "ac_required"]
