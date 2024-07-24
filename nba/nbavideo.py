import requests
import subprocess

def get_video(gameID,eventID):

    url = 'https://stats.nba.com/stats/videoeventsasset'

    params = {
        'GameID': gameID,
        'GameEventID': eventID
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

    video_data = response_data["resultSets"]['Meta']['videoUrls']

    for video in video_data:

        print(video['surl'])


#get_video('0022301203','4')


def get_video_url(gameID):

    url = 'https://stats.nba.com/stats/videodetailsasset'

    params = {
    'AheadBehind': '',
    'CFID': '',
    'CFPARAMS': '',
    'ClutchTime': '',
    'Conference': '',
    'ContextFilter': '',
    'ContextMeasure': 'FGA',
    'DateFrom': '',
    'DateTo': '',
    'Division': '',
    'EndPeriod': '0',
    'EndRange': '28800',
    'GROUP_ID': '',
    'GameEventID': '',
    'GameID': gameID,
    'GameSegment': '',
    'GroupID': '',
    'GroupMode': '',
    'GroupQuantity': '5',
    'LastNGames': '0',
    'LeagueID': '00',
    'Location': '',
    'Month': '0',
    'OnOff': '',
    'OppPlayerID': '',
    'OpponentTeamID': '0',
    'Outcome': '',
    'PORound': '0',
    'Period': '0',
    'PlayerID': '2544',
    'PlayerID1': '',
    'PlayerID2': '',
    'PlayerID3': '',
    'PlayerID4': '',
    'PlayerID5': '',
    'PlayerPosition': '',
    'PointDiff': '',
    'Position': '',
    'RangeType': '0',
    'RookieYear': '',
    'Season': '2023-24',
    'SeasonSegment': '',
    'SeasonType': 'Regular Season',
    'ShotClockRange': '',
    'StartPeriod': '0',
    'StartRange': '0',
    'StarterBench': '',
    'TeamID': '1610612747',
    'VsConference': '',
    'VsDivision': '',
    'VsPlayerID1': '',
    'VsPlayerID2': '',
    'VsPlayerID3': '',
    'VsPlayerID4': '',
    'VsPlayerID5': '',
    'VsTeamID': ''
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

    # 使用列表推导获取所有的 lurl
   
    video_lurls = [video["lurl"] for video in video_data["Meta"]["videoUrls"]]

    print(video_lurls)
  
    # 使用列表推导获取所有的名称
    video_names = [video["dsc"] for video in video_data["playlist"]]

    # 使用 zip 函数将名称和 URL 合并，然后使用列表推导将每一对名称和 URL 放入其自己的列表
    name_url_result = [[name, url] for name, url in zip(video_names, video_lurls)]

    return name_url_result

get_video_url('0022301203')

import subprocess

# 你的视频 URL
video_url = "http://example.com/video.mp4"

# 使用 ffmpeg 直接从在线视频流生成 GIF
convert_command = f"ffmpeg -i {video_url} -vf 'fps=10,scale=320:-1:flags=lanczos' -c:v palettegen palette.png"
subprocess.run(convert_command, shell=True)
convert_gif_command = f"ffmpeg -i {video_url} -i palette.png -filter_complex 'fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse' output.gif"
subprocess.run(convert_gif_command, shell=True)