# # 파일에서 문서 열기
#     <형식>
#     파일객체명 = open('파일 이름', 'r')
#     변수명 = 파일 객체명. read()
#     파일객체명.close()
#
#     print(변수명)     #화면으로 보고싶을때 사용
#

# #ex)
# file = open('Hello.txt', 'r')    #파일열기(읽기모드로)
# temp = file.read()   #읽은내용을 temp 변수에 담는다
# file.close()   #파일닫기
#
# print(temp)

# #파일에서 여러 줄을 리스트로 각 읽기
#
#     <형식>
#     파일객체명 = open('파일 이름', 'r')
#     리스트명 = 파일 객체명. readlines()
#     파일객체명.close()
#
#     print(리스트명) #화면에서 보고싶을때 사용

# #ex)
# file = open('Hello.txt','r')
# lines = file.readlines()    #파일에서 읽은 내용을 리스트 형식으로 저장
# file.close()
#
# print(lines)
# print('========================')
# print(lines[3])
# print('===================')
# for i in lines:
#     print(i,end='')  #print함수에서 있는 엔터기능을 없엔다
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\13day-240614.py
# ['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n', '10번째 줄입니다.\n', '11번째 줄입니다~~~~~~~~~!!\n', '12번째 줄입니다~~~~~~~~~!!\n', '13번째 줄입니다~~~~~~~~~!!\n', '14번째 줄입니다~~~~~~~~~!!\n', '15번째 줄입니다~~~~~~~~~!!\n', '16번째 줄입니다~~~~~~~~~!!\n', '17번째 줄입니다~~~~~~~~~!!\n', '18번째 줄입니다~~~~~~~~~!!\n', '19번째 줄입니다~~~~~~~~~!!\n', '20번째 줄입니다~~~~~~~~~!!\n', '11번째 줄입니다~~~~~~~~~!!\n', '12번째 줄입니다~~~~~~~~~!!\n', '13번째 줄입니다~~~~~~~~~!!\n', '14번째 줄입니다~~~~~~~~~!!\n', '15번째 줄입니다~~~~~~~~~!!\n', '16번째 줄입니다~~~~~~~~~!!\n', '17번째 줄입니다~~~~~~~~~!!\n', '18번째 줄입니다~~~~~~~~~!!\n', '19번째 줄입니다~~~~~~~~~!!\n', '20번째 줄입니다~~~~~~~~~!!\n', '11번째 줄입니다~~~~~~~~~!!\n', '12번째 줄입니다~~~~~~~~~!!\n', '13번째 줄입니다~~~~~~~~~!!\n', '14번째 줄입니다~~~~~~~~~!!\n', '15번째 줄입니다~~~~~~~~~!!\n', '16번째 줄입니다~~~~~~~~~!!\n', '17번째 줄입니다~~~~~~~~~!!\n', '18번째 줄입니다~~~~~~~~~!!\n', '19번째 줄입니다~~~~~~~~~!!\n', '20번째 줄입니다~~~~~~~~~!!\n']
# ========================
# 4번째 줄입니다.
#
# ===================
# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# 10번째 줄입니다.
# 11번째 줄입니다~~~~~~~~~!!
# 12번째 줄입니다~~~~~~~~~!!
# 13번째 줄입니다~~~~~~~~~!!
# 14번째 줄입니다~~~~~~~~~!!
# 15번째 줄입니다~~~~~~~~~!!
# 16번째 줄입니다~~~~~~~~~!!
# 17번째 줄입니다~~~~~~~~~!!
# 18번째 줄입니다~~~~~~~~~!!
# 19번째 줄입니다~~~~~~~~~!!
# 20번째 줄입니다~~~~~~~~~!!
# 11번째 줄입니다~~~~~~~~~!!
# 12번째 줄입니다~~~~~~~~~!!
# 13번째 줄입니다~~~~~~~~~!!
# 14번째 줄입니다~~~~~~~~~!!
# 15번째 줄입니다~~~~~~~~~!!
# 16번째 줄입니다~~~~~~~~~!!
# 17번째 줄입니다~~~~~~~~~!!
# 18번째 줄입니다~~~~~~~~~!!
# 19번째 줄입니다~~~~~~~~~!!
# 20번째 줄입니다~~~~~~~~~!!
# 11번째 줄입니다~~~~~~~~~!!
# 12번째 줄입니다~~~~~~~~~!!
# 13번째 줄입니다~~~~~~~~~!!
# 14번째 줄입니다~~~~~~~~~!!
# 15번째 줄입니다~~~~~~~~~!!
# 16번째 줄입니다~~~~~~~~~!!
# 17번째 줄입니다~~~~~~~~~!!
# 18번째 줄입니다~~~~~~~~~!!
# 19번째 줄입니다~~~~~~~~~!!
# 20번째 줄입니다~~~~~~~~~!!


# #page 232
# import  time
#
# file = open(time.strftime('%y-%m-%d')+'.txt','at')  #날짜에 형식지정(파일명)
# while True:
#     schedule = input('오늘의 스케줄을 입력하세요 >>>')
#     if not schedule:    #스케줄이 없다면(아무것도 입력안했다면)
#         break           #반복문을 종료한다
#     file.write(schedule+'\n')   # 스케줄 뒤에 엔터 삽입
# file.close()        #파일닫기


# # page 237
# file = open('엄마돼지아기돼지.txt','rt')    #파일열기 (읽기모드로)
#
# line_list = file.readlines()   #전체 글을 저장할 리스트
# count = 0        # 꿀의 개수
# for line in line_list:        # 전체글 중 하나의 라인을 문자열 line변수에 저장
#     for ch in line:           # line에 담긴 모든 문자들을 하나씩 ch변수에 저장
#         if ch == '꿀':         # ch변수에 담긴 값과 꿀을 비교
#             count += 1         # 같다면 1씩 증가(개수변수 증가)
#
# file.close()            #파일 닫기
# print('꿀은 전체{}번 나타납니다.'.format(count))

# # with 문과 함께 파일입출력 하기
#     파일을 열면 항상 close해주어야 하는 불편함을 덜어주는 기능
#
#     <형식>
#     with open('파일 이름','파일 열기모드') as 파일개체명:
#     수행할 코드

# #ex)
# li = ['Hello~\n','world!\n','merng~~\n','python!!\n']
#
# with open('file.txt','w') as f:
#     f.writelines(li)
#     f.write('ㅋㅋㅋㅋ\n')
#     f.write('파일썬 잼있어!!\n')
#
# with open('file.txt','r') as f:
#     temp = f.read()   #파일의 내용을 모두 읽어 temp변수에 담는다
#
# print(temp)
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\13day-240614.py
# Hello~
# world!
# merng~~
# python!!
# ㅋㅋㅋㅋ
# 파일썬 잼있어!!

#page 242
# #파일 복사
#
# buffer_size = 1024    #한번에 읽어 들어가는 데이터의 크기 (1024byte==1kb)
# with open('./Section14/code.mp4','rb') as source:
#     with open('./Section14/code2.mp4','wb') as copy:
#         while True:
#             buffer = source.read(buffer_size) #buffer_size 만큼 읽어 변수에 담는다.
#             if not buffer:
#                 break
#             copy.write(buffer)
# print('code2.mp4 파일에 복사 되었습니니다!')

# #csv 파일 입출력
# #csv 파일읽기
# #page 246
# student_list=[]
# with open('./Section14/학생명단.csv','rt') as file:
#     file.readline()   #제목 줄(지워진다)
#     while True:
#         line = file.readline()   #한줄씩 읽어 line리스트에 담는다
#         if not line:
#             break
#         student = line.split(',')  #,로 구분된 것을 분리해서 student에 저장
#         student_list.append(student)  #결과리스트에 분리한 student 저장
# print(student_list)


# #page 247
# member_list = []
# with open('/Section14/회원명단.csv','rt') as file:
#     file.readline()
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         member =line.split(',')    # ['강나라',필라테스,25일]
#         member[0] =member[0].strip('"')    # 양쪽 큰 따옴표 제거 후 다시 저장
#         member_list.append(member)
#
# print(member_list)

########################################################
#파일 입출력 문제
#새로운 텍스트 파일 loop.txt를 생성하되, 파일 열기 모드를 추가모드로 한다
#1부터 100까지 한 칸씩 띄우고 모두 한줄에 저장한다
#[loop.txt 열어본 결과]
#숫자 1 숫자2 숫자3...... 숫자 99 숫자 100

# file = open('loop.txt','a')
# for i in range(1,101):
#     data = f'숫자 {i}'
#     file.write(data)
# file.close()

# # 두번째 방법)
# with open('loop.txt', 'a') as f:
#     for i in range(1, 101):
#         data = f'숫자 {i} '
#         f.write(data)




























