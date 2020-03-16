from main.model_form.ticket_form import TicketForm
from main.service import ticket_service
from django.shortcuts import render, redirect
from django.views import View
import logging

logger = logging.getLogger(__name__)


class TicketView(View):

    def get(self, request):
        try:
            return render(request, 'ticket/tickets.html', {'tickets': ticket_service.all_tickets()})
        except Exception as e:
            logger.error("Exception in getting ticket view", e)
            return redirect("create_ticket")

    def post(self, request):
        try:
            ticket = ticket_service.create(request.POST)
            return redirect('get_ticket_by_id', id=ticket.id)
        except Exception as e:
            logger.error("Exception in post ticket view", e)
            return redirect("create_ticket")


class TicketByIdView(View):

    def get(self, request, id):
        try:
            return render(request, 'ticket/ticket.html', {'ticket': ticket_service.get_ticket(id)})
        except Exception as e:
            logger.error("Exception in getting ticket by id", e)
            return redirect("create_or_get_all_tickets")


def create_ticket(request):
    return render(request, 'ticket/create_ticket.html', {'form': TicketForm})
