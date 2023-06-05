# 다음 영화 순위 크롤링 하는 프로그램
import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

# 엑셀파일 쓰기 준비
# 엑셀파일 쓰기
write_wb = Workbook()

# Sheet1에다 입력
write_ws = write_wb.active
# 컬럼데이터 입력
write_ws['A1'] = '순위'
write_ws['B1'] = '제목'
write_ws['C1'] = '평점'
write_ws['D1'] = '예매율'
write_ws['E1'] = '개봉날짜'

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
        # 순위
        rank = rank + 1
        m1 = f'{rank}위'
        # 제목 
        a_tag = tr.select_one("a")
        m2 = a_tag.text 
        # 평점
        txt_grade = tr.select_one("span.txt_grade")
        m3 = txt_grade.text 
        # 예매율
        txt_num = tr.select_one("span.txt_num")
        m4 = txt_num.text 
        # 개봉날짜
        txt_date = tr.select_one(".txt_info > span.txt_num")
        m5 = txt_date.text 

        #행 단위로 추가
        write_ws.append([m1, m2, m3, m4, m5])

    # 엑셀 파일 저장
    write_wb.save('영화순위.xlsx')

else:
    print("HTTP 요청 실패")