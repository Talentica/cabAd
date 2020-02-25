from django.urls import path
from main.controller import team_controller


urlpatterns = [
    path('<int:id>', team_controller.TeamByIdView.as_view(), name='get_team_by_id'),
    path('', team_controller.TeamView.as_view(), name='create_or_get_all_teams')
]
