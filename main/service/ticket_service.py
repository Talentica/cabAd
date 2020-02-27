from main.models.ticket import Ticket
from main.model_form.ticket_form import TicketForm

import logging

logger = logging.getLogger(__name__)


def all_tickets():
    try:
        return Ticket.objects.all()
    except Exception as e:
        logger.error("Exception in fetching all tickets", e)


def create(ticket):
    try:
        form = TicketForm(ticket)
        if form.is_valid():
            form.save()
        else:
            logger.error("Form is not valid")
    except Exception as e:
        logger.error("Error in creating ticket", e)


def get_ticket(ticket_id):
    try:
        return Ticket.objects.get(id=ticket_id)
    except Exception as e:
        logger.error("Error in getting ticket detail", e)
