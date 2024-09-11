#for

# 반복 횟수가 정해져 있을때 사용
# <형식>
# for 변수명 in 리스트명:
#     반복할 코드
#
# for 변수명 in range(횟수)   # 시작값이 0
#     반복할 코드 --> 횟수만큼 실행
#
# for 변수명 in range(시작값, 끝값 +1):
#     반복할 코드
#
# for 변수명 in range(시작값, 끝값 +1, 증가값):
#     번복할 코드
#
# for _ in range(횟수): #반복할 변수를 생략가능(횟수만 반복하고 싶을때)
#     반복할 코드

# 시퀀스(순서가 있는 자료형) 와 for문

# #for 와 리스트
# for n in [1, 2, 3]:
#     print(n)
#
# print()
#
# string = ['가위','바위', '보']
# for item in string:
#     print(item)
#
# print('=====================================')
#
# #for 와 문자열
# for ch in 'Hello':
#     print(ch)
#
# print()
#
# #for 와 튜플
# four_seasons = ('Spring','Summer','Autumn', 'Winter')
# for season in four_seasons:
#     print(season)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# 1
# 2
# 3
#
# 가위
# 바위
# 보
# =====================================
# H
# e
# l
# l
# o
#
# Spring
# Summer
# Autumn
# Winter

#page 120
# pwd = input('비밀번호를 입력하세요 >>>> ')
#
# ch_count = 0  # 문자 개수를 담을 변수
# num_count = 0  # 숫자 개수를 담을 변수
#
# for ch in pwd:
#     if ch.isalpha():  # ch문자면 참 아니면 거짓
#         ch_count += 1   # 문자개수 변수 1증가
#     elif ch.isnumeric(): # ch숫자 라면
#         num_count += 1  # 숫자 개수 변수 1증가
#
# if ch_count > 0 and num_count > 0:  # 각각 개수가 0보다 크면
#     print('가능한 비밀번호 입니다.')
# else:
#     print('불가능한 비밀번호 입니다.')

# for와 range()
# for i in range(10):   # 10번 반복, i 변수의 초기값 0
#     print(f'{i}번째 문장 입니다.') # 0~ 9
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# 0번째 문장 입니다.
# 1번째 문장 입니다.
# 2번째 문장 입니다.
# 3번째 문장 입니다.
# 4번째 문장 입니다.
# 5번째 문장 입니다.
# 6번째 문장 입니다.
# 7번째 문장 입니다.
# 8번째 문장 입니다.
# 9번째 문장 입니다.

# for i in range(1,11): # 10 번 반복, i 변수의 초기값1, 끝값 10
#     print(f'{i}번째 문장 입니다.')   # 1~10
#
# print()
#
# for i in range(1,11,2):  # 홀수만 출력, 증가값 2
#     print(f'{i}번째 문장 입니다.')   # 1,3,5,7,9
#
# print()
#
# for i in range(10,0,-1):  # 10부터 1까지 1씩 감소
#     print(f'{i}번째 문장 입니다.') #10~1
#
# print()
# for i in reversed(range(10)):  #reversed : 반전(반대로)
#     print(f'{i}번째 문장 입니다.')  #9~0
#
# print()
#
#
# count = int(input('반복할 횟수를 립력하세요 (1부터 시작) : '))
# for i in range(1,count+1):
#     print(f'{i}번째 문장 입니다.')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# 1번째 문장 입니다.
# 2번째 문장 입니다.
# 3번째 문장 입니다.
# 4번째 문장 입니다.
# 5번째 문장 입니다.
# 6번째 문장 입니다.
# 7번째 문장 입니다.
# 8번째 문장 입니다.
# 9번째 문장 입니다.
# 10번째 문장 입니다.
#
# 1번째 문장 입니다.
# 3번째 문장 입니다.
# 5번째 문장 입니다.
# 7번째 문장 입니다.
# 9번째 문장 입니다.
#
# 10번째 문장 입니다.
# 9번째 문장 입니다.
# 8번째 문장 입니다.
# 7번째 문장 입니다.
# 6번째 문장 입니다.
# 5번째 문장 입니다.
# 4번째 문장 입니다.
# 3번째 문장 입니다.
# 2번째 문장 입니다.
# 1번째 문장 입니다.
#
# 9번째 문장 입니다.
# 8번째 문장 입니다.
# 7번째 문장 입니다.
# 6번째 문장 입니다.
# 5번째 문장 입니다.
# 4번째 문장 입니다.
# 3번째 문장 입니다.
# 2번째 문장 입니다.
# 1번째 문장 입니다.
# 0번째 문장 입니다.
#
# 반복할 횟수를 립력하세요 (1부터 시작) : 16
# 1번째 문장 입니다.
# 2번째 문장 입니다.
# 3번째 문장 입니다.
# 4번째 문장 입니다.
# 5번째 문장 입니다.
# 6번째 문장 입니다.
# 7번째 문장 입니다.
# 8번째 문장 입니다.
# 9번째 문장 입니다.
# 10번째 문장 입니다.
# 11번째 문장 입니다.
# 12번째 문장 입니다.
# 13번째 문장 입니다.
# 14번째 문장 입니다.
# 15번째 문장 입니다.
# 16번째 문장 입니다.


#ex) 1부터 100 까지의 수즁 3의 배수, 5의 배수, 3과 5의 공 배수
# for i in range(1, 101): #초기값은 1, 끝값은 100, 증가값 1(생략)
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} : 3과 5의 공배수')
#     elif i % 3 == 0:
#         print(f'{i} : 3의 배수')
#     elif i % 5 == 0:
#         print(f'{i} : 5의 배수')
#     else:
#         print(i)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# 1
# 2
# 3 : 3의 배수
# 4
# 5 : 5의 배수
# 6 : 3의 배수
# 7
# 8
# 9 : 3의 배수
# 10 : 5의 배수
# 11
# 12 : 3의 배수
# 13
# 14
# 15 : 3과 5의 공배수
# 16
# 17
# 18 : 3의 배수
# 19
# 20 : 5의 배수
# 21 : 3의 배수
# 22
# 23
# 24 : 3의 배수
# 25 : 5의 배수
# 26
# 27 : 3의 배수
# 28
# 29
# 30 : 3과 5의 공배수
# 31
# 32
# 33 : 3의 배수
# 34
# 35 : 5의 배수
# 36 : 3의 배수
# 37
# 38
# 39 : 3의 배수
# 40 : 5의 배수
# 41
# 42 : 3의 배수
# 43
# 44
# 45 : 3과 5의 공배수
# 46
# 47
# 48 : 3의 배수
# 49
# 50 : 5의 배수
# 51 : 3의 배수
# 52
# 53
# 54 : 3의 배수
# 55 : 5의 배수
# 56
# 57 : 3의 배수
# 58
# 59
# 60 : 3과 5의 공배수
# 61
# 62
# 63 : 3의 배수
# 64
# 65 : 5의 배수
# 66 : 3의 배수
# 67
# 68
# 69 : 3의 배수
# 70 : 5의 배수
# 71
# 72 : 3의 배수
# 73
# 74
# 75 : 3과 5의 공배수
# 76
# 77
# 78 : 3의 배수
# 79
# 80 : 5의 배수
# 81 : 3의 배수
# 82
# 83
# 84 : 3의 배수
# 85 : 5의 배수
# 86
# 87 : 3의 배수
# 88
# 89
# 90 : 3과 5의 공배수
# 91
# 92
# 93 : 3의 배수
# 94
# 95 : 5의 배수
# 96 : 3의 배수
# 97
# 98
# 99 : 3의 배수
# 100 : 5의 배수

#page 125
# dan = int(input('출력할 구구단을 입력하세요 >>>'))
# for n in range(1, 10):
#     print('{} X {} = {}'.format(dan,n,dan*n))

# 결과값


#ex) 중첩 for문릉 사용한 구구단 만들기

# for i in range(2,10): #단부분(2~9)
#     print('*********{}단**********'.format(i))
#
#     for k in range(1, 10): #곱해지는 수(1~9)
#        print('{} X {} = {}'.format(i,k,i*k))
#     print()   # 단 끝난 후 빈 줄 추가


#ex) 중첩 for 문을 이용한 별 찍기
# for i in range(5):
#     for j in range(5):
#         print('*',end='')
#     print()
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# *****
# *****
# *****
# *****
# *****

# print()
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# print()
#
# for i in range(5):
#     for j in range(5):
#         if i > j:
#             print(' ', end='')
#         else:
#             print('*',end='')
#     print()
#
# print()
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end='')
#     print()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# *
#  *
#   *
#    *
#     *
#
# *****
#  ****
#   ***
#    **
#     *
#
# *
# **
# ***
# ****
# *****


###############################################
#문제
# for 이용해서 1~5 까지의 숫자드을 차럐대로 출력하기
# (range함수 사용)
# [화면 실행결과]
# 1 2 3 4 5

# for n in range(1, 6):
#     print( n, end=' ')

#for 문 1부터 10까지의 합
# [화면 실행결과]
# 1부터 10 까지의 합 : 55
# 힌트 :  합계를 담은 변수를 먼저 만들어서 초기화하고 진행하기, range사용

# total = 0
# for i in range(1,11):
#     total += i
# print('1부터 10까지의 합 : {}' .format(total))


# for 문을 이용하여 1부터 키보드로 입력한 값까지의 합계 구하기
# [화면 실행결과]
# 값을 입력하시오 : 123
# 1부터 123까지의 합계 : 7626

# total = 0
# num = int(input('값을 입력하시오 : '))
# for n in range(1,num+1):
#     total += n
# print('1부터 {}까지의 합 : {}'.format(num,total))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\7day-240529.py
# 값을 입력하시오 : 123
# 1부터 123까지의 합 : 7626