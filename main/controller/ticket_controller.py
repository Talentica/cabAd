from main.service import ticket_service
from django.shortcuts import render


def create(request):
    if request.method == "POST":
        ticket = ticket_service.create(request)


def all_tickets(request):
    tickets = ticket_service.all_tickets()
    return render(request, 'ticket/tickets.html', {'tickets': tickets})
