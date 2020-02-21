from django import forms
from main.models.team import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
