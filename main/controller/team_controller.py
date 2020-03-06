from django.shortcuts import render, redirect
from main.service import team_service
from main.model_form.team_form import TeamForm
from django.views import View
import logging


logger = logging.getLogger(__name__)


class TeamView(View):

    def get(self, request):
        try:
            return render(request, 'team/teams.html', {'teams': team_service.get_all_teams()})
        except Exception as e:
            logger.error("Team Controller: Exception while getting all teams...!!!", e)
            return redirect('create_team')

    def post(self, request):
        try:
            team = team_service.create(request.POST)
            return redirect('get_team_by_id', id=team.id)
        except Exception as e:
            logger.error("Team Controller: Exception while creating new team...!!!", e)
            return redirect('create_team')


class TeamByIdView(View):

    def get(self, request, id):
        try:
            return render(request, 'team/team.html', {'team': team_service.get_team(id)})
        except Exception as e:
            logger.error("Team Controller: Exception while getting team by id...!!!", e)
            return redirect('create_or_get_all_teams')


def create_team(request):
    return render(request, "team/create.html", {'form': TeamForm})
