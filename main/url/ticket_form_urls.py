from django.urls import path
from main.controller import ticket_controller


urlpatterns = [
    path('', ticket_controller.create_ticket, name='create_ticket')
]