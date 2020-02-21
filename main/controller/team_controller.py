from django.shortcuts import render, redirect

from main.service import team_service
from main.model_form.team_form import TeamForm
from django.views import View


class CreateTeamView(View):
    team_form = TeamForm

    def get(self, request):
        form = self.team_form()
        return render(request, "team/create.html", {'form': form})

    def post(self, request):
        form = self.team_form(request.POST)
        if form.is_valid():
            team = team_service.create(form)
            return render(request, 'team/team.html', {'team': team})
        else:
            self.get(request)


def get_team(request, team_id):
    return render(request, 'team/team.html', {'team': team_service.get_team(team_id)})


def get_all_teams(request):
    return render(request, 'team/teams.html', {'teams': team_service.get_all_teams()})
