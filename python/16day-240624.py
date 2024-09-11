# #page 276
# class USB:                                      #클래스 정의
#     def __init__(self,capacity):                #생성자
#         self.capacity = capacity                # 인스턴스 변수
#
#     def info(self):                             #인스턴스 메서드 정의
#         print('{}GB USB'.format(self.capacity))
#
# usb = USB(64)                                   #인스턴스(객체) 생성 -> 붕어빵을 구웠다
# usb.info()                                      #인스턴스 메서드 호출
#
# usb2 = USB(128)                                 #인스턴스(객체) 생성 -> 붕어빵을 구웠다
# usb2.info()                                     #인스턴스 메서드 호출
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 64GB USB
# 128GB USB


# #page 277
# class Service:
#     def __init__(self, service):   # 생성자
#         self.service = service     #인스턴스 변수
#         print('{} Service가 시작되었습니다.'.format(self.service))
#
#     def __del__(self):             #소멸자
#         print('{} Service가 종료되었습니다.'.format(self.service))
#
# s = Service('길 안내')     #인스턴스(객체) 생성 -> 붕어빵을 구웠다
# del s     #인스턴스(객체) 삭제  -> 붕어빵을 먹었다(사라짐)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 길 안내 Service가 시작되었습니다.
# 길 안내 Service가 종료되었습니다.


# #page 278
# #클래스 변수
#     클래스 안에서 공간이 할당된 변수
#     여러 인스턴스(객체)가 클래스 변수 공간을 함께 사용

# #ex)
# class Car:    #클래스 정의
#     count = 0      #클래스 변수  정의 (0으로 초깃값을 줬다)
#
#     def __init__(self,name, speed):     #생성자
#         self.name = name       #인스턴스 변수
#         self.speed = speed
#         Car.count += 1         # 클래스 변수를 1 증가 시킨다
#
#     def info(self):
#         print(f'{self.name}의 현재 속도 : {self.speed}km')
#         print(f'생성된 자동차 수 : {Car.count}대')
#         print('=======================================')
#
# car1 = Car('붕붕카',0)   #인스턴스(객체) 생성  ->   붕어빵을 구웠다
# car1.info()                        #인스턴스 메서드 호출
#
# car2 = Car('빵빵카', 30)
# car2.info()
#
# car3 = Car('제네시스', 200)
# car3.info()
#
# car4 = Car('아우디',210)
# car4.info()
#
# car5 = Car('람보르기니',300)
# car5.info()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 붕붕카의 현재 속도 : 0km
# 생성된 자동차 수 : 1대
# =======================================
# 빵빵카의 현재 속도 : 30km
# 생성된 자동차 수 : 2대
# =======================================
# 제네시스의 현재 속도 : 200km
# 생성된 자동차 수 : 3대
# =======================================
# 아우디의 현재 속도 : 210km
# 생성된 자동차 수 : 4대
# =======================================
# 람보르기니의 현재 속도 : 300km
# 생성된 자동차 수 : 5대
# =======================================


#클래스 메소드 - 클래스 변수를 사용하는 메서드, 객체 없이 호출가능
# #page 280
# class Korean:             #클래스 정의
#     country = '한국'       #클래스 변수('한국' 으로 초기화)
#
#     @classmethod
#     def trip(cls,country):      #클레스 메서드 정의
#         if cls.country == country:
#             print('국내여행 입니다.')
#
#         else:
#             print('해외여행 입니다.')
#
# Korean.trip('한국')
# Korean.trip('미국')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 국내여행 입니다.
# 해외여행 입니다.


# # page 282
# class Bag:
#     count = 0
#
#     def __init__(self):
#         Bag.count += 1
#
#     @classmethod
#     def sell(cls):
#         cls.count -= 1
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print('현재 가방 : {}개'.format(Bag.remain_bag()))
# bag1 = Bag()
# bag2 = Bag()
# bag3 = Bag()
# print('현재 가방 : {}개'.format(Bag.remain_bag()))
# bag1.sell()
# bag2.sell()
# print('현재 가방 : {}개'.format(Bag.remain_bag()))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 현재 가방 : 0개
# 현재 가방 : 3개
# 현재 가방 : 1개


# # 클래스 상속
# #page 284
# class Person:   #슈퍼클래스(부모 클래스)
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self,food):       #인스턴스 메서드 정의
#         print(f'{self.name}가 {food}를 먹습니다.')
#
# class Student(Person):     #서브 클래스(자식 클래스)
#     def __init__(self,name,school):
#         super().__init__(name)     #슈퍼(부모) 클래스의 생성자를 호출
#         self.school = school
#
#     def study(self):           #인스턴스 메서드 정의
#         print(f'{self.name}는 {self.school}에서 공부를 합니다!!')
#
# potter = Student('해리포터','호그와트')     #인스턴스(객체) 생성
# potter.eat('감자')   #상속받은 메서드 호출
# potter.study()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 해리포터가 감자를 먹습니다.
# 해리포터는 호그와트에서 공부를 합니다!!


# #page 286
# class Coffee:   #슈퍼클래스
#     def __init__(self, been):
#         self.been = been
#
#     def coffee_info(self):  #인스턴스 메서드
#         print('원두 : {}'.format(self.been))
#
# class Espresso(Coffee):    #서브 클래스
#     def __init__(self,been, water):
#         super().__init__(been)   #부모의 생성자를 호출
#         self.water = water
#
#     def espresso_info(self):           #인스턴스 메서드 정의
#         super().coffee_info()      #부모클래스 호출
#         print('물 : {}ml'.format(self.water))
#         print('===========================')
#
# coffee = Espresso('콜롬비아',30)
# coffee.espresso_info()
#
# coffee2 = Espresso('맥심모카 골드',50)
# coffee2.espresso_info()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\16day-240624.py
# 원두 : 콜롬비아
# 물 : 30ml
# ===========================
# 원두 : 맥심모카 골드
# 물 : 50ml
# ===========================







































