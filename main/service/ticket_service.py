from main.models.ticket import Ticket
from django import forms
import logging

logger = logging.getLogger(__name__)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"


def all_tickets():
    return Ticket.objects.all()


def create(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        logger.error("Request is not valid", request)
