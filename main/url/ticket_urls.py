from django.urls import path
from main.controller import ticket_controller


urlpatterns = [
    path('', ticket_controller.TicketView.as_view(), name='create_or_get_all_tickets')
]