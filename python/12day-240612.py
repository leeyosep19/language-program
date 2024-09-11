# #__name__
#   현재 모듕릐 이름을 담고 있는 내장 변수
#
#  원래 파일에서 실행하면 __name__에 '__name__'이 할당 모듈로 참조하고
#  있는 다른 파일에서 실행하면 __name__에 해당 모듈명이 할당됨

# #ex)
# from my_secure import *
#
# print(secure_no('951012-1234567'))


# # 표준모듈
# #math  모듈
# import math
# print(math.pi) #원주율
# print(math.ceil(1.1))   #올림
# print(math.floor(1.9))   #내림
# print(math.sqrt(25))     #제곱근
# print(math.pow(2,3))  #거듭제곱
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\12day-240612.py
# 3.141592653589793
# 2
# 1
# 5.0
# 8.0


# # random 모듈
# import  random
#
# print(random.randint(1,10))    #1이상 10이하으; 정수중 아무 정수
#
# print(random.randrange(10))     #0~9중 아무 정수
# print(random.randrange(1,11))  #1~10
# print(random.randrange(1,11,2))   #1,3,5,7,9중 하나
#
# print(random.random())   #0이상 1미만 중 아무 숫자(실수)
#
# seasons = ['spring', 'summer', 'fall', 'winter']
# print(random.choice(seasons))
# print(random.sample(range(1,46),6))
#
# my_list = [1,2,3,4,5,]
# random.shuffle(my_list)    #임의로 섞기
# print(my_list)

# #page 213
#
# import random
#
# dice = random.randint(1,6)
# while True:
#     user = int(input('주사위 값은 얼마 일까요?  >>>'))
#     if dice == user:
#         print("{}! 정답 입니다".format(dice))
#         break
#     else:
#         print('오답입 니다! 다시 시도 하세요!')

# #ex) 모듈을 이욯해서 속으로 10초 동안 세어 맞히는 프로그램
# import time
#
# input('엔터를 누르고 10초를 셉니다!!')
# start = time.time()   #현재 시간을 저장
#
# input('10초 후에 다시 엔터를 누릅 니다!!')
# end = time.time()
#
# diff = end - start   #두시간의 차이
# print(f'실제 걸린 시간 : {diff}초')
# print(f'내가 예측한 시간과의 차이 : {abs(diff-10)}초')  #abs 절대값

# 결과값



# #page 218
# from datetime import *
#
# start = datetime.now()  # 계산하기전 현재 날짜와 시간
# total = 0
# for num in range (1, 1000001):
#     total += num
# end = datetime.now()
# elapse = end - start
# elapse = elapse.total_seconds()
# print('총합은 {}입니다.'.format(total))
# print('총 {}초가 소요 되었 습니다.'.format(elapse))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\12day-240612.py
# 총합은 500000500000입니다.
# 총 0.08293초가 소요 되었 습니다.


#page 226
# #파일 입출력
# #파일을 생성하고 문자열 쓰기
#     <형식>(기본 문법)
#     파일 객체명 = open('파일이름', 'w')  #파일 열기 (텍스트 txt)
#     파일 객체명.write('문자열')
#     파일객체명.write(str(숫자))
#     파일객체명.close()
#
#     <형식>(리스트 문법)
#     리스트명 =[값1,값2, ...]
#     파일 객체명 = open('파일이름', 'w')


# #ex)
# file = open('Hello.txt', 'w') #파일 열기
# file.write('Hello World!')
# file.close() #파일 닫기


# # ex) for 를 이용해서 파일 문자열 쓰기
# file = open('Hello.txt','w')
# #상대경로 : 현재 폴더를 기준으로    ./(현재 폴더), ../(상위 폴더)
# #절대경로 : 'C:\python_저녁'
# #예를 들어 c드라이브 안 a라는 폴더에 Hello.txt를 생성(절대경로)
# #'C:/a/Hello.txt'
# for i in range(1,11):
#     data = f'{i}번째 줄입니다.\n'   #\n : 엔터
#     file.write(data)
#
# file.close()


# #ex)for을 이용해서 파일에 새로운 내용 추가하기
# file = open('Hello.txt', 'a')   #파일 열기 (추가모드)
# for i in range(11, 21):
#     data = f'{i}번째 줄입니다~~~~~~~~~!!\n'
#     file.write(data)
# file.close()

#####################################################
#파일입출력 문제
# 새로운 텍스트 파일 text.txt를 만들고 1부터 10까지의 수가 저장 되도록 하여라
#[text.txt 파일 열었을 때]
#12345678910

# file = open('text.txt','w')
# for i in range(1,11):
#
#     file.write(str(i))
#
# file.close()


