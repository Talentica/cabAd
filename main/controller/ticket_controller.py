from main.model_form.ticket_form import TicketForm
from main.service import ticket_service
from django.shortcuts import render
from django.views import View


class TicketView(View):

    def get(self, request):
        return render(request, 'ticket/tickets.html', {'tickets': ticket_service.all_tickets()})

    def post(self, request):
        return render(request, 'ticket/ticket.html', {'ticket': ticket_service.create(request.POST)})


class TicketByIdView(View):

    def get(self, request, id):
        return render(request, 'ticket/ticket.html', {'ticket': ticket_service.get_ticket(id)})


def create_ticket(request):
    return render(request, 'ticket/create_ticket.html', {'form': TicketForm})
