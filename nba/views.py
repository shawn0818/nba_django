# views.py
from typing import Any, Dict
from .models import Players,Teams,Games
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import sample
from django.views.generic import ListView
from django.core.paginator import Paginator
from .tables import ALLGAMETABLE
from django_filters.views import FilterView
from .filters import GamesFilter
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from .analysis_stats  import  analysis_leader_stats   # Import the function from your file

from .nba_stats import get_video_url

def get_data(request):

    player_total_pts = analysis_leader_stats()

    top10 = player_total_pts[['PLAYER_ID', 'PLAYER_NAME', 'PTS']].head(10)

    # 将每一行转换为列表，并去掉第一个元素
    top10 = [list(row)[1:] for row in top10.itertuples()]

    video_data_list = get_video_url('0022300291','1610612747') 
    #video_data_list = get_video_url('0022300215','1610612760') 
    #video_data_list = get_video_url('0022300171','1610612749') 
    return render(request, 'nba/player_data.html', {"player_total_pts":top10,'video_data_list':video_data_list})


def index(request):

    # Get 10 random objects from each model
    player_objects = sample(list(Players.objects.all()), 15)
    team_objects = sample(list(Teams.objects.all()), 15)
    game_objects = sample(list(Games.objects.all()), 15)

    page_data = {
        "player_objects":player_objects,
        "team_objects" : team_objects,
        "game_objects" : game_objects
    }

    return render(request, 'nba/index.html',page_data)




def players_info(request,player_id):

    player = Players.objects.get(pk=player_id)

    player_url = f"https://cdn.nba.com/headshots/nba/latest/1040x760/{player.PERSON_ID}.png"

    '''
    attributes = {
        'person_id': '球员ID',
        'first_name': '名字',
        'last_name': '姓氏',
        'birthdate': '出生日期',
        'school': '学校',
        'country': '国家',
        'last_affiliation': '上一所属',
        'height': '身高',
        'season_exp': '赛季经验',
        'jersey': '球衣号码',
        'position': '位置',
        'team_id': '球队ID',
        'team_name': '球队名称',
        'team_abbreviation': '球队缩写',
        'team_code': '球队代码',
        'team_city': '球队城市',
        'from_year': '起始年份',
        'to_year': '结束年份',
        'draft_year': '选秀年份',
        'draft_round': '选秀轮次',
        'draft_number': '选秀顺序',
        'position_initials': '位置缩写',
    }
    '''

    data = {
    'person_id': player.PERSON_ID,
    'first_name': player.FIRST_NAME,
    'last_name': player.LAST_NAME,
    'birthdate': player.BIRTHDATE,
    'school': player.SCHOOL,
    'country': player.COUNTRY,
    'last_affiliation': player.LAST_AFFILIATION,
    'height': player.HEIGHT,
    'season_exp': player.SEASON_EXP,
    'jersey': player.JERSEY,
    'position': player.POSITION,
    'team_id': player.TEAM_ID,
    'team_name': player.TEAM_NAME,
    'team_abbreviation': player.TEAM_ABBREVIATION,
    'team_code': player.TEAM_CODE,
    'team_city': player.TEAM_CITY,
    'from_year': player.FROM_YEAR,
    'to_year': player.TO_YEAR,
    'draft_year': player.DRAFT_YEAR,
    'draft_round': player.DRAFT_ROUND,
    'draft_number': player.DRAFT_NUMBER,
    'position_initials': player.POSITION_INITIALS,
}

    context = {
        #'attributes': attributes,
        'data': data,
        'player_url':player_url
    }

    return render(request, 'nba/player_info.html',context)


def teams_info(request,team_id):

    team = Teams.objects.get(pk=team_id)

    # 构建包含字段名称和值的字典
    fields_dict = {field.verbose_name: getattr(team, field.name) for field in team._meta.fields}

    # 调用生成背景图片URL的函数
    background_url = f"https://cdn.nba.com/logos/nba/{team_id}/primary/L/logo.svg"

    return render(request, 'nba/team_info.html', {"team":team, 'fields_dict': fields_dict,'background_url': background_url})


def games_info(request,record_id):

    game = Games.objects.get(pk=record_id)
    fields_and_values = [(field.verbose_name, getattr(game, field.name)) for field in game._meta.fields]
    return render(request, 'nba/game_info.html', {'fields_and_values': fields_and_values})


class GamesListView(ListView):

    model = Games
    template_name = "nba/games_list.html"
    context_object_name = "games_list"
    paginate_by = 20  # 指定每页显示的数量
    #filterset_class = GamesFilter  # 指定使用的过滤器类

    def get_queryset(self):

        queryset = super().get_queryset()

        player_id = self.request.GET.get('player_id')

        season_id = self.request.GET.get('season_id')
        
        # 如果提供了Player_ID参数，使用它来过滤查询集

        if player_id:

            queryset = queryset.filter(Player_ID=player_id)

        if season_id:

            queryset = queryset.filter(SEASON_ID=season_id)
            
        return queryset.order_by('pk')  # 按照主键升序排序

    
   

   






