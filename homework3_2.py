#############################################################
#          HW3: Genie 뮤직 정보 가져오기 + MongoDB 생성
#############################################################

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text.strip()

    # rank 추출하기
    rank_tag = song.select_one('.number')
    rank_tag.span.decompose()  # span 태그 없애기
    rank = rank_tag.text.strip()  # 깨끗해진 태그에서 텍스트 추출

    print(rank, title, artist)

    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.songs.insert_one(doc)




