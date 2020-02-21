from django import forms
from main.models.team import Team


def create(form):
    try:
        return form.save()
    except:
        pass


def get_team(team_id):
    try:
        return Team.objects.get(id=team_id)
    except:
        pass


def get_all_teams():
    try:
        return Team.objects.all()
    except:
        pass