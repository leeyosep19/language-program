# #page 267
# class Computer:    #클래스 정의
#     def set_spec(self, cpu, ram, vgs, ssd):     #인스턴스 메서드 정의
#         self.cpu = cpu   #인스턴스 변수
#         self.ram = ram
#         self.vgs = vgs
#         self.ssd = ssd
#
#     def hardware_info(self):    #인스턴스 메서드 정의
#         print('CPU = {}'.format(self.cpu))
#         print('RAM = {}'.format(self.ram))
#         print('VGS = {}'.format(self.vgs))
#         print('SSD = {}'.format(self.ssd))
#         print('==============================')
#
# desktop = Computer()      #인스턴스(객체) 생성  --> 붕어빵을 구웠다
# desktop.set_spec('i7','16GB', 'GTX1060', '512GB')   #인스턴스 메서드 호출
# desktop.hardware_info()    #인스터스 메서드를 호출
# print(desktop)
# print('===========================================')
#
# notebook = Computer()     #인스턴스(객체) 생성 -->또다른 붕어빵을 구웠다
# notebook.set_spec('i5', '8GB', 'MX300', '256GB')    #인스턴스 메서드를 호출
# notebook.hardware_info()    #인스턴스 메서드를 호출
# print(notebook)
# print('==========================================')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# CPU = i7
# RAM = 16GB
# VGS = GTX1060
# SSD = 512GB
# ==============================
# <__main__.Computer object at 0x00000266B8B61E80>
# ===========================================
# CPU = i5
# RAM = 8GB
# VGS = MX300
# SSD = 256GB
# ==============================
# <__main__.Computer object at 0x00000266B8B61EB0>
# ==========================================


# #page 269
# class Calculator:   #클래스 정의
#     def input_expr(self):
#         expr = input('수식을 입력하세요>>>')    #지역변수
#         self.expr = expr      #인스턴스 변수로 다시 저장
#
#     def calculator(self):
#         return  eval(self.expr)   #eval() : 문자열로된 수식을 계산해주는 함수
#
# calc = Calculator() #인스턴스 생성    --> 붕어빵을 구웠다
# calc.input_expr()   #인스턴스 메서드를 호출
# print('수식 결과는 {}입니다'.format(calc.calculator()))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# 수식을 입력하세요>>>1+2+3+4
# 수식 결과는 10입니다


# #섹션 15 page270  응용1
# class Book:    #클래스 정의
#     def set_info(self,title, author):   #인스턴스 메서드 정의
#         self.title = title
#         self.author = author
#
#     def print_info(self):
#         print('책 제목 : {}'.format(self.title))
#         print('책의 저자 : {}'.format(self.author))
#         print('============================')
#
# #인스턴스 객체를 생성하고 --> 책 생성
# book1 = Book()
# book2 = Book()
# book3 = Book()
# book4 = Book()
# print(book1,book2,book3,book4,sep='\n')
#
# #책 제목과 저자 정보를 저장
# book1.set_info('파이썬','민태경')
# book2.set_info('어린왕자', '생텍쥐페리')
# book3.set_info('오늘부터 개발자','김병옥')
# book4.set_info('트렌드코리아2024','김난도')
#
#
# book_list = [book1,book2,book3,book4]  #객체를 4개 담은 리스트 생성
# for book in book_list:
#     book.print_info()   #출력 메서드를 호출
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# <__main__.Book object at 0x00000217494E1C10>
# <__main__.Book object at 0x00000217494E1C40>
# <__main__.Book object at 0x00000217494E1D00>
# <__main__.Book object at 0x00000217494E1D30>
# 책 제목 : 파이썬
# 책의 저자 : 민태경
# ============================
# 책 제목 : 어린왕자
# 책의 저자 : 생텍쥐페리
# ============================
# 책 제목 : 오늘부터 개발자
# 책의 저자 : 김병옥
# ============================
# 책 제목 : 트렌드코리아2024
# 책의 저자 : 김난도
# ============================


# #응용2
# class Watch:    #클래스정의
#     def set_time(self):     #인스턴스 메서드 정의
#         now = input('시간을 입력하세요 >>>')   #ex)12:00:00
#         hms = now.split(':')   #:(콜론)으로 분리 ex)['12', '00', '00']
#         self.hour = int(hms[0])     #인스턴스 변수
#         self.minute = int(hms[1])
#         self.second = int(hms[2])
#
#     def add_hour(self,hour):        #인스턴스 메서드 정의
#         if hour <= 0:
#             return
#         self.hour += hour
#         self.hour %= 24
#
#     def add_minute(self,minute):
#         if minute <= 0:
#             return
#         self.minute += minute
#         self.add_hour(self.minute // 60)
#         self.minute %= 60
#
#     def add_second(self,second):
#         if second <= 0:
#             return
#         self.second += second
#         self.add_minute(self.second // 60)
#         self.second %= 60
#
#     def see(self):    #인스턴스 메서드 정의 (출력 메서드)
#         print('계산된 시간은 {}시 {}분 {}초 입니다'.format(self.hour,self.minute,self.second))
#
# watch = Watch()   #인스턴스 생성
# watch.set_time()   #인스턴스 메서드 호출
# watch.add_hour(int(input('계산할 시간을 입력하세요>>>')))
# watch.add_minute(int(input('계산할 분을 입력하세요>>>')))
# watch.add_second(int(input('계산할 초를 입력하세요>>>')))
# watch.see()    #출력(인스턴스) 메서드 호출
#
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# 시간을 입력하세요 >>>12:00:00
# 계산할 시간을 입력하세요>>>3
# 계산할 분을 입력하세요>>>90
# 계산할 초를 입력하세요>>>3690
# 계산된 시간은 17시 31분 30초 입니다


############################################################
# 클래스 문제
# 친구의 이름과 전화번호 정보를 담을수 있는 클래스 Friend 를 만들어보자
#set_info(), show_info() 인스턴스 메서드를 포함한다
#인스턴스 변수 : 이름, 전화번호(변수명은 마음대로 하기!)
#[화면실행결과]
#이름 : 라이언
#전화번호 : 010-1234-5678
#-----------------------
#이름 : 춘식이
#전하번호 : 010-1111-2222
#-----------------------

# class Friend:
#     def set_info(self,name,tel):
#         self.name = name
#         self.tel = tel
#
#     def show_info(self):
#         print('이름 : {}'.format(self.name))
#         print('전화번호 : {}'.format(self.tel))
#         print('---------------------------')
#
# name1 = Friend()
# name2 = Friend()
#
# name1.set_info('라이언','010-1234-5678')
# name2.set_info('춘식이','010-1111-2222')
#
# name1.show_info()
# name2.show_info()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# 이름 : 라이언
# 전화번호 : 010-1234-5678
# ---------------------------
# 이름 : 춘식이
# 전화번호 : 010-1111-2222
# ---------------------------


# #섹션 16 : 클래스와 객체2
# # 생성자 (constructor)
#     객체에서 초깃값을 설정해야할 필요가 있을때 사용, ex)set_info()
#     객체가 생성될때 자동으로 호출해주는 메서드
#     __init__ 사용
#
#     스페셜 메서드 (매직 메서드) : 파이썬에서 목적에 따라 자동으로 호출되는 메서드
#                               앞뒤로 __가 붙은 메서드
#
#     <형식>
#     class 클래스이름:
#         def __init__(self): #생성자 (인스턴스 메서드)
#             self.속성 = 값   #인스턴스 변수
#

# #ex) 생서자를 사용하지 않은 경우
# class Candy:
#     def set_info(self,shape,color):
#         self.shape = shape
#         self.color = color
#
#     def print_info(self):
#         print('<생성자를 사용하지 않은 경우!>>')
#         print('self.shape :',self.shape)
#         print('self.color :',self.color)
#         print('=====================')
#
# satang = Candy()
# satang.set_info('circle','red')
# satang.print_info()
#
# # ex)생성자를 사용한 예제
# class Candy2:
#     def __init__(self,shape,color):
#         self.shape = shape
#         self.color = color
#
#     def print_info(self):
#         print('<생성자를 사용하지 않은 경우!>>')
#         print('self.shape :',self.shape)
#         print('self.color :',self.color)
#         print('=====================')
#
# satang2 =Candy2('circle','red')   #개체 생성과 동시에 생성자를 호출
# satang2.print_info()
#
# satang3 = Candy2('circle','pink')
# satang3.print_info()
#
# satang4 = Candy2('circle','green')
# satang4.print_info()
#
# satang5 = Candy('circle', 'black')    #에러!!  (Candy클래스에는 생성자가 없다!)
# satang5.print_info()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\15day-240619.py
# Traceback (most recent call last):
#   File "D:\python-1\15day-240619.py", line 257, in <module>
#     satang5 = Candy('circle', 'black')
#               ^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Candy() takes no arguments
# <생성자를 사용하지 않은 경우!>>
# self.shape : circle
# self.color : red
# =====================
# <생성자를 사용하지 않은 경우!>>
# self.shape : circle
# self.color : red
# =====================
# <생성자를 사용하지 않은 경우!>>
# self.shape : circle
# self.color : pink
# =====================
# <생성자를 사용하지 않은 경우!>>
# self.shape : circle
# self.color : green
# =====================


###########################################################
# 과제  파일 입출력
# practice.txt 를 만들어 '제 1의 아해가 무섭다고 그리오' 부터
# '제 5의 아헤가 무섭다고 그리오.'까지 순서대로 한줄에 하나씩
# 파일안에 내용을 넣고, 그파일을 다시 열어 파이썬 화면에 출력하세오
# (파일 쓰기, 파일 읽기 모두 해야함)
# [화면실행결과]
# 제1의 아헤가 무섭다고 그리오.
# 제2의 아헤가 무섭다고 그리오.
# 제3의 아헤가 무섭다고 그리오.
# 제4의 아헤가 무섭다고 그리오.
# 제5의 아헤가 무섭다고 그리오.

# file = open('practice.txt','w')
# for i in range(1,6):
#     date = f'제{i}의 아헤가 무섭다고 그리오.\n'
#     file.write(date)
# file.close()
#
#
# file = open('practice.txt','r')
# lines = file.readlines()
#
# for i in lines:
#     print(i,end='')
# file.close()


#2)
with open('practice2.txt','w') as f:
    for i in range(1, 6):
        date = '제 {}의 아헤가 무섭다고 그리오.\n'.format(i)
        f.write(date)

with open('practice2.txt','r') as f:
    lines = f.readlines()

    for i in lines:
        print(i,end='')










