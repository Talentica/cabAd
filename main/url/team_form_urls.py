from django.urls import path
from main.controller import team_controller


urlpatterns = [
    path('', team_controller.create_team, name='create_team')
]