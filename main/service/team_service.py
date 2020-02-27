from django import forms

from main.model_form.team_form import TeamForm
from main.models.team import Team


def create(team):
    try:
        form = TeamForm(team)
        if form.is_valid():
            return form.save()
        else:
            raise
            print("form not valid")
    except:
        print("exception in service")
        raise


def get_team(team_id):
    try:
        return Team.objects.get(id=team_id)
    except:
        print("exception in service")
        raise


def get_all_teams():
    try:
        return Team.objects.all()
    except:
        print("exception in service")
        raise