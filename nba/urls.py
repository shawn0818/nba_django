from django.urls import path
from . import views
from django.views.generic.list import ListView



app_name = 'nba'
urlpatterns = [
    path("", views.index, name="index"),
    path("teams/<int:team_id>/", views.teams_info, name="teams_info"),
    path("players/<int:player_id>/", views.players_info, name="players_info"),
    path("games/<int:record_id>/", views.games_info, name="games_info"),
    path('gameslist/', views.GamesListView.as_view(),name = "games_list"),
    path('allplayers/', views.get_data,name="player_view")
]