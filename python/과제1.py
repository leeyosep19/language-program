#################################################

# 문제1) 날짜와 시간이 출력되게 만들기

# [화면실행결과]

# 2020/10/31 11:43:59

# 힌트 > print함수의 sep, end사용

# print(2020,10,31, sep='/', end='  ')
# print(11,43,59,sep=':')
#
# print()

#########################################################

# 문제2) 화면실행결과를 참고하여 문자열 인덱싱으로 한 글자씩 출력해보자.

# string = 'PYTHON'

# [화면실행결과]

# P

# Y

# H

# N

# string = 'PYTHON'
# print(string[0])
# print(string[1])
# print(string[3])
# print(string[-1])
#
# print()
# 문제3) 문자열 슬라이싱으로 화면실행결과와 같도록 출력해보자.

# mystr = 'GOOD NIGHT'

# [화면실행결과]

# OO

# GH

#  NIGHT

# mystr ='GOOD NIGHT'
# print(mystr[1:3])
# print(mystr[7:9])
# print(mystr[4:])
#
# print()
#
# # 문제4) 과일이름을 요소로 하는 값이 3개인 리스트 a를 생성해라(과일이름 3개)
# a = ['apple','banana', 'grape']
# print(a)
#
# # 문제5) 음식이름을 요소로 하는 값이 3개인 리스트 b를 생성해라(음식이름 3개)
# b = ['ramea', 'bulgogi', 'gukbap']
# print(b)
#
# # 문제 6) 위 두개의 리스트를 하나로 합친 리스트c를 생성해라
# c = a+b
# print(c)
#
# # 문제7) 리스트 a에서 마지막 과일을 다른 과일로 대체해라
#
# a[2] = 'plum'
# print(a)

# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\과제1.py
# 2020/10/31  11:43:59
#
# P
# Y
# H
# N
#
# OO
# GH
#  NIGHT
#
# ['apple', 'banana', 'grape']
# ['ramea', 'bulgogi', 'gukbap']
# ['apple', 'banana', 'grape', 'ramea', 'bulgogi', 'gukbap']
# ['apple', 'banana', 'plum']



# num1 = int(input('삼성 전자의 주가는 ?'))
# num2 = int(input('LG전자의 주가는 ?'))
# print(f'삼성 주가는 {num1}이고 LG전자의 주가는{num2}이다. 주가차이는{num1+num2}이다')


#문제1) 변수 height를 정수형(int)으로 만들어 값을 입력하시오.(input)

# 변수 weight를 실수형(float)으로 만들어 값을 입력하시오.

# height와 weight를 더한 값을 출력하시오.

# [화면실행결과]

# 키가 얼마인가요? 165

# 몸무게가 얼마인가요? 50.0

# 키 + 몸무게 : 215.0

# height = int(input('키가 얼마 인가요 ?'))
# weight = float(input('몸무게가 얼마 인가요 ?'))
#
# print('키{}와 몸무게{} 의 더한 값은{} 입니다'.format(height,weight,height+weight))
#
# height = int(input('키가 얼마 인가요 ?'))
# weight = float(input('몸무게가 얼마 인가요 ?'))
# print(f'키{height}와 몸무게{weight} 의 더한 값은{height+weight} 입니다')


# 문제2) 이름과 국어, 수학, 영어 점수(정수형)를 입력받는다.

# 총합과 평균을 구하시오. 평균은 소수 첫째자리까지 표현한다

# [화면실행결과]

# 이름을 입력하세요 : 파이썬

# 국어 성적을 입력하세요 : 95

# 수학 성적을 입력하세요 : 98

# 영어 성적을 입력하세요 : 79

# 파이썬님의 성적은 총합 272점, 평균 90.7점입니다. (평균은 소수첫째자리까지)

# name = input('이름을 입력 하세요 : ')
# kor = int(input('국어 성적을 입력 하세요 : '))
# math = int(input('수학 성적을 입력 하세요 : '))
# eng = int(input('영어 성적을 입력 하세요 : '))
# total = kor+math+eng
# avg = total / 3
#
#
# print('{} 의 성적은 총합 {}점, 평균 {:.1f}점 입니다.'.format(name,total,avg))







# 문제3) 반지름을 입력받아 원의 둘레와 넓이를 구하자.

# 원의 둘레 공식(2 * 3.14 * 반지름), 원의 넓이 공식(3.14 * 반지름 * 반지름)

# 이 때 결과값이 소수 둘째자리까지 나오도록 반올림한다.

# [화면실행결과]

# 원의 반지름을 입력하세요(cm) : 3

# 원의 둘레는 18.84 cm이고 원의 넓이는 28.26 cm입니다.

# one = int(input('원의 반지름을 입력 하세요(cm) : '))
#
# circumference = 2 * 3.14 * one
# wide = 3.14 * one * one
#
# print('원의 둘레는 {:.2f} cm이고 원의 넓이는 {:.2f} cm 입니다.'.format(circumference,wide))





 #문제4) 2개의 변수를 만들어 실수형으로 입력받는다.

# 피타고라스의 정리를 바탕으로 빗변의 값을 소수 첫째자리까지로 나오도록 구하자.

# 피타고라스 정리 : 직각삼각형의 빗변의 제곱은 두 직각 변의 제곱합과 같다.

# 참고공식 : 빗변 제곱값 = 첫 번째 직각변의 길이 제곱값 + 두 번째 직각 변의 길이 제곱값

# 빗변 = 빗변 제곱값 ** 0.5

# (제곱을 원래 값으로 하기 위해 1/2(0.5)를 거듭제곱한다. => 제곱근 구하는 것임)

# [화면실행결과]

# 첫 번째 직각변의 길이(cm) : 15.3

# 두 번째 직각변의 길이(cm) : 12.1

# 빗변의 길이는 19.5cm입니다

# Pythagoras1 = float(input('첫 번째 직각변의 길이(cm) : '))
# Pythagoras2 = float(input('두 번째 직각변의 길이(cm) : '))
#
# a =Pythagoras1**2 + Pythagoras2**2
# b = a**0.5
#
# print('빗변의 길이는 {:.1f}cm입니다.'.format(b))


#과제
# 한점을 구성하는(x.y) 좌표를 입력받고 , 이점이 (50, 40),(50.80),(100,40),(100,80)을
# 꽂지점으로 갖는 사각형 안에 있는지 판별하는 프로그램을 작성 하시오
# (선 위에 점이 있는 것은 포함 하지 않는 것으로 한다.)
# [화면 실행 결과]
# x좌료를 입력하시오 : 60
# y좌료를 입력하시오 : 60
# 사각형 안에 없습니다.


x = int(input('x좌표를 입력 하세요 : '))
y = int(input('y좌표를 입력 하세요 : '))
if 50 < x <100 and 40 < y < 80 :
    print('사각형 안에 있습니다!')
else:
    print("사각형 안에 없습니다!")







