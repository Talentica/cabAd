from django.urls import path
from main.controller import ticket_controller


urlpatterns = [
    path('<int:id>', ticket_controller.TicketByIdView.as_view(), name='get_ticket_by_id'),
    path('', ticket_controller.TicketView.as_view(), name='create_or_get_all_tickets')
]