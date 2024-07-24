import json
import requests

#获取数据
def get_player_data(player_id, season):
    url = 'https://stats.nba.com/stats/playerdashboardbyyearoveryearcombined'
    params = {
        'DateFrom': '',
        'DateTo': '',
        'GameSegment': '',
        'LastNGames': 0,
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Base',
        'Month': 0,
        'OpponentTeamID': 0,
        'Outcome': '',
        'PORound': 0,
        'PaceAdjust': 'N',
        'PerMode': 'PerGame',
        'Period': 0,
        'PlayerID': player_id,
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': season,
        'SeasonSegment': '',
        'SeasonType': 'Regular Season',
        'ShotClockRange': '',
        'VsConference': '',
        'VsDivision': '',
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com",
        "Pragma": "no-cache",
        "Referer": "https://www.nba.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
    }
    
    response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()  # 抛出异常如果 HTTP 状态码不是 200

    response_data = response.json()  # Parse response as JSON

    for resultSet in response_data["resultSets"]:

        if resultSet["name"] == "OverallBasePlayerDashboard":
            overallBaseData = resultSet 
            #最新的基础数据
        elif resultSet["name"] == "OverallAdvancedPlayerDashboard":
            overallAdvancedData = resultSet
            #最新的高阶数据
        elif resultSet["name"] == "ByYearBasePlayerDashboard":
            byYearBaseData = resultSet
            #历年基础数据

    return overallBaseData,overallAdvancedData,byYearBaseData


#获取所有球员总得分列表

def get_leader_players():

    url = 'https://stats.nba.com/stats/leagueLeaders'

    params = {
        "ActiveFlag": "No",
        "LeagueID": "00",
        "PerMode": "Totals",
        "Scope": "S",
        "Season": "All Time",
        "SeasonType": "Regular Season",
        "StatCategory": "PTS"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com",
        "Pragma": "no-cache",
        "Referer": "https://www.nba.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
    }
    
    response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()  # 抛出异常如果 HTTP 状态码不是 200

    response_data = response.json() # Parse response as JSON

    leader_data = response_data["resultSet"]

    return leader_data

def get_video_url(gameID,teamID):

    url = 'https://stats.nba.com/stats/videodetailsasset'

    params = {
    
            "LeagueID": "00",
            "Season": "2023-24",
            "SeasonType": "Regular Season",
            "TeamID": teamID,
            "PlayerID": 0,
            "GameID": gameID,
            "Outcome": "",
            "Location": "",
            "Month": 0,
            "SeasonSegment": "",
            "DateFrom": "",
            "DateTo": "",
            "OpponentTeamID": 0,
            "VsConference":"",
            "VsDivision": "",
            "Position": '',
            "RookieYear": '',
            "GameSegment": '',
            "Period": 0,
            "LastNGames": 0,
            "ClutchTime": '',
            "AheadBehind": '',
            "PointDiff": '',
            "RangeType": 0,
            "StartPeriod": 1,
            "EndPeriod": 10,
            "StartRange": 0,
            "EndRange": 28800,
            "ContextFilter": "",
            "ContextMeasure": "FGA",
            "OppPlayerID": ""
	
}

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com",
        "Pragma": "no-cache",
        "Referer": "https://www.nba.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
    }
    
    response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()  # 抛出异常如果 HTTP 状态码不是 200

    response_data = response.json() # Parse response as JSON

    video_data = response_data["resultSets"]

    print(video_data)

    # 使用列表推导获取所有的 lurl
   
    video_lurls = [video["lurl"] for video in video_data["Meta"]["videoUrls"]]

    print(video_lurls)
  
    # 使用列表推导获取所有的名称
    video_names = [video["dsc"] for video in video_data["playlist"]]

    # 使用 zip 函数将名称和 URL 合并，然后使用列表推导将每一对名称和 URL 放入其自己的列表
    name_url_result = [[name, url] for name, url in zip(video_names, video_lurls)]

    return name_url_result
    






