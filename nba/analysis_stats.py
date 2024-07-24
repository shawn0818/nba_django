import pandas as pd
#from .nba_stats import get_player_data  # Import the function from your file
from .nba_stats import get_leader_players

def analysis_player_stats(player_id):

    overallBaseData,overallAdvancedData,byYearBaseData = get_player_data(player_id,season="2023-24")

    ByYearBasePlayerDashboard_df = pd.DataFrame(byYearBaseData['rowSet'], columns=byYearBaseData['headers'])

    player_points_total = ByYearBasePlayerDashboard_df['PTS'].sum()

    return player_points_total

def analysis_leader_stats():

    all_leader_data = get_leader_players()

    all_leader_data_df = pd.DataFrame(all_leader_data['rowSet'], columns=all_leader_data['headers'])

    return all_leader_data_df







    