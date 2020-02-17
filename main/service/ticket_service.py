from main.models.ticket import Ticket
from django import forms


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"


def all_tickets():
    return Ticket.objects.all()


def create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()

