import django_filters
from .models import Games

class GamesFilter(django_filters.FilterSet):
    
    Player_ID = django_filters.CharFilter(lookup_expr='exact', label='球员id')
    SEASON_ID = django_filters.CharFilter(lookup_expr='exact', label='赛季id')

    class Meta:
        model = Games
        fields = ['Player_ID','SEASON_ID']
