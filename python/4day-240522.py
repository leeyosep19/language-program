#page 52
#기본 입출력
#표준출력
# 이스케이프 문자

# 프로그래밍 할 때 사용할수 있도록 미리 정의 해둔 문자 조합 출력물을 보기 좋게
# 보는 용도로 사용
# 대표적인것 --->\n (엔터)

# print('Hello \'World\'')
# print("Hello 'World'")
# print("Hello \"World\"")
# print('Hello "World"')
#
# print('*\n**\n***')
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# Hello 'World'
# Hello 'World'
# Hello "World"
# Hello "World"
# *
# **
# ***

#page55
# print('재미있는', '파일썬')
# print('Python','Java', 'C', sep=',')
#
# print()  #빈줄
#
# print('영화 타이타닉')
# print('평점', end=':')
# print('5점')
#
# fos = open('sample.py',mode='wt')  #파일열기
# print('print("Hello World")',file=fos)  #파일에 출력(내용저장)
# fos.close()   #파일 닫기
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 재미있는 파일썬
# Python,Java,C
#
# 영화 타이타닉
# 평점:5점

#page56
#형식을 갖춘 문자열 (문자열 포매팅)
#1) % 연사낮 (기본 포매팅) %d %o %X %f%s

# name = 'kai'  #문자열
# print('내이름은 %s입니다,' %name)
#
# height = 120.5  #실수형
# print('내키는 %f cm입니다.' %height)  #소수 여번째 자리까지 표시됨
#
# weight = 23.55
# print('내 몸무게는 %.1f kg입니다.'% weight)
#
# year, month, day = 2014, 8, 25   #정수
# print('내생일은 %d년 %d월 %d일 입니다.'%(year, month, day))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 내이름은 kai입니다,
# 내키는 120.500000 cm입니다.
# 내 몸무게는 23.6 kg입니다.
# 내생일은2014년 8월 25일 입니다.

#page 59
#.format()메소드
# <형식>
# '문자열{}'.format(변수명)

#page 60
# zipcode = '06236'
# print('우편번호 : {}'.format(zipcode))
#
# address = '''서울 특별시 강남구
# 테헤란로 146'''
#
# print('주소 :{addr}'.format(addr =address))
#
# tel1, trl2, tel3 = '02', '538', '0021'
# print('연락쳐 : {0} - {1} - {2}'.format(tel1, trl2, tel3))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 우편번호 : 06236
# 주소 :서울 특별시 강남구
# 테헤란로 146
# 연락쳐 : 02 - 538 - 0021

# ex)
# print('{0:<10}'.format('hi'))  # 전체10칸, 왼쪽정렬
# print('{0:>10}'.format('hi'))  # 전체10칸, 오른쪽정렬
# print('{0:^10}'.format('hi'))  # 전체10칸, 중간정렬
#
# print('{:=^30}'.format('python'))   #전체30 칸, 공백을 = 로 표현, 가운데 정렬
# print('{:!<30}'.format('python'))   #전체30 칸, 공백을 ! 로 표현, 왼쪽 정렬
#
# n = 3.141592
# print('{:.3f}'.format(n))  #소수 세번째 자리까지 반올림
#
# a = '파일썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
# b = '{}{}       {}'.format (100, 200, 300)
# c = '{}{}{}'.format(1, '파이썬', True)
# print(a)
# print(b)
# print(c)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# hi
#         hi
#     hi
# ============python============
# python!!!!!!!!!!!!!!!!!!!!!!!!
# 3.142
# 파일썬 열공하여 첫 연봉 5000만원 만들기
# 100200       300

#page 61
# f-string (f 문자열 포매팅)
# <형식>
# f '문자열{변수명} 문자열'

#ex)
# name = '푸바오'
# age = 3
# print(f'나이 이름은 {name}입니다. 나의 나이는{age}살 입니다.')
# print(f'나는 내년이면 {age+1}살이 됩니다.')
#
# print(f'{"pyhton":=^30}')  #전체30 칸, 공백을 = 로 표현, 가운데 정렬
# print(f'{"pyhton":!<30}')  #전체30 칸, 공백을 ! 로 표현, 왼쪽 정렬
#
# n = 3.014152
# print(f'{n:.3f}')  #소수 세번째 자리 까지
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 나이 이름은 푸바오입니다. 나의 나이는3살 입니다.
# 나는 내년이면 4살이 됩니다.
# ============pyhton============
# pyhton!!!!!!!!!!!!!!!!!!!!!!!!
# 3.014


# 포매팅 비교하기
# n = 3 # 정수
# print('I eat',n,'apple.')
# print('I eat %d apple.' %n)   #% 연산자 포매팅(기본 포매팅)
# print('I eat {} apple.'.format(n))  #.format메서드 방식
# print(f'I eat {n} apple.')    #f- string (f 문자열 포매팅)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# I eat 3 apple.
# I eat 3 apple.
# I eat 3 apple.
# I eat 3 apple.

#page62
#input  (C언어에서  scanf의미0
#표준입력(input)
# n = input('정수를 입력하세요 : ')
# print(n)
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 정수를 입력하세요 : 3
# 3

# name = input('이름을 입력하세요 : ')
# age = input('나이를 입력하세요 : ')
#
# print('입력된 이름은{}입니다.'.format(name))
# print('입력된 나이는 {}살입니다.'.format(age))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\4day-240522.py
# 이름을 입력하세요 : yo seb   # 입력된 값
# 나이를 입력하세요 : 31       # 입력된 값
# 입력된 이름은yo seb입니다.
# 입력된 나이는 31살입니다.

########################################################

#ex) 포매팅 문제
# 변수 number에 정수 5를 담고, 오늘 배운 3사지 포메팅 형식으로 출력해보자
#[화면결과]
# I eat 5 apple
# I eat 5 apple
# I eat 5 apple
number = 5
print('I eat %d apple.' %number)
print('I eat {} apple.'.format(number))
print(f'I eat {number} apple.')

