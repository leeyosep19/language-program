#
#리스트 연산자  ----> +,* 더하기 곱하기
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(list_a)
# print(list_b)
#
# list_c = list_a + list_b   #더하기는 하나의 리스트로 합쳐진다(이어진다)
# print(list_c)
#
# list_d = list_a * 3    #곱하기는 3번 반복한다
# print(list_d)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\3day-240520.py
# [1, 2, 3]
# [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

#page41
# append 중요 단어  (요소를 추가할때)
# 리스트의 요소 값 추가 : append, insert
# list1 =  [1, 2, 3]
# print('list1 :',list1)
#
# list1.append(4)  #맨뒤에 정수 4를 삽입
# print('list1 :',list1)
#
# list1.append(100)
# print('list1 :',list1)
#
# list1.insert(1,50)  #1번 인뎃스 자리에 50을 삽입했다
# print('list1 :',list1)
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\3day-240520.py
# list1 : [1, 2, 3]
# list1 : [1, 2, 3, 4]
# list1 : [1, 2, 3, 4, 100]
# list1 : [1, 50, 2, 3, 4, 100]

# 리스트의 요소 값 제거 (인덱스 번호로 삭제 ): pop, del
# list2 = [0, 1, 2, 3, 4, 5]
# print('list2 :', list2)
#
# del list2[1]   # 1번인덱스 자료값을 삭제
# print('list2 :', list2)
#
# list2.pop(2)   # 2번인덱스 자료값을 삭제
# print('list2 :', list2)
#
# list2.pop()   # 맨 마지막 자료를 삭제
# print('list2 :', list2)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\3day-240520.py
# list2 : [0, 1, 2, 3, 4, 5]
# list2 : [0, 2, 3, 4, 5]
# list2 : [0, 2, 4, 5]
# list2 : [0, 2, 4]

#page 42
# 튜플 - 읽기 전용 리스트
# t1 = (1, 2, 3)
# print('튜플 t1 :', t1)
#
# t2 = 1, 2, 3  # 괄호를 생략할 수 있다
# print('튜플 t2 :', t2)
#
# t3 = tuple([100, 3.14, 'hello'])
# print('튜플 t3 :', t3)
# print(type(t3))
#
# t4 = (100)   # 튜풀이 아님! 변수로 인식!
# print('변수 t4 :', t4)
# print(type(t4))
#
# t5 = (100,)  # t5 = 100, 튜플 로 한자리 만들고싶을때 (,) 을 붙여쓴다
# print('튜플 t5:', t5)
#
# 결과값
# 튜플 t1 : (1, 2, 3)
# 튜플 t2 : (1, 2, 3)
# 튜플 t3 : (100, 3.14, 'hello')
# <class 'tuple'>
# 변수 t4 : 100
# <class 'int'>
# 튜플 t5: (100,)

#리스트와 튜플의 차이점
# #리스트는 [], 튜플은 ()
# 리스트는 그 값의 추가, 수정, 삭제 가능
# 튜플은 그값을 바꿀수 없다
#
# #리스트와 튜플의 공통점
# 연산 가능(덧셈, 곱셈)
# 안덱싱, 슬라이싱 가능(시퀀스 자료형 - 순서가 있는 자료형)

#page43
# #셋트(집합)
# s1 = {1, 2, 3}
# print('셋트 s1', s1)
# print(type(s1))
#
# #값 1개 추가하기 - add
#
# s1.add(4)  #무조건 맨뒤에 추가 (순서가 없기 때문에)
# print('셋트 s1', s1)
#
# #값을 여러개 추가하기 - update
#
# s1.update([5, 6, 7])
# print('셋트 s1', s1)
#
# #특정 값을 제거하기 - remove
# s1.remove(3)   #값 3을 지워라
# print('셋트 s1', s1)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\3day-240520.py
# 셋트 s1 {1, 2, 3}
# <class 'set'>
# 셋트 s1 {1, 2, 3, 4}
# 셋트 s1 {1, 2, 3, 4, 5, 6, 7}
# 셋트 s1 {1, 2, 4, 5, 6, 7}

#page44
# #딕션너리
# dic ={ }  #빈 딕셔너리
# print(type(dic))
#
# s2 = set()
# print(s2)
# print(type(s2))
#
# dic = {'name': '홍길동', 'dirthday':'0720'}
# print('딕셔너리 dic :', dic)
#
# #특정값을 출력할때
# print(dic['name'])   #값(홍길동) 이 출력
# a = dic['dirthday']
# print(a)
#
# #딕셔너리 값을 수정 할때
# dic['name'] = '푸바오'
# print('딕셔너리 dic :', dic)
#
# #딕셔너리 쌍을 추가 할때
# dic['address'] = '용인'    #해당하는 키가 없으면 추가됨
# print('딕셔너리 dic :', dic)
#
# #딕셔너리 쌍을 삭제할때 -del
# del dic['address']  #address에 해당하는 키와 값을 삭제
# print('딕셔너리 dic :', dic)
#
# #key 리스트 만들기 - keys
# print(dic.keys())  #키만 따로 모아서 리스트를 만든다
#
# li = list(dic.keys())
# print(li)
# print(type(li))
#
# #값( value) 라스트 만들기 values
# print(dic.values())
#
# #items 함수를 이용해서 쌍을 얻기
# print(dic.items())   #쌍이 튜플 형식으로 묶인다
# li = list(dic.items())
# print(li)
#
# #키와  값을 모두 지우기
# dic.clear()
# print('딕셔너리 dic :', dic)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\pythonProject\.venv\3day-240520.py
# <class 'dict'>
# set()
# <class 'set'>
# 딕셔너리 dic : {'name': '홍길동', 'dirthday': '0720'}
# 홍길동
# 0720
# 딕셔너리 dic : {'name': '푸바오', 'dirthday': '0720'}
# 딕셔너리 dic : {'name': '푸바오', 'dirthday': '0720', 'address': '용인'}
# 딕셔너리 dic : {'name': '푸바오', 'dirthday': '0720'}
# dict_keys(['name', 'dirthday'])
# ['name', 'dirthday']
# <class 'list'>
# dict_values(['푸바오', '0720'])
# dict_items([('name', '푸바오'), ('dirthday', '0720')])
# [('name', '푸바오'), ('dirthday', '0720')]
# 딕셔너리 dic : {}

