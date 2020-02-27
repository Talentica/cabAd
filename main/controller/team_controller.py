from django.shortcuts import render, redirect

from main.service import team_service
from main.model_form.team_form import TeamForm
from django.views import View


class TeamView(View):

    def get(self, request):
        try:
            return render(request, 'team/teams.html', {'teams': team_service.get_all_teams()})
        except:
            print("exception in controller")

    def post(self, request):
        try:
            return render(request, 'team/team.html', {'team': team_service.create(request.POST)})
        except:
            print("exception in controller")
            create_team(request)


class TeamByIdView(View):

    def get(self, request, id):
        try:
            return render(request, 'team/team.html', {'team': team_service.get_team(id)})
        except:
            print("exception in controller")


def create_team(request):
    return render(request, "team/create.html", {'form': TeamForm})