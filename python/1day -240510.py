# #, ''' ''' 주석
# '''
# 작성자 : 이요셉
# 작성 일자 : 24-05-10
# '''
# # 출력 해주는 함수
# print('안녕 하세요!!!')  #메모 (주석)
# 한꺼번에 주석 처리하는 방법 드래그 해서 ctrl + /
# 주석 해제 할때  드래그 해서 ctrl + /

# 실행방법
# 마우스 오른쪽 버튼 run
# 또는 단축키 ctrl +shift + f10

# 저장 방법
# run 하면 자동 저장
# ctrl + s

# print 함수 (표준 출력)
# print('안녕~~~~') # 문자는 앞으로 작은 따움표 또는 큰 따움표를 넣는다
#
# print(1)   #숫자는 따움표를 붙이지 않는다
# print(2)
# print(3)
# print()   #빈 줄 : 파일썬 에서는 print함수는 기본적으로 엔터를 포함한다
#
# print(1, 2, 3)   # 쉼표 : 구분자, 구분자는 실행 시 스페이스(공백)로 바뀐다
# print(4, '안녕', 5, '메롱')
# print('     ', '빈칸')    #공백도 글자다!
# print()
#
# print(1, 2, 3, sep=',')    #sep =   출력 사이 사이에 콤마(,) 가 나오도록
# print(4, 5, 6, sep=':')     #  출력 사이 사이에 콜론(:) 이 나오도록
# print(7, 8, 9, sep='')      # 붙여서 표시
#
# print(1, end='')    #엔터 기능을 없앤다
# print(2, end=':')    #엔터 대신에 콜론(:)이 나온다
# print(3, end='      ')  #엔터 대신에 공백 글자(스페이스)가 나온다
# print(4)
# print(5)

# 결과값
# 안녕~~~~
# 1
# 2
# 3
#
# 1 2 3
# 4 안녕 5 메롱
#       빈칸
#
# 1,2,3
# 4:5:6
# 789
# 12:3      4
# 5

#변수
# 상자 또는 그릇 (메모리 저장소)에 내용물 을 담았다 라는  의미
# <형식>
#변수 이름  = 값
#= 대입연산자(
# 예약어 (키워드) : 특별한 의미가 부여된 단어 파일썬 에서 미리 특정 의미로 사용
#



# ex) 예약어 확인하는 방법
# import keyword
#
# print(keyword.kwlist)
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\1day -240510.py"
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Alice

#page 32
# name ='Alice'    #변수이름(왼쪽)에는 따움표를 넣지 않는다
# age = 25
# address = '''우편 변호 12345 서울시
# 영등포구 여의도동 서울빌딩 501호'''
# boyfriend = None  #None  : 없다
# height = 168.5
#
# print(name)
# print(age)
# print(address)
# print(boyfriend)
# print(height)


##################################
#  문제 b라는 변수를 생성 하고 음수3을 저장한 후 출력 해보자
b = -3
print(b)

# 문제  자신의 이름(영어)를 변수명 으로 한 후 자신의 나이를 할당 하여 보자.
lee_yo_sep = '31'


print(lee_yo_sep)


