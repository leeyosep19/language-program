# #page 287
# class Person:
#     population = 0   #인구수 (클래스 변수)
#
#     def __init__(self,name):    # 생성자
#         self.name = name       #인스턴스 변수
#         Person.population += 1
#         print('{} is born.'.format(self.name))
#
#     def __del__(self):     #소멸자
#         Person.population  -= 1  # 인구수 1감소
#         print ('{} is dead.'.format(self.name))
#
#     @classmethod
#     def get_population(cls):        #클래스  메서드 정의
#         return cls.population       # 인구수 반환
#
# man = Person('james')   #인스턴스 생성
# woman = Person('emily')
# print('전체인구수 : {}명'.format(Person.get_population()))
# del man #   인스턴스 삭제
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# james is born.
# emily is born.
# 전체인구수 : 2명
# james is dead.
# emily is dead.


#page 292
#예외처리
#예외 종류
#SyntaxError: 잘못된 문법
#NameError : 참조 변수 없음 (변수이름이 틀렸다 )
#ZeroDivisionError : 0나누기 에러
#IndexError  : 인덱스 범위 에러
#KeyError : 잘못된 키
#ValueError : 참조 값이 없을때
#TypeError : 자료형에 맞지 않는 연산을 수행할 경우


# #모든 예외를 처리 하는 방식 (try ~ except)
# try:  #예외가 발생할 가능성이 있는 코드
#     num = int(input('정수를 입력하세요 : '))
#     print('원의 반지름 : {}'.format(num))
#     print('원의 둘레 : {}'.format(num * 3.14*2))
#     print('원의 넓이 : {}'.format(num*num*3.14))
# except:
#     print('정수를 입력하지 않았습니다.')


# #page 297
# try:
#     height = input('키를 입력하세요 >>>')   #문자열
#     height = round(height)               #반올림
#     print('입려가신 키는 {}cm로 처리 됩니다.'.format(height))
# except:
#     print('예외가 발생했습니다.')


# # 특정 예외만 처리하는 방식
# #page 298
# try:
#     a = int(input('제수를 입력하세요 : '))
#     b = int(input('피제수를 입력하세요 : '))
#     print('{} / {} = {}'.format(a,b,a/ b))
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
# except Exception:
#     print('알수 없는 예외가 발생했습니다.')

# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# 제수를 입력하세요 : 3
# 피제수를 입력하세요 : 1
# 3 / 1 = 3.0

# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# 제수를 입력하세요 : 3.1
# 정수만 입력할 수 있습니다.


# #예외 메세지 처리하기
# #page 299
# a = [10, 20, 30, 40, 50]
#
# try:
#     print(a[10])
# except IndexError as e:
#     print(e)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# list index out of range


# #else문과 finally문
#
#     else : 예외 발생하지 않고, 정상적으로 처리될때 실행되는 구문
#     finally : 예외처리 구문에서 가장 마지막에 사용할수 있는 구문
#             예외 발생 여부와 관계없이 무조건 실행해야 할 경우에 사용
#     try : 는 단독으로는 사용할수 없으며, 반듯이 except 또는 finally와
#             한께 사용해야함
#     else 는 반듯이 except 뒤에 사용해야함

# #ex)
# try:
#      num = int(input('정수를 입력하세요 : '))
# except:
#     print('정수를 입력하지 않았습니다!')
# else:      #예외가 발생하지 않았을때
#     print('원의 반지름 : {}'.format(num))
#     print('원의 둘레 : {}'.format(num * 3.14*2))
#     print('원의 넓이 : {}'.format(num*num*3.14))
# finally:    #무조건 실행
#     print('일단 프로그램이 끝났습니다.')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# 정수를 입력하세요 : 2
# 원의 반지름 : 2
# 원의 둘레 : 12.56
# 원의 넓이 : 12.56
# 일단 프로그램이 끝났습니다.

# # page 301
# try:
#     filename = input('열고자 하는 파일명을 입력하세요>>>')
#     file = open(filename, 'rt')
# except FileNotFoundError:
#     print('{} 파일이 존재하지 않습니다.'.format(filename))
# else:
#     buffer = file.read()
#     print(buffer,end='')
#     print()
#     file.close()
# finally:
#     print('프로그램을 종료합니다!')


# # 강제로 예외를 발생시키기(raise)
#     강제로 예외를 발생시킴
#     1. 프로그램 개발 단계에서 아직 구현되지 않은 일부러 예외를
#     발생시켜 잊어버리지 않도록 하는 경우에 활용
#     2. 파이썬이 예외로 인식하지 못하지만 실제로 예외인 경우(ex 나이)

# #ex)
# num = int(input('정수를 입력하세요 : '))
# if num > 0:
#     raise  '아직 구현되지 않는 부분입니다.'
# else:
#     print('0또는 음수입니다.')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# 정수를 입력하세요 : 2
# Traceback (most recent call last):
#   File "D:\python-1\17day - 240626.py", line 154, in <module>
#     raise  '아직 구현되지 않는 부분입니다.'
# TypeError: exceptions must derive from BaseException


# #page 303
# try:
#     score = int(input('점수를 입력하세요 >>>'))
#     if score < 0 or score > 100:      #점수가 범위를 벗어났다면
#         raise  Exception('점수는 0~100 사이입니다.')   #강제로 예외 발생
# except Exception as e:
#     print(e)   #예외 메세지 출력
# else:    #정상적인 경우
#     if score >= 80:
#         print('{}점은 합격입니다.'.format(score))
#     else:
#         print('{}점은 불합격 입니다.'.format(score))


# #pass
#     예외 발새아면 바로 처리해야 하지만 크게 중요한 부분이 아닐 경우
#     프로그램의 경우 종료를 막는 목적으로 pass 를 사용
#
#     <형식>
#     try:
#     예외가 발생할 가능성이 있는 코드
#     except:
#         pass


# #ex)
# li = ['52','123', '29', '파이썬', '111']
# li_num = []    #숫자만 담을 빈 리스트를 생성
#
# for i in li:  #li에 있는 값들을 하나씩 꺼내어 반복
#     try:
#         result = int(i)  #정수형인 숫자로 변환
#         li_num.append(result)  #예외없이 통과한 값만 li_num에 추가
#     except:
#         pass    #예외 발생하면 그냥 넘어감
#
# print(li_num)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe "D:\python-1\17day - 240626.py"
# [52, 123, 29, 111]


#################################################

# #예외 처리 문제
# #나이를 입력 받아 정상적인 정수면 나이를 출력하고, 그 외의 경우라면
# #예외처리를 하는 코드를 만들어보자 . try, except, else, finally 사용
# #[화면실행결과- 정상적일때]
# #나이를 입력하세요 : 20
# #입력하신 나이는 20살 입니다.
# #프로그램을 종료합니다
#
#
# #[화면실행결과- 비정상적일때]
# #나이를 입력하세요 : 스물
# #입력이 잘못 되었습니다
# #프로그램을 종료합니다
#
# try:
#     age = int(input('나이를 입력하세요 : '))
# except ValueError:
#     print('입력이 잘못 되었습니다.')
# else:
#     print('입력하신 나이는 {}살 입니다.'.format(age))
# finally:
#     print('프로그램을 종료합니다!')


##################################################
#과제
#page 289

class Car:                                         #슈퍼클래스(부모클래스)
    max_oil = 50                                   #클래스 변수

    def __init__(self,oil):
        self.oil = oil                             #인스턴스 변수

    def add_oil(self,oil):                         #인스턴스 메서드
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:                 #최대 주유량보다 크다면
            self.oil = Car.max_oil                 #현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print('현재 주유상태 : {}'.format(self.oil))

class Hybrid(Car):                                #서브 클래스(자식 클래스)
    max_battery = 30

    def __init__(self,oil,battery):
        super().__init__(oil)
        self.battery = battery

    def add_charge(self,battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print('현재 충전 상태 : {}'.format(self.battery))

car = Hybrid(0,0)
car.add_oil(100)
car.add_charge(50)
car.hybrid_info()




























