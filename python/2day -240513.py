# 여러개의 변수
# a, b, c = 1, 2, 3  #변수의 값으 대입할때 한번에 순서대로 대입, 짝이 맞아야함
# print(a)
# print(b)
# print(c)
#
# a = b = c = 4
# print(a)
# print(b)
# print(c)
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# 1
# 2
# 3

# 4
# 4
# 4


#변수의 교환
# a = 1
# b = 2
# print('a변수 :', a)
# print('b변수 :', b)
#
# a, b = b, a    #변수 교환(맞교환 가능)
# print('a변수 :', a)
# print('b변수 :', b)
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# a변수 : 1
# b변수 : 2

# a변수 : 2
# b변수 : 1

#자료형

# 프로그래밍 할때 쓰이는 , 숫자, 문자열 등 자료 형태로 사용 하는 모든것 다른언 어의 경우는 변수 설정시 애초에
# 타입(자료형) 을 설정 해야 하는 경우가 많음, 파일썬의 경우는 값을 할당 하면 그 때 타입이 결정 되기 때문에
# 초보자가 배우기 쉽다.

# type 함수로 자료형을 볼수있다.

# ex)type
# print(type(1))   #1은 정수형 (int)
# print(type(1.0))  # 실수형(float)
# print(type('Hello'))  #문자열(str)
# print(type(True))   #논리형(bool)
#
# a = 100
# print(type(a))   #int
#
# a = 3.14
# print(type(a))  #float
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# <class 'int'>
# <class 'float'>


# 정수형
# print(int(1.9))
# print(int(True))   #정수1은 참
# print(int(False))   #0은 거짓
#
# b = ('100')  #문자열
# print(type(b))
# c = 100   #정수
# print(type(c))
#
# d = int(b)    #b변수의 값을 정수형으로 변환하여 d변수에 담아라
# print(type(d))
# print(d)
#
# print()
# n = 95 #10진수 정수
# print(bin(n))   #2진수 (0 ,1)
# print(oct(n))    #8진수 (0~ 7)
# print(hex(n))    #16진수 (0~9, a~f)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# 1
# 1
# 0
# <class 'str'>
# <class 'int'>
# <class 'int'>
# 100
#
# 0b1011111
# 0o137
# 0x5f

# 실수
# print(float(1))
# print(float(True))
# print(float(False))
# print(float('3.14'))
# print(float('100'))
# # print(float('가'))   # 문자는 오류난다
# print()
#
# # 논리형
# print(bool(0))
# print(bool(1))
# print(bool(2))    #0을 제외한 나머지수는 모두 참이다
# print(bool(''))   #비어있는 값은 거짓
# print(bool([]))
#
# print()
#
# #문자열
# print(str(100))
# print(str(True))
# print(str(False))
# print(str(3.14))
#
# print()
# print('Hello, python!')  #작은 따움표
# print("Hello, python!")  #큰 따움표
#
# print('''
# Life is too short,
# you need python,
# ''')    #여러줄 출력 할때는 따움표 3개를 시작과 끈에 넣는다
#
# print("It's me.")  #'를 표현 할때 편리하다
# print('"파일썬 아주 쉽네."라고 그가 말했다.') #인용문(")넣을때도 편리하다
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# 1.0
# 1.0
# 0.0
# 3.14
# 100.0
#
# False
# True
# True
# False
# False
#
# 100
# True
# False
# 3.14
#
# Hello, python!
# Hello, python!
#
# Life is too short,
# you need python,
#
# It's me.
# "파일썬 아주 쉽네."라고 그가 말했다.

#문자열 인덱싱
# [0] : 문자열의 처음
# [-1] : 문자열의 마지막

#ex)
# print('안녕하세요'[0])   #원하는 글자만 따올수 있다.
# print('안녕하세요'[1])
# print('안녕하세요'[2])
# print('안녕하세요'[3])
# print('안녕하세요'[4])
# print()
#
# print('안녕하세요'[-1])
# print('안녕하세요'[-2])
# print('안녕하세요'[-3])
# print('안녕하세요'[-4])
# print('안녕하세요'[-5])
# print()
#
# a = 'My python'
# print(a)
# print(a[0])
# print(a[2])    #인덱싱에 포함(공백도 글자다!)
# print(a[-1])
# 결과값
# D:\python - 1\pythonProject\.venv\Scripts\python.exe
# "D:\python-1\pythonProject\2day -240513.py"
# 안
# 녕
# 하
# 세
# 요
#
# 요
# 세
# 하
# 녕
# 안
#
# My
# python
# M
#
# n

#문자열 슬라이싱
# 문자열의 구간을 표시 예를 들어 a라는 변수가 있다면 a[시작번호 : 끝번호+1]
# [:] ----> 처음부터 끝까지, 모두를 의미

# print('안녕하세요'[1:3])  #1~3번 앞-->1번,2번
# print('안녕하세요'[2:5])  #2번~5번 앞-->2번,3번, 4번
#
# print()
#
# a = 'python'
# print(a[0:2])
# print(a[:])  # 모두 다 (전체)
#
# print(a[:3])  #0번~3번 앞 (처음부터, 시작번호를 생략할수있다)
# print(a[2:])  #2번~끝까지  (끝번호를 생략할수있다)
#
# print()
#
# b = 'Hello'
# print(b[1])  #인덱싱
# print(b[2:4])  #슬라이싱
# print(b)    #원본에는 영향을 주지 않는다
#
# c = b[1]
# d = b[2:4] #다음에 도 사용할 수있다
# print(c)
# print(d)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# 녕하
# 하세요
#
# py
# python
# pyt
# thon
#
# e
# ll
# Hello
# e
# ll

#컬렉션 자료형
# 리스트(list)
# a = [] #빈 리스트
# b = [1, 2, 3]  #정수로만 이루어진 리스트
# c = ['a', 'b', 'c', 'd']  #문자열 4개로 이루어진 리스트
# d = [1, 2, 'a', 'b', True]  #여러 자료형으로 이루어진 리스트
# e = [1, 2, ['a','b']] #중첩 리스트
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
#
# print()
# #리스트 인덱싱
# print(b[1])
# print(c[3])
# print(d[0])
# print(e[2])
# print(e[-1])    #중첩 리스트안에 있는 값을 출력하고 자 할때
# print(e[2][0])
#
# f = [1, 2, ['a','b', ['안녕','하세요']]]
# print(f)
# print(f[2])
# print(f[2][2])
# print(f[2][2][0])
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# []
# [1, 2, 3]
# ['a', 'b', 'c', 'd']
# [1, 2, 'a', 'b', True]
# [1, 2, ['a', 'b']]
#
# 2
# d
# 1
# ['a', 'b']
# ['a', 'b']
# a
# [1, 2, ['a', 'b', ['안녕', '하세요']]]
# ['a', 'b', ['안녕', '하세요']]
# ['안녕', '하세요']
# 안녕

# 리스트 요소(값) 수정
# a = ['a', 'b', 'c']
# print(a)
# a[1] = 'merong!'
# print(a)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\pythonProject\2day -240513.py"
# ['a', 'b', 'c']
# ['a', 'merong!', 'c']