from django.urls import path, include
from main.constants import uri_constants
from main.url import team_urls, team_form_urls, ticket_urls, ticket_form_urls


urlpatterns = [
    path(uri_constants.TEAM_URI, include(team_urls)),
    path(uri_constants.TEAM_FORM_URI, include(team_form_urls)),
    path(uri_constants.TICKET_URI, include(ticket_urls)),
    path(uri_constants.TICKET_FORM_URI, include(ticket_form_urls))
]