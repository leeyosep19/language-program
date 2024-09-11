# #page305
# class NameError(Exception):
#
#     def __init__(self,message):
#         super().__init__(message)
#
# try:
#     name = input('이름을 입력하세요 >>>')
#     if len(name) < 2 or len(name) > 6:         #강제로 예외 발생
#         raise NameError('이름은 2~6자 사이로 입력해주세요.')
#
# except NameError as e:
#     print(e)
#
# else:
#     print('입력된 이름은 {}입니다.'.format(name))

# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\18day-240628.py
# 이름을 입력하세요 >>>이요셉
# 입력된 이름은 이요셉입니다.


# # 응용문제  page 304
#
# class Quiz:
#     answer = ['경기도','강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도','제주 특별시']
#
#     @classmethod
#     def challenge(cls):
#         if not cls.answer:            #값이 없다는 뜻 정답을 모두 맞추었다
#             print('모든 도를 맞췄습니다. 성공입니다!!')
#             return
#         do = input('정답은? >>>')       #우리가 한 대답
#         if do not in cls.answer:
#             raise  Exception('틀렸습니다!')
#
#         for i, answer_do in enumerate(cls.answer):
#             if do == answer_do:              #정답과 대답이 같다면
#                 print('정답입니다!')
#                 cls.answer.pop(i)     #i번째 값을 꺼내어 삭제
#
#         cls.challenge()
#
# try:
#     print('우리나라의 9개의 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
#     Quiz.challenge()
# except Exception as e:
#     print(e)


# #page 307
# import  random
#
# class UpDown:
#     def __init__(self):
#         self.answer = random.randint(1,100)    #정답(1~100)
#         self.count = 0      #시도횟수
#
#     def challenge(self):
#         self.count += 1
#         n = int(input('입력(1~100) >>> '))     #사용자로부터 숫자 입력 받음
#         if n < 1 or n > 100: #범위를 벗어나면 예외를 발생시킴
#             raise  Exception('1~100 사임나 입력하세요.')
#         return n     # 입력값 반환
#
#     def play(self):
#         while True:
#             try:
#                 n = self.challenge()    #숫자를 입력 받는다
#             except Exception as e:
#                 print(e)
#             else:
#                 if self.answer > n:
#                     print('UP')
#                 elif self.answer < n:
#                     print('Down')
#                 else:
#                     print('{}번만의 정답입니다!!'.format(self.count))
#                     break
#
# game = UpDown()
# game.play()
#
# 결과값
# D:\python-1\pythonProject\.venv\Scripts\python.exe D:\python-1\18day-240628.py
# 입력(1~100) >>> 50
# Down
# 입력(1~100) >>> 15
# UP
# 입력(1~100) >>> 20
# Down
# 입력(1~100) >>> 18
# 4번만의 정답입니다!!


# #page 308
# class BankError(Exception):
#     def __init__(self,message):
#         super().__init__(message)
#
# class BankAccount:
#     def __init__(self,acc_no,balance):
#         self.acc_no = acc_no     #계좌번호
#         self.balance =balance    #통장잔액
#
#     #입금 기능
#     def deposit(self,mooney):    #임금할 금액
#         if mooney <= 0:
#             raise BankError('{}원 입금 불가'.format(mooney))
#         self.balance += mooney   # 입금
#
#     #출금 기능
#     def withdraw(self,money):
#         if money <= 0:
#             raise BankError('{}원 출금 불가'.format(money))
#         if money > self.balance:
#             raise BankError('잔액 부족!')
#         self.balance -= money
#         return money
#
#     #이체 기능
#     def transfer(self,you_acc,money):
#         you_acc.deposit(self.withdraw(money))
#
#     #조회기능
#     def inquiry(self):
#         print('계좌 번호 : '.format(self.acc_no))
#         print('통장 잔액 : '.format(self.balance))
#
# #정상상황
# me = BankAccount('023-34-56789',50000)
# you = BankAccount('987-65-43210',50000)
#
# try:
#     me.transfer(you,5000)
# except BankError as e:
#     print(e)
# finally:
#     me.inquiry()
#     you.inquiry()


# 챗 gpt 수정
# class BankError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
# class BankAccount:
#     def __init__(self, acc_no, balance):
#         self.acc_no = acc_no     # 계좌번호
#         self.balance = balance   # 통장잔액
#
#     # 입금 기능
#     def deposit(self, money):    # 입금할 금액
#         if money <= 0:
#             raise BankError('{}원 입금 불가'.format(money))
#         self.balance += money   # 입금
#
#     # 출금 기능
#     def withdraw(self, money):
#         if money <= 0:
#             raise BankError('{}원 출금 불가'.format(money))
#         if money > self.balance:
#             raise BankError('잔액 부족!')
#         self.balance -= money
#         return money
#
#     # 이체 기능
#     def transfer(self, you_acc, money):
#         you_acc.deposit(self.withdraw(money))
#
#     # 조회 기능
#     def inquiry(self):
#         print('계좌 번호 : {}'.format(self.acc_no))
#         print('통장 잔액 : {}'.format(self.balance))
#
# # 정상 상황
# me = BankAccount('023-34-56789', 50000)
# you = BankAccount('987-65-43210', 50000)
#
# try:
#     me.transfer(you, 5000)
# except BankError as e:
#     print(e)
# finally:
#     me.inquiry()
#     you.inquiry()





















