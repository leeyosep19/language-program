#웹 크롤링의 이해

# #일반 웹 페이지 정보 가져오기
# #page 318
# import  requests  # http요청을 수행해야 할 웹페이지의 소스코드를 가져오는 패키지
#
# url = 'http://www.naver.com'    #가지고올 웹 페이지 주소
# response = requests.get(url)   #가지고온 결과를 response변수에 담느다
# print(response.text)           #결과를 텍스트로
# print('응답코드 : {}'.format(response.status_code))  #응답코드 출력


# #검색결과 웹페이지 정보 가져오기
# #page 319
# import requests
#
# url ='https://search.naver.com/search.naver'
# param = {'query':'파이썬'}   #검색어
# response = requests.get(url,params=param)
# print(response.text)



#page322
# #Beautifulsoup 메서드 사용하기
# # ex)
# from bs4 import BeautifulSoup
#
# html = '''
# <div>
#     <a href="https://www.naver.com">네이버</a>
#     <a href="https://www.kakao.com">카카오</a>
# </div>
# '''
#
# soup = BeautifulSoup(html,'html.parser')
# print(soup.find('a'))            #해당 테그 전체(첫번째 태그만)
# print(soup.find('a').text)       #태그의 텍스틑 부분(내용부분)
# print(soup.find('a').get('href'))  #속성값
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# <a href="https://www.naver.com">네이버</a>
# 네이버
# https://www.naver.com


# #Beautifulsoup 메서드 사용하기 - find_all()
#
# from bs4 import BeautifulSoup
#
# html ='''
# <ul>
#     <li id="movie">영화</li>
#     <li>여행</li>
#     <li>독서</li>
# </ul>
# '''
#
# soup = BeautifulSoup(html,'html.parser')
# print(soup.find_all('li'))      #태그 전체 (리스트 형식으로)
#
# print(soup.find_all('li')[1])
# print(soup.find_all('li')[2])
# print(soup.find_all('li')[0].text)
# print(soup.find_all('li')[1].text)
# print(soup.find_all('li')[2].text)
# print(soup.find_all('li')[0].get('id'))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# [<li id="movie">영화</li>, <li>여행</li>, <li>독서</li>]
# <li>여행</li>
# <li>독서</li>
# 영화
# 여행
# 독서
# movie



# #Beautifulsoup사용하기 -class 속성 활용하기
#
# from bs4 import BeautifulSoup
#
# html ='''
# <div>
#     <div class="gnb">뉴스</div>
#     <div class="gnb">지도</div>
# </div>
# '''
#
# soup = BeautifulSoup(html,'html.parser')
# print(soup.find_all('div',class_='gnb'))    #태그 전체 (속성gnb(리스트형식))
# print(soup.find_all('div',class_='gnb')[0].text)   #내용
# print(soup.find_all('div',class_='gnb')[1].text)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# [<div class="gnb">뉴스</div>, <div class="gnb">지도</div>]
# 뉴스
# 지도


# #Beautifulsoup사용하기 -id 속성 활용하기
#
# from bs4 import BeautifulSoup
#
# html ='''
# <div id="container">
#     <div id="left">왼쪽 영역</div>
#     <div id="right">오른쪽 영역</div>
# </div>
# '''
#
# soup = BeautifulSoup(html,'html.parser')
# print(soup.find('div', id='left'))
# print(soup.find('div', id='right').text)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# <div id="left">왼쪽 영역</div>
# 오른쪽 영역

# #ex) 뉴스 제목
# import  requests
# from bs4 import BeautifulSoup
#
# url = 'https://news.daum.net'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html,'html.parser')
#
# result = soup.find_all('strong',class_='tit_g')
#
# # print(result)
# for i in result:
#     print(i.text.strip())   #공백제거 하고 텍스트만 가져온다


# #주소 찾기
#
# import  requests
# from bs4 import BeautifulSoup
#
# url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html,'html.parser')
#
# for i in soup.find_all('a'):
#     print(i.text)
#     url2 = i.get('href')
#     print(url2)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# 링크1
# http://python.cyber.co.kr/pds/books/python2nd/test1.html
# 링크2
# ./test3.html



# #절대 url 표시
#
# import urllib
# import  requests
# from bs4 import BeautifulSoup
#
# url = 'http://python.cyber.co.kr/pds/books/python2nd/test2.html'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html,'html.parser')
#
# for i in soup.find_all('a'):
#     print(i.text)
#     url2 = i.get('href')
#     link_url = urllib.parse.urljoin(url,url2)
#     print(link_url)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\19day-240701.py
# 링크1
# http://python.cyber.co.kr/pds/books/python2nd/test1.html
# 링크2
# http://python.cyber.co.kr/pds/books/python2nd/test3.html



#이미지 파일을 읽어 들어 저장하기

# import  requests
#
# #이미지를 파일을 변수에 저장한다
#
# image_url ='http://python.cyber.co.kr/pds/books/python2nd/sample1.png'
# imgdata = requests.get(image_url)
#
# print(image_url.split('/'))
# filename = image_url.split('/')[-1]
#
# with open(filename,'wb') as f:
#     f.write(imgdata.content)
#































