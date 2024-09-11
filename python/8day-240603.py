#비시퀀스와 for문

#for와 세트
# for item in {'가위', '바위', '보'}:
#     print(item)  # 순서는 램덤으로 나온다
#
# print('=========================')
#
# #for 와 딕셔너리
# person = {
#     'name' : '에밀리',
#     'age' : 20
# }
#
# for item1 in person:
#     print(item1)  #딕셔너리 를 돌리면 키가 출력
#
# print('==============================')
#
# for item2 in person:
#     print(person[item2])   #값(value)이 출력
#
# print('==============================')
#
# for item3 in person:
#     print(person.get(item3))    #값이 출력
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 가위
# 보
# 바위
# =========================
# name
# age
# ==============================
# 에밀리
# 20
# ==============================
# 에밀리
# 20


#page 128
# eng_dict = {
#     'sun' : '태양',
#     'moon' : '달',
#     'star' : '별',
#     'space' : '우주'
# }
# for word in eng_dict:
#     print('{}의 뜻 : {}'.format(word,eng_dict.get(word)))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# sun의 뜻 : 태양
# moon의 뜻 : 달
# star의 뜻 : 별
# space의 뜻 : 우주

#page 134 기타제어문

#break
#ex) 0 부터 99까지 출력
# i = 0
# while True:          #무한반복
#     print(i, end=' ')  # i 출력
#     i += 1 # i = i+1
#     if i == 100:   # i가 100이 되면
#         break      # 제어 흐름을 빠져 나온다

# while True:
#     city = input('대한민국의 수도는 어디인가요? >>>>>')
#     if city == '서울' or city == 'seoul' or city == 'SEOUL':
#         print('정답입니다 !!')
#         break  #반복문을 종료
#     else:
#         print('오답입니다 !! 다시시도하세요.')
#
# 결과값

#page 137
# hobbies = []
# while True:
#     hobby = input('취미를 입력하세요 (종료는 그냥 엔터)>>>>')
#     if hobby == '':
#         print('입력된 취미가 모두 저장되었습니다. ')
#         break
#     else:
#         hobbies.append(hobby)   #hobby변수에 담긴 값을 리스트에 추가
# print(hobbies)  # 반복문이 모두 끝난 후에 실행
#
# 결과값

#ex) 반복문을 이용한 커피자판기 프로그램
# coffee = 3
# while True:
#     money = int(input('돈을 넣어 주세요 : '))
#     if money == 300:                         #커피값을 300 원이라고 가정했을경우
#         print('커피가 나왔습니다!')
#         coffee -= 1                            #
#         print(f'남은 커피의 양은 {coffee}개 입니다.')
#     elif money > 300:
#         print(f'거스름돈 {money - 300}원을 주고 커피도 줍니다 !')
#         coffee -= 1
#         print(f'남은 커피의 양은 {coffee}개 입니다.')
#     else:
#         print(f'{money}원을 다시 돌려주고 커피는 주지 않습니다!')
#         print(f'남은 커피의 양은 {coffee}개 입니다.')
#
#     if coffee == 0:
#         print('커피가 다 떨어졌습니다. 판매를 중지합니다!')
#         break
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 돈을 넣어 주세요 : 300
# 커피가 나왔습니다!
# 남은 커피의 양은 2개 입니다.
# 돈을 넣어 주세요 : 500
# 거스름돈 200원을 주고 커피도 줍니다 !
# 남은 커피의 양은 1개 입니다.
# 돈을 넣어 주세요 : 200
# 200원을 다시 돌려주고 커피는 주지 않습니다!
# 남은 커피의 양은 1개 입니다.
# 돈을 넣어 주세요 : 1000
# 거스름돈 700원을 주고 커피도 줍니다 !
# 남은 커피의 양은 0개 입니다.
# 커피가 다 떨어졌습니다. 판매를 중지합니다!


#page 138 continue문

#continue
#ex)0~10 사이의 수 중에서 홀수만 출력
# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0:                 # 짝수라면
#         continue
#     print(a)                       # 홀수만 출력
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 1
# 3
# 5
# 7
# 9

#page 139
# fruits = ['사과', '감귤']
# count = 3                              #입력해야 할 남은 과일 개수
#
# while count > 0:
#     fruit = input('어떤 과일을 저장할까요? >>>')
#     if fruit in fruits:                  #fruit변수에 있는 값이 fruits리스트에 포함되었나?
#         print('동일한 과일이 있습니다')
#         continue                         #포함되었다면 다시 반복문의 처음(조건)으로 돌아간다
#     fruits.append(fruit)                 # 포함되지 않은
#     count -= 1                #횟수를 1번 줄여준다
#     print('입력이 {}번 남았습니다.'.format(count))
#
# print('5개 과일은 {}입니다.'.format(fruits))
#
# 결과값


# page 140
# count = 0
# tolal = 0
# while count < 5:
#     n = int(input('{}번째 정수를 입력하세요>>>'.format(count +1)))
#     if n <= 0:                                             # 0과 음수는 제외하기 위해 넣은 코드
#         print('0 이하의 정수는 처리 할수 없습니다.')
#         continue
#     tolal += n
#     count += 1
# print('입력된 5개 양수의 총 합은 {}입니다'.format(tolal))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 1번째 정수를 입력하세요>>>5
# 2번째 정수를 입력하세요>>>3
# 3번째 정수를 입력하세요>>>-2
# 0 이하의 정수는 처리 할수 없습니다.
# 3번째 정수를 입력하세요>>>2
# 4번째 정수를 입력하세요>>>6
# 5번째 정수를 입력하세요>>>-7
# 0 이하의 정수는 처리 할수 없습니다.
# 5번째 정수를 입력하세요>>>1
# 입력된 5개 양수의 총 합은 17입니다

# 참고) 리스트 내포 (리스트 컴프리헨션)
#append 사용
# li = [1, 2, 3]
# num1 = []
# for n in li:
#     num1.append(n * 2)
# print('append 사용 : {}'.format(num1))
#
# print()
# # 리스트 내포사용
# num2 = [n*2 for n in li]
# print('리스트 내포사용 : {}'.format(num2))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# append 사용 : [2, 4, 6]
#
# 리스트 내포사용 : [2, 4, 6]

#내장함수
# 문자열 내장함수
#chr() : 유니코드를 문자로 변환
# print(chr(48))
# print(chr(49))
# print(chr(65))
# print(chr(66))
# print(chr(97))
# print(chr(98))
# print(chr(44032))
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 0
# 1
# A
# B
# a
# b
# 가

#ord() : 문자를 유니코드로 변환
# print(ord('A'))
# print(ord('a'))
# print(ord('가'))
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 65
# 97
# 44032


#eval() : 문자열로 된 값을 계산  (보안이 취약)
# print('100 + 200')
# print(eval('100+200'))
# print(eval('min(1,2,3)'))   #min() : 최솟값
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 100 + 200
# 300
# 1

#page 149
# expr = input('계산식을 입력하세요 >>>')
# result = eval(expr)
# print(result)
# print(type(result))
# print(expr+ '=' + str(result))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\8day-240603.py
# 계산식을 입력하세요 >>>1+2+3
# 6
# <class 'int'>
# 1+2+3=6



#########################################
#ex) for 문제
# 1. 시작 값과 끝값, 중심값까지 사용자에게 정수를 입력받아
# 시작값과 끝 값까지의 합계구하기 (for, range()이용)
#[화면실행결과]
#시작값을 입력하시오 : 3
# 끝값을 입력하시오 : 300
# 중심값을 입력하시오 : 3
# 3에서 300까지의 3씩 증가시킨 값의 합계 : 15150

total = 0
n1 = int(input('시작값을 입력하시오 : ' ))
n2 = int(input('끝값을 입력하시오 : ' ))
n3 = int(input('중심값을 입력하시오 : ' ))
for n in range(n1,n2+1,n3):
    total += n
print(f'{n1}에서 {n2}까지 {n3}씩 증가시킨 값의 합계 : {total}')






















