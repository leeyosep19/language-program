# #csv 모듈로 csv파일 읽기
# #page 249
# import csv
#
# with open('./Section14/차량관리.csv','wt',newline='') as file:
#     csv_maker = csv.writer(file,delimiter=',')
#     csv_maker.writerow([1,'08러1234','2020-10-20,14:00'])
#     csv_maker.writerow([2,'25다1234','2020-10-20,14:10'])
#     csv_maker.writerow([3,'28하1234','2020-10-20,14:20'])
#
# print('차량관리.csv 파일이 생성되었습니다.')
import json

# #csv 모듈로 csv파일 읽기
# #page 249
# import csv
#
# with open('./Section14/차량관리.csv','rt') as file:
#     csv_reader = csv.reader(file,delimiter=',',quotechar='"')
#     for line in csv_reader:
#         print(line)
#
# print(csv_reader)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\14day-240617.py
# ['1', '08러1234', '2020-10-20,14:00']
# ['2', '25다1234', '2020-10-20,14:10']
# ['3', '28하1234', '2020-10-20,14:20']
# <_csv.reader object at 0x000002418A6757E0>


# #json 파일 입출력
# #json 파일 쓰기  (생성)
# #page 251
# import  json
#
# dict_list =[
#     {
#         'name' : 'james',
#         'age' : 20,
#         'spec' :[175.5,70.5]
#     },
#     {
#         'name' : 'alice',
#         'age' : 21,
#         'spec' : [168.5,60.5]
#
#     }
# ]
# json_string = json.dumps(dict_list)    #json으로 변환(인코딩)
#
# with open('./Section14/dictlist.json','wt') as file:
#     file.write(json_string)
#
# print('dictlist.json 파일이 생성되었습니다.')


# #json 파일읽기
# #page253
# import json
#
# with open('./Section14/dictlist.json','rt') as file:
#     josn_reader = file.read()     #파일 전체 읽기josn_reader에저장
#     dict_list = json.loads(josn_reader)  #파이썬으로 변환
#
# print(dict_list)
#
# for dic in dict_list:
#     print('이름 : {}'.format(dic['name']))
#     print('나이 : {}'.format(dic['age']))
#     print('키 : {}'.format(dic['spec'][0]))
#     print('몸무게 : {}'.format(dic['spec'][1]))
#     print('================================')
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\14day-240617.py
# [{'name': 'james', 'age': 20, 'spec': [175.5, 70.5]}, {'name': 'alice', 'age': 21, 'spec': [168.5, 60.5]}]
# 이름 : james
# 나이 : 20
# 키 : 175.5
# 몸무게 : 70.5
# ================================
# 이름 : alice
# 나이 : 21
# 키 : 168.5
# 몸무게 : 60.5
# ================================

# # 섹션 14 page254
# while True:
#     filename = input('복사할 파일명을 입력하세요 >>>>')
#     extname = filename[filename.rfind('.')+1:]   #확장자를 추출
#     if extname != 'txt':
#         print('복사할 수 없는 파일입니다!')
#     else:
#         break
#
# with open(filename,'rt') as source:  #원본
#     with open('복사본-'+filename,'wt') as copy:  #복사본
#         while True:
#             buffer = source.read(1)    #1바이트씩 읽어  buffer에 담는다
#             if not buffer:
#                 break
#             copy.write(buffer)
#
# print('복사본-' + filename + '파일이 생성되었습니다!')


# #ex) 응용2번
# import csv
# with open('./Section14/cctv.csv', 'rt') as csvfile:
#     buffer = csv.reader(csvfile,delimiter=',',quotechar='"')
#     totalcctv = 0 # cctv 개수
#     for i, line in enumerate(buffer):
#         if i != 0:              #제목줄은 제외
#             totalcctv += int(line[6])
#
# print('대구광역시 달서구에 설치된 cctv는 총 {}대 입니다'.format(totalcctv))
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\14day-240617.py
# 대구광역시 달서구에 설치된 cctv는 총 2583대 입니다


# #응용3 page 255
#
# with open('./Section14/cctv.json','rt',encoding='utf-8') as jsonfile:
#     buffer = jsonfile.read()
#     cctv_list = json.loads(buffer)       #파이썬으로 변환
#     cctv_purpose = set()       #결과를 담을 빈 세트를 생성 (복사x)
#     for place in cctv_list:
#         cctv_purpose.add(place['설치목적구분'])     #세트에 추가
#
# print(cctv_purpose)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\14day-240617.py
# {'주정차단속', '방범(공원)', '방범', '방범(경찰 설치)', '방범(어린이보호구역)', '방범(치수과)', '방범(그린파킹)'}
#


# #page 260
# #클래스와 객체
# # 객체 지향 프로그래밍
# 문자를 작게 나누어 객체를 만들고 객체를 조합해서 문제를 해결하는 방식
#
# 복잡한 문제를 처리하는데 유용하며, 기능을 개선하고 발전시킬 때도 해당 클래스만 수정하면 되므로, 유지보수에 효율적
#
# 클래스 : 똑같은 무언가를 계속해서 만들어 낼수 있는 설계도 과자를, 붕어빵틀에 비유
# 객체 : 붕어빵트에서 만들어 낸 붕어빵에 비유 각각의 객체마다 고유의 특성을 가진다
#       파이썬에서는 문자, 정수, 실수 , 함수 등 모두 객체다
# 인스턴스 : 특정 객체가 어떤 클래스의 객체인지 관계위주로 설명할때 사용
#         클래스와 연관지어 객체를 말할때 인스턴스라고한다
# 메서드 : 클래스 안에서 구현된 함수
#
# <형식>
# class 클래스이름 : #파이썬에서는 클래스이름을 주로 대문자로 사용
#     def 메서드 이름 (self,매개변수):  #인스턴스 메서드
#     #self  -> 메서드를 호출한 객체가 자동으로 전달되는 매개변수
#     self.속성 = 값    #인스턴스 변수
#
#
# 인스턴스이름 = 클래스 이름()  #인스턴스(객체) 생성
# 인스턴스 이름.메서드 이름()   #메서드 (함수)  호출


# #ex)
# class Person:  #클래스이름
#     def who_am_i(self,name,age,tel,address):     #인스턴스 메서드
#         self.name = name    #인스턴스 변수
#         self.age = age
#         self.tel = tel
#         self.address =address
#
# boy1 = Person()     #boy1 인스턴스 (객체)생성   -> 붕어빵을 구웠다
# print(boy1)
# boy1.who_am_i('john',15,'123-1234','toronto')
# print(boy1.name)
# print(boy1.age)
# print(boy1.tel)
# print(boy1.address)
#
#
# boy2 = Person()     #boy2 인스턴스
# print(boy2)
# boy2.who_am_i('ryan', 20, '111-1111', 'Daegu')
# print(boy2.name)
# print(boy2.age)
# print(boy2.tel)
# print(boy2.address)
#
#
# boy3 = Person()
# boy3.who_am_i('hlro', 28, '121-1131', 'seoul')
# print(boy3)
# print(boy3.name)
# print(boy3.age)
# print(boy3.tel)
# print(boy3.address)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\14day-240617.py
# <__main__.Person object at 0x000002D6EDEEBFB0>
# john
# 15
# 123-1234
# toronto
# <__main__.Person object at 0x000002D6EE1C2210>
# ryan
# 20
# 111-1111
# Daegu
# <__main__.Person object at 0x000002D6EE1C2240>
# hlro
# 28
# 121-1131
# seoul





















