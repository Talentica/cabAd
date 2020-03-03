from django import forms

from main.model_form.team_form import TeamForm
from main.models.team import Team
import logging


logger = logging.getLogger(__name__)


def create(team):
    try:
        form = TeamForm(team)
        if form.is_valid():
            return form.save()
        else:
            logger.error("Invalid Team form...!!!")
            raise
    except Exception as e:
        logger.error("Team Service: Exception while creating new team...!!!", e)
        raise


def get_team(team_id):
    try:
        return Team.objects.get(id=team_id)
    except Exception as e:
        logger.error("Team Service: Exception while getting team by id...!!!", e)
        raise


def get_all_teams():
    try:
        return Team.objects.all()
    except Exception as e:
        logger.error("Team Service: Exception while getting all teams...!!!", e)
        raise
