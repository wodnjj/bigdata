# 다음 영화 순위 크롤링 하는 프로그램
import requests
from bs4 import BeautifulSoup
import csv

# 다음 영화 정보 가져오는 함수
def get_dmv():
    # 리스트로 함수 밖으로 전달 시킬 변수
    m_list = list() # 영화정보 리스트 변수 선언
    # 다음 영화 순위 페이지 URL
    url = "https://movie.daum.net/ranking/reservation"

    # HTTP 요청 보내기
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # HTTP 요청이 성공했는지 확인하기
    if response.status_code == 200:
        # HTML 파싱하기
        soup = BeautifulSoup(response.text, "html.parser")
        # 영화 순위 리스트 찾기
        rank = 0
        movie_list = soup.select(".thumb_cont")
        for tr in movie_list:
            rank = rank + 1
            a_tag = tr.select_one("a")
            txt_grade = tr.select_one("span.txt_grade")
            txt_num = tr.select_one("span.txt_num")
            txt_date = tr.select_one(".txt_info > span.txt_num")
            m_list.append([rank, a_tag.text, txt_grade.text, txt_num.text, txt_date.text])
    else:
        print("HTTP 요청 실패")
    
    return m_list