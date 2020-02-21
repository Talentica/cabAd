from django.urls import path, include
from constants import TEAM_URI
from main.url import team_urls


urlpatterns = [
    path(TEAM_URI, include(team_urls))
]