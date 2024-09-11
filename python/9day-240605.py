#숫자 내장 함수
# #abs() : 절댓값
# print(abs(10))
# print(abs(-10))
# print('======================')
#
# # divmod() : 몫과 나머지
# print(divmod(10,3))            #결과는 튜플 형식
# d , m = divmod(10, 3)
# print(d)
# print(m)
#
# print('=======================')
#
# # max() : 최댓값
# print(max(1, 2))
# li = [10, 8, 4, 2]
# print(max(li))
#
# print('============================')
# #min() : 최솟값
# print(min(1, 10))
# print(min(li))
#
# print('===========================')
# #pow() : 거듭제곱  (**연산자)
# print(pow(10, 2))  #10을 두번 곱한다
# print(pow(10,3))
# print(pow(10,-2))
#
# print('===========================')
#
# # round() : 반올림
# print(round(1.5))    #일의 자리까지
# print(round(1.4))
# print(round(1.55, 1))    # 소수 첫째자리까지 반올림
#
# print('===========================')
#
# # sum() : 합계
# li = [1, 2, 3, 4, 5]
# print(sum(li))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# 10
# 10
# ======================
# (3, 1)
# 3
# 1
# =======================
# 2
# 10
# ============================
# 1
# 2
# ===========================
# 100
# 1000
# 0.01
# ===========================
# 2
# 1
# 1.6
# ===========================
# 15
# import distutils.log

# #page 153
# money = 10000
# price = 3000    # 빵한개의 가격
# result = divmod(money,price)
# print(result)
# print('빵을 {}개 사고 {}원이 남았습니다.'.format(result[0],result[1]))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# (3, 1000)
# 빵을 3개 사고 1000원이 남았습니다.

#page 154
#시퀀스 내장함수
#enumerate()   *****중요 함수
#
# <형식>
# for 인덱스번호, 값 in enumerate(리스트명):
#     수행할 코드

# #ex)
# li = [10, 20, 30]
# for i in li:
#     print(i)    # 리스트의 값(요소)만 출력
# print()
#
# for itme in enumerate(li):
#     print(itme)               #튜플로 묶어서 나온다
#
# for index, value in enumerate(li):
#     print(f'{index}번째 : {value}')
#
# print()
# for i, v in enumerate(li, start=1): # 인덱스 시작 번호를 1로 정함
#     print(f'{i}번째 : {v}')
#
# print('===================')
#
# # len() : 길이 (항목수)
# li = ['a', 'b', 'c', 'd']
# print(len(li))
#
# ch = 'Hello'
# print(len(ch))
#
# d = {'a' : 'apple', 'b' : 'banana'}
# print(len(d))
#
# print(len(range(10)))      #0~9 : 10 개
# print(len(range(1, 10)))   #1~19 : 9 개
#
# # 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# 10
# 20
# 30
#
# (0, 10)
# (1, 20)
# (2, 30)
# 0번째 : 10
# 1번째 : 20
# 2번째 : 30
#
# 1번째 : 10
# 2번째 : 20
# 3번째 : 30
# ===================
# 4
# 5
# 2
# 10
# 9

# #ex) 총첨과 평균구하기
# score = [70, 60, 55, 75, 95]    #학생 점수 리스트
# total = 0                       # 총점0으로 초기화
#
# for i, v in enumerate(score, start=1):
#     print(f'{i}번째의 학생 점수 : {v}')
#     total += v
#
# print(f'총점 : {total}')
# avg = total /len(score)     #리스트 개수로 나누어 평균을 구한다
# print(f'평균 : {avg}')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# 1번째의 학생 점수 : 70
# 2번째의 학생 점수 : 60
# 3번째의 학생 점수 : 55
# 4번째의 학생 점수 : 75
# 5번째의 학생 점수 : 95
# 총점 : 355
# 평균 : 71.0


# #sorted() : 정렬
# my_list = [6, 3, 1, 2, 5, 4]
# sorted_list = sorted(my_list)    #정렬된 새로운 리스트 생성, 원본은 그대로
# reverse_list = sorted(my_list, reverse=True)
# print(f'원본 : {my_list}')
# print(f'정렬후 (오름차순) : {sorted_list}')
# print(f'정렬후 (내림차순) : {reverse_list}')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# 원본 : [6, 3, 1, 2, 5, 4]
# 정렬후 (오름차순) : [1, 2, 3, 4, 5, 6]
# 정렬후 (내림차순) : [6, 5, 4, 3, 2, 1]

# #zip() : 튜플로 묶기
# names = ['james', 'emily', 'amande']
# scores = [60, 70, 80]
# for student in zip(names, scores):
#     print(student)
#
# for name, score in zip(names,scores):
#     print(f'{name}의 점수는 {score}점입니다')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# ('james', 60)
# ('emily', 70)
# ('amande', 80)
# james의 점수는 60점입니다
# emily의 점수는 70점입니다
# amande의 점수는 80점입니다

#page 159
# months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for month, day in enumerate(months):
#     print('{}월 = {}일'.format(month+1, day))특정 문자열의개수

# 메소드

# # 문자열 메소드
# # .count() : 특정 문자열의개수
# s = '내가 그린 기린 그림은 목긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다'
# print(s.count('기린'))
#
# a = 'best of best'
# print(a.count('best'))
# print(a.count('best',5))    #5번 인덱스 부터 시작하겠다
# print(a.count('best',-7))
#
# print('===================================')
#
# # .find(),.index() : 특정 문자열의 위치 반환
# b = 'apple'
# print(b.find('p'))    #해당 인덱스 번호
# print(b.rfind('p'))   #끝에서 부터 나오는 인덱스번호
# print(b.find('z'))     #없는 경우 -1
#
# print(a.find('best'))
# print(a.find('best',5))   # 지정한 인덱스부터 검색
#
# print('================================')
#
# print(b.index('p'))
# print(b.index('z'))   # 없는 경우에는 에러를 발생시킨다

# #대소문자 변환 메소드  : .upper(). lower, capitalize()
# s = 'BEST of best'
# print(s.upper())       #대문자  변화
# print(s.lower())       #소문자  변환
# print(s.capitalize())   #첫글자만 대문자
#
# print('=================')
#
# #.join()  : 합치기 *****중요
# a = '-'.join('python')
# print(a)
#
# b= '+'.join(['a', 'b', 'c'])
# print(b)
#
# c = ' '.join(['x', 'y', 'z'])
# print(c)
#
# d = ''.join({'a':'apple','b':'banana'})
# print(d)         #키만 사용
#
# print("==========================")
#
# #.split() : 나누기(리스트 형식으로 결과 나옴)
# a = 'Life is too short'
# print(a.split())    #공백을 기준으로 분리
#
# b = '010-1234-5678'
# print(b.split('-'))    #-을 기준으로 분리
#
# c = '제임스,25,남,서울'
# print(c.split(','))   #,을 기준으로 분리
#
# print('=====================')
# # .replace()  : 바꾸기
# print(a.replace('Life', 'Leg'))
#
# print(b.replace('-',''))
# print('===========================')
# #.strip()  : 불필요한 문자열 바꾸기
# a ='     apple'
# print(a)
# print(len(a))
#
# b = a.lstrip()   #왼쪽 공백을 제거 ,rstrip() : 오른쪽 공백제거
# print(b)
# print(len(b))
#
# c = '<head<'
# d = c.strip('<')   # 양쪽 < 문자 제거
# print(d)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# BEST OF BEST
# best of best
# Best of best
# =================
# p-y-t-h-o-n
# a+b+c
# x y z
# ab
# ==========================
# ['Life', 'is', 'too', 'short']
# ['010', '1234', '5678']
# ['제임스', '25', '남', '서울']
# =====================
# Leg is too short
# 01012345678
# ===========================
#      apple
# 10
# apple
# 5
# head

# # 리스트 메소드
# #.extend() : 확장
# my_list = ['apple', 'banana']
# my_list.extend(['cherry','mange'])
# print(my_list)   #원본 수정됨
#
# print('================')
#
# #.remove() : 특정값을 제거
# my_list.remove('mange')
# print(my_list)
#
# my_list.remove('banana')
# print(my_list)
#
# print('================')
#
# #.clear() : 모든값 제거
# my_list.clear()
# print(my_list)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\9day-240605.py
# ['apple', 'banana', 'cherry', 'mange']
# ================
# ['apple', 'banana', 'cherry']
# ['apple', 'cherry']
# ================
# []












