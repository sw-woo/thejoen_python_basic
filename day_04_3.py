# 절차 지향 함수로 명함출력하는 함수 만들기
# 이름, 이메일, 주소를 입력 받아서 명함을 출력하는 기능 


# def print_business_card(name, email, addr):
#     print('*' * 40)
#     print("Name: %s" %name)
#     print(f"Email: {email}")
#     print("Address: {}".format(addr))
#     print('*' * 40)


# name = input("이름을 입력해 주세요!")
# email = input("이메일을 입력해 주세요!")
# addr = input("주소를 입력해 주세요!")

# print(print_business_card(name, email, addr))


# class BusinessCard:
    

#     def __init__(self):
#         self.name = input("이름을 입력해 주세요!")
#         self.email = input("이메일을 입력해 주세요!")
#         self.addr = input("주소을 입력해 주세요!")

#     # def set_info(self):
#     #     self.name = input("이름을 입력해 주세요!")
#     #     self.email = input("이메일을 입력해 주세요!")
#     #     self.addr = input("주소를 입력해 주세요!")

#     def print_info(self):
#         print('*' * 40)
#         print("Name", self.name)
#         print("Email", self.email)
#         print("Address", self.addr)
#         print('*' * 40)


# cards = []
# number = int(input("몇개의 명함을 출력하시겠습니까?"))

# for _ in range(number):
#     card = BusinessCard()
#     # card.set_info()
#     cards.append(card)

# for card in cards:
#     card.print_info()





# class MyClass:
#     def __init__(self):
#         print("객체가 생성되었습니다.")

# inst1 = MyClass()

# inst1.__init__()


# 파이썬 변수의 스코프(범위 or 생명주기)


# result = 0

# def add (num):
#     global result 
#     # result = 0
#     result += num
#     return result

# print(add(3))
# print(add(4))

# a = 20 # 전역 변수 특징 
# #1. 스크립트안에서 어디서든 불러서 사용 가능
# #2. 함수안에서 전역변수를 사용할 수 있지만, 값을 변경하려면 global 키워드를 사용해야 함

# def foo():
#     global a # 전역 변수 x를 사용하겠다.
#     x=30 # x는 foo의 지역변수 
#     a = x
#     print(a)

# foo()
# print(a)

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b
    
#     def sub(self):
#         return self.a - self.b
    
#     def mul(self):
#         return self.a * self.b
    
#     def div(self):
#         return self.a / self.b
    
#     def mod(self):
#         return self.a % self.b
    
#     def pow(self):
#         return self.a ** self.b



# calc = Calculator(10, 5)
# calc2 = Calculator(20, 3)

# choice = 1

# while choice !=0:
#     print("0. 종료")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 곱하기")
#     print("4. 나누기")
#     print("5. 나머지")
#     print("6. 제곱")
#     choice = int(input("원하는 연산을 선택하세요: "))
#     if choice == 0:
#         break
#     elif choice == 1:
#         print("더하기 결과: ", calc.add())
#     elif choice == 2:
#         print("빼기 결과: ", calc.sub())
#     elif choice == 3:
#         print("곱하기 결과: ", calc.mul())
#     elif choice == 4:
#         print("나누기 결과: ", calc.div())
#     elif choice == 5:
#         print("나머지 결과: ", calc.mod())
#     elif choice == 6:
#         print("제곱 결과: ", calc.pow())
#     else:
#         print("잘못된 입력입니다.")





















