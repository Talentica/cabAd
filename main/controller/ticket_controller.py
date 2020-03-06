from main.model_form.ticket_form import TicketForm
from main.service import ticket_service
from django.shortcuts import render
from django.views import View
import logging

logger = logging.getLogger(__name__)


class TicketView(View):

    def get(self, request):
        try:
            return render(request, 'ticket/tickets.html', {'tickets': ticket_service.all_tickets()})
        except:
            logger.error("Exception in getting ticket view")

    def post(self, request):
        try:
            return render(request, 'ticket/ticket.html', {'ticket': ticket_service.create(request.POST)})
        except:
            logger.error("Exception in post ticket view")


class TicketByIdView(View):

    def get(self, request, id):
        try:
            return render(request, 'ticket/ticket.html', {'ticket': ticket_service.get_ticket(id)})
        except:
            logger.error("Exception in getting ticket by id")


def create_ticket(request):
    return render(request, 'ticket/create_ticket.html', {'form': TicketForm})
