#input의 형변환
# a = input('입력 : ')   # input을 사용하면  문자열됨 (str)
# print('변수 a의 값 : {}'.format(a))
# print('변수 a의 자료형(타입) : {}'.format(type(a)))
# print()
#
# b = int(input('입력 : '))  #타입을 정수(int)로 바꿀려면 int로
# print('변수 a의 값 : {}'.format(b))
# print('변수 a의 자료형(타입) : {}'.format(type(b)))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 입력 : 2
# 변수 a의 값 : 2
# 변수 a의 자료형(타입) : <class 'str'>
#
# 입력 : 2
# 변수 a의 값 : 2
# 변수 a의 자료형(타입) : <class 'int'>


#ex) 더하기 계산의 차이
# s1 = input('입력 s1 : ')               #12 입력
# s2 = input('입력 s2 : ')               #34  입력
#
# print('s1 + s2 = {}'.format(s1+s2))   #문자열 이라서 이어서 나온다 결과 (1234)
# print()
#
# i1 = int(input('입력 i1 : '))         #12 입력
# i2 = int(input('입력 i2 : '))         #34  입력
# print('i1 + i2 = {}'.format(i1+i2))   # 정수형으로 변환해서 더하기를 수행한다 결과 (46)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 입력 s1 : 3
# 입력 s2 : 5
# s1 + s2 = 35
#
# 입력 i1 : 12
# 입력 i2 : 34
# i1 + i2 = 46


#ex) 실수형으로 입력 받기
# num1 = float(input('실수로된 첫번째 숫자 : '))
# num2 = float(input('실수로된 두번째 숫자 : '))
#
# print('덧셈 결과 : {}'.format(num1+num2))
# print('뺄셈 결과 : {}'.format(num1-num2))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 실수로된 첫번째 숫자 : 12.3
# 실수로된 두번째 숫자 : 11.1
# 덧셈 결과 : 23.4
# 뺄셈 결과 : 1.200000000000001


#page 65
# price = 50000 # 물건값
# n = int(input('할부 개월 입력 >>>'))   #정수형으로 형변환
# print('매달 내는 돈은 {}원 입니다'.format(price / n))   # 실수형으로 출력

#산술연산자
#page 73
# a = 7
# b = 2
# print('{} + {} = {}'.format(a,b,a+b))   #더하기
# print('{} - {} = {}'.format(a,b,a-b))   #빼기
# print('{} * {} = {}'.format(a,b,a*b))    #곱하기
# print('{} ** {} = {}'.format(a,b,a**b))   #거듭제곱
# print('{} / {} = {}'.format(a,b,a/b))     #나눗셈  --> 결과가 실수형
# print('{} // {} = {}'.format(a,b,a//b))   # 몪
# print('{} % {} = {}'.format(a,b,a%b))     #나누기하고 남은 나머지
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 7 + 2 = 9
# 7 - 2 = 5
# 7 * 2 = 14
# 7 ** 2 = 49
# 7 / 2 = 3.5
# 7 // 2 = 3
# 7 % 2 = 1

#복합 대입 연산자
#ex) a가 10에서 시작해서 코드가 진행될수록 값이 변하도록 해보기
# a = 10
# print('a의 값 : {}'.format(a))
#
# a += 5    # a = a+5
# print('a의 값 : {}'.format(a))
#
# a -= 5   #a = a-5
# print('a의 값 : {}'.format(a))
#
# a *= 5  #a = a 곱하기 5
# print('a의 값 : {}'.format(a))
#
# a /= 5  # a =  a나누기 5
# print('a의 값 : {}'.format(a))  #결과는 실수형
#
# a %= 5  #a = a나누고 5 나머지
# print('a의 값 : {}'.format(a))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# a의 값 : 10
# a의 값 : 15
# a의 값 : 10
# a의 값 : 50
# a의 값 : 10.0
# a의 값 : 0.0


#page 76
# piggy_bank = 0
# money = 10000
# piggy_bank += money
#
# print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
# print('지금 저금통에는 {}원이 있습니다'.format(piggy_bank))
#
# snack = 2000
# piggy_bank -= snack
#
# print('저금통에서 스낵구입비 {}원을 뺐습니다.'.format(snack))
# print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 저금통에 용돈 10000원을 넣었습니다.
# 지금 저금통에는 10000원이 있습니다
# 저금통에서 스낵구입비 2000원을 뺐습니다.
# 지금 저금통에는 8000원이 있습니다.

#관계 연산자
# a = 15
# print('{} > 10: {}'.format(a,a > 10))
# print('{} < 10: {}'.format(a,a < 10))
# print('{} >= 10: {}'.format(a,a >= 10))
# print('{} <= 10: {}'.format(a,a <= 10))
# print('{} == 10: {}'.format(a,a == 10))
# print('{} != 10: {}'.format(a,a != 10))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 15 > 10: True
# 15 < 10: False
# 15 >= 10: True
# 15 <= 10: False
# 15 == 10: False
# 15 != 10: True


#page79
# a = 10
# b = 0
# print('{} > 0 and {} > 0 : {}'.format(a,b,a>0 and b>0))
# print('{} > 0 or {} > 0 : {}'.format(a,b,a>0 or b>0))
# print('not {} : {}'.format(a, not a))
# print('not {} : {}'.format(b, not b))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 10 > 0 and 0 > 0 : False
# 10 > 0 or 0 > 0 : True
# not 10 : False
# not 0 : True

#비트 연산자
#page 82
# a = 10    #00001010(2진수)
# b = 70    #01000110(2진수)
#
# print('a & b : {}'.format(a & b))   #00000010
# print('a | b : {}'.format(a | b))   #01001110
# print('a ^ b : {}'.format(a ^ b))   #01001100
# print('~a : {}'.format(~a))         #11110101
# print('a << 1 : {}'.format(a << 1)) #00010100   왼쪽으로 한칸 이동
# print('a >> 1 : {}'.format(a >> 1)) #00000101   오른쪽으로 한칸 이동
#
# 겱과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# a & b : 2
# a | b : 78
# a ^ b : 76
# ~a : -11
# a <<1 : 20
# a >>1 : 5

#page 83 시퀀스 연산자
# tree = '#'
# space = ' '
# print(space *4 + tree *1)
# print(space *3 + tree *3)
# print(space *2 + tree *5)
# print(space *1 + tree *7)
# print(space *0 + tree *9)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
#     #
#    ###
#   #####
#  #######
# #########

#멤버쉽 연산자 (in 연산자)
# print('안녕' in '안녕하세요')  #포함되어 있다
# print('메롱' in '안녕하세요')  #포함되어 있지 않다
#
# print('안녕' not in '안녕하세요')
# print('메롱' not in '안녕하세요')
#
# 결과값
# :\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# True
# False
# False
# True

#조건 연산자
# a = 10
# b = 20
# result = (a - b) if(a >= b) else(b - a)
# print('{}과 {}의 차이는 {} 입니다.'.format(a,b,result))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 10과 20의 차이는 10 입니다.

#page 90
#조건문
# if
# a = 99
# if a < 100:
#     print('100보다 작군요!') #참일때만 출력
#
# print()
# num = int(input('정수를 입력하세요 : ' ))
# if num > 0:
#     print('양수입니다!')
# if num == 0:
#     print('0입니다!')
# if num < 0:
#     print('음수입니다!')
#
# #결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\5day-240524.py
# 100보다 작군요!
#
# 정수를 입력하세요 : 0
# 0입니다!


#else은 조건문을 붙이지 않는다
#page 95
# age = int(input('몇 살입니까?>>>'))
# if age >= 20:
#     print('성인')
# else:
#     print('미성년자')

################################################

#input문제
# 1. 정수 변수 2개를 만들어 숫자를 입력 받는다. input함수
# 아래의 출력결과 처럼 나오게 해보자
# [화면 실행결과]
# 첫 번째 정수는? 13
# 두 번째 정수는? 5
# 나눗셈의 몪은 2 나머지는 3입니다

num1 = int(input('첫 번째 정수는 ? '))
num2 = int(input('두 번째 정수는 ? '))

print('나눗셈의 몪은 {} 나머지는 {}입니다'.format(num1 // num2,num1 % num2))

num1 = int(input('첫 번째 정수는 ? '))
num2 = int(input('두 번째 정수는 ? '))
print(f'나눗셈의 몪은 {num1 // num2} 나머지는 {num1 % num2}입니다')



# 스터디룸 input문제 올림






