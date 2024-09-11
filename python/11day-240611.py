#page189
#가변 매개변수 : 매개변수(입력값)의 개수를 정확히 모를때 사용

# <형식>
# def 함수이름(*매개변수명) : # 함수정의    *args
#     수행할 코드
#
# 함수이름(필요한 인수만큼 입력 )  #함수 호출

#page 191
# def adder(*args):                   #함수정의
#     print('{}의 합은 {}입니다.'.format(args,sum(args)))
#
# adder(1, 2)                    #함수호출
# adder(1,2,3)
# adder(1,2,3,4)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# (1, 2)의 합은 3입니다.
# (1, 2, 3)의 합은 6입니다.
# (1, 2, 3, 4)의 합은 10입니다.

# #ex)
# def add_mul(choice,*args): #함수정의 (가변 매개변수를 맨뒤로 배치)
#     if choice == 'add':
#         answer = 0          #합계를 담을 변수 초깃값을 0으로 한다
#         for i in args:      #가변 매개변수 args의 개수만큼 반복
#             answer += i      #answer = answer+i
#
#     elif choice == 'mul':
#         answer = 1        #초기값을 1로 한다 (0으로 하면 계속 0이됨)
#         for i in args:
#             answer *= i   #answer = answer *i
#
#     return  answer     #결과로 나온 answer을 반환한다
#
# a = add_mul('add',1,2,3)
# print(a)#함수호출
#
# b = add_mul('mul',4,5,6,7)
# print(b)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# 6
# 840

# #지역 변수 / 전역 변수
#     지역변수 : 한정된 지역(함수 안)에서 사용
#     전역변수 : 프로그래 전체에서 사용,예약어 global

# #ex)
# a = 100        #전역변수
#
# def func1():   #함수정의
#     a = 10     #지역변수 (이 함수는 안에서 사용)
#     print('func1 함수에서의 a의 값 : {}'.format(a))
#
# def func2():   #함수 정의
#     print('func2 함수에서의 a의 값 : {}'.format(a))
#
# func1()   #함수 호출    (우선 순위 전역 변수보다 지역변수가 나온다)
# func2()   #함수호출
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# func1 함수에서의 a의 값 : 10
# func2 함수에서의 a의 값 : 100


# #ex) 전역변수의 값을 변경해야 하는 경우
# a = 0 #전역변수
#
# def f():    #함수 정의
#     global a     #전역변수 a를 가리킨다(지역변수가아니고 전역변수가로)
#     a = 10        #전역 변수 a의 값을 10 으로 변경한다
#
# print('함수 호출 전 a : {}'.format(a))
# f()    #함수호출
# print('함수 호출 후 a : {}'.format(a))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# 함수 호출 전 a : 0
# 함수 호출 후 a : 10


#page 195
# def coffee_machine(money,pick):
#     print('{}원에 {}를 선택하셨습니다.'.format(money,pick))
#     menu ={
#         '아메리카노' : 1000,
#         '카페라떼' : 1500,
#         '카푸치노' : 2000,
#         '돌체라떼' : 2000
#     }
#     if  pick not in menu:
#         print('{}는 판매하지 않습니다'.format(pick))
#         return  money,'메뉴에 없음'
#     elif menu[pick] > money:
#         print('{}는 {}원입니다.'.format(pick,menu[pick]))
#         return money, '금액이 부족'
#     else:
#         return money -menu[pick],pick
#
# order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노, 돌체라떼)>>>>>')     #pick
# pay = int(input('얼마를 내시나요? >>>>'))                                         #money
#
# change, coffee = coffee_machine(pay,order)                       #반환값이 2개이므로 결가변수 2개
# print('잔돈 {}원, 커피{}'.format(change,coffee))

# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# 커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노, 돌체라떼)>>>>>자몽에이드
# 얼마를 내시나요? >>>>5000
# 5000원에 자몽에이드를 선택하셨습니다.
# 자몽에이드는 판매하지 않습니다
# 잔돈 5000원, 커피메뉴에 없음

# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# 커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노, 돌체라떼)>>>>>카푸치노
# 얼마를 내시나요? >>>>1000
# 1000원에 카푸치노를 선택하셨습니다.
# 카푸치노는 2000원입니다.
# 잔돈 1000원, 커피금액이 부족

# #모듈과 impart
# #모듈을 불러와서 사용하기
#
#     <형식>
#     import 모듈이름 as 별칭 -->as 별칭 생략가능
#     또는
#     from 모듈이름 import 모듈함수
#     ----> 호출시 모듈이름을 생략하고 함수만 사용하고 싶을때
#     from 모듈이름 import *
#     ---->모듈 안에 있는 모든 함수를 당겨쓸때 모두의 의미를 가진 *를 사용

# #ex) import 방식
# import  m    #m이라는 모듈(파일썬 파일)을 불러온다
#
# result1 = m.add(1,2)    #m모듈에 있는 add함수 호출
# result2 = m.sub(2,1)    #m모듈에 있는 sub함수 호출
# print('result1 : {}'.format(result1))
# print('result2 : {}'.format(result1))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# result1 : 3
# result2 : 3


# #ex)from방식
# from m import  mul,div   #m모듈에 있는 mul,div 함수를 가져온다
#
# result1 = mul(1,2)
# result1 = div(2,1)
# print('result1 : {}'.format(result1))
# print('result2 : {}'.format(result1))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# result1 : 2.0
# result2 : 2.0

##ex)from방식(2)
# from m import *   #m모듈안에있는 모든 함수를 가져오겠다
#
# x = int(input('x를 입력하세요 : '))
# y = int(input('y를 입력하세요 : '))
# n1 = add(x, y)
# n2 = sub(x ,y)
# n3 = div(x, y)
# n4 = mul(x, y)
# print(n1, n2, n3, n4, sep='\n')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# x를 입력하세요 : 5
# y를 입력하세요 : 8
# 13
# -3
# 0.625
# 40


# #page 209
# from my_secure import *
#
# print(secure_name('김철수'))
# print(secure_no('951012-1234567'))
# print(secure_phone('010-1234-5678'))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\11day-240611.py
# 김**
# 951012-1******
# 010-****-5678

##############################################
#사용자 함수 문제
# 두개의 정수를 전달맏아서 그 두 수의 몫과 나머지를 가가 반환하는
# 함수를 만들어보자. 이때 두개의 정수는 input()을 이용해서 입력 받는다
# 반환값 return이 있도록하고, 함수이름과 매개변수이름 등은 자유롭게한다
# 함수호출은 한번만 한다
# [화면실행결과]
# 첫번째 수를 입력하세요 : 5
# 두번째 수를 입력하세요 : 2
# 몫 :2, 나머지1
#
# num1 = int(input('첫번째 수를 입력하세요 :'))
# num2 = int(input('두번째 수를 입력하세요 :'))
#
# def i(num1,num2):
#     return num1 // num2, num1 % num2
#
# result1, result2 = i(num1,num2)
# print('몫은 {}, 나머지 {}'.format(result1, result2))






