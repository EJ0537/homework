# 숙제: Genie 뮤직 정보 가져오기


# Try 1: rank 출력시 상승, 하강 등의 정보가 같이 나오는 문제가 발
# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
# span = soup.find_all("span")
#
# songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#
# for song in songs:
#     # rank = song.select_one('.number').span.decompose().text
#     title = song.select_one('td.info > a.title.ellipsis').text.strip()
#     artist = song.select_one('td.info > a.artist.ellipsis').text.strip()
#     rank = song.select_one('.number').text.strip()  # rank에서 텍스트 제거하는 것이 너무 어려웠음. 이건 해답코드 참조한 것.
#     # span = song.find("span")
#     # rank = song.select_one('.number').span.decompose()  # rank에서 텍스트 제거하는 것이 너무 어려웠음. 이건 해답코드 참조한 것.
#     # Rank = rank.span.decompose()
#
#     print(rank, title, artist)


## TRY 2 : decompose 사용하여 span tag 제거르 시도해 보았으나 rank가 모두 none으로 떠버리는 문제 발
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
#
# songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#
# for song in songs:
#     title = song.select_one('td.info > a.title.ellipsis').text.strip()
#     artist = song.select_one('td.info > a.artist.ellipsis').text.strip()
#     span = song.find("span")
#     rank = song.select_one('.number').span.decompose()
#     print(rank, title, artist)

## Try 3: 튜터에게 질문하여 rank 부분 바꿔봄 - 성공! + MongoDB에 업데이트 하기
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아감
db = client.dbsparta # 이미 지난번에 만들었는데 아직도 필요한가?

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text.strip()

    # rank 추출하기: 튜터에게 질문해서 구한 답. 즉 decompose는 return하지 않기 때문에 위에서처럼 rank에 값을 넣을 경우 none이 되어버리는 것!
    rank_tag = song.select_one('.number')  # 해당 html 태그 선택
    rank_tag.span.decompose()  # span 태그 없애기
    rank = rank_tag.text.strip()  # 깨끗해진 태그에서 텍스트 추출

    print(rank, title, artist)

    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.songs.insert_one(doc)

####################################################################
####                     Mongo DB에 저장해보기                     #####
####################################################################


# MongoDB에 insert 하기



