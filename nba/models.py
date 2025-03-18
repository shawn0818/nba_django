from django.db import models

# Create your models here.
class Teams(models.Model):
    TEAM_ID = models.CharField(max_length=50,primary_key=True)
    ABBREVIATION = models.CharField(max_length=50)
    NICKNAME_x = models.CharField(max_length=50)
    YEARFOUNDED_x = models.CharField(max_length=50)
    CITY_x = models.CharField(max_length=50)
    ARENA =  models.CharField(max_length=50)

    class Meta:
        db_table = 'teams-info' # 已存在的表名

class Players(models.Model):
    PERSON_ID =  models.CharField(max_length=50,primary_key=True)
    FIRST_NAME =  models.CharField(max_length=50)
    LAST_NAME =  models.CharField(max_length=50)
    BIRTHDATE =  models.DateField()
    SCHOOL =  models.CharField(max_length=50)
    COUNTRY =  models.CharField(max_length=50)
    LAST_AFFILIATION =  models.CharField(max_length=50)
    HEIGHT =  models.CharField(max_length=50)
    SEASON_EXP = models.IntegerField()
    JERSEY = models.CharField(max_length=10)
    POSITION = models.CharField(max_length=10)
    TEAM_ID = models.CharField(max_length=10)
    TEAM_NAME = models.CharField(max_length=30)
    TEAM_ABBREVIATION = models.CharField(max_length=30)
    TEAM_CODE = models.CharField(max_length=30)
    TEAM_CITY = models.CharField(max_length=30)
    FROM_YEAR = models.IntegerField()
    TO_YEAR = models.IntegerField()
    DRAFT_YEAR = models.IntegerField()
    DRAFT_ROUND = models.CharField(max_length=30)
    DRAFT_NUMBER = models.CharField(max_length=30)
    POSITION_INITIALS = models.CharField(max_length=30)

    class Meta:
        db_table = 'players-info' # 已存在的表名

class Games(models.Model):
    RECORD_ID = models.IntegerField(primary_key=True)   
    SEASON_ID = models.CharField(max_length=50)
    Player_ID = models.CharField(max_length=50)
    Game_ID = models.CharField(max_length=50)
    GAME_DATE =  models.DateField()
    MATCHUP = models.CharField(max_length=50)
    WL = models.CharField(max_length=50)
    MIN = models.IntegerField()
    FGM = models.IntegerField()
    FGA = models.IntegerField()
    FG3M = models.IntegerField(blank=True)
    FG3A = models.IntegerField()
    FTM = models.IntegerField()
    FTA = models.IntegerField()
    OREB = models.IntegerField()
    DREB = models.IntegerField()
    REB = models.IntegerField()
    AST = models.IntegerField()
    STL = models.IntegerField()
    BLK = models.IntegerField()
    TOV = models.IntegerField()
    PF = models.IntegerField()
    PTS = models.IntegerField()

    class Meta:
        db_table = 'game-regular' # 已存在的表名

