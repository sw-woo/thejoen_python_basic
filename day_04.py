# import random


import day_04_2 as ch

sungwoo = ch.warrior("sungwoo-전사3")

print(sungwoo.name)
print(sungwoo.strength)
print(sungwoo.agility)
print(sungwoo.intellect)













# def generate_lotto_numbers():
#     """
#     Generates random lotto numbers based on user input.
#     """
#     print("***로또번호생성기***")
#     print("===================================")
#     print("***게임수를 입력하세요 숫자만***")
#     cn =  'y'

#     while (cn =='y'):
#         num = input('게임수:')
#         if (num.isdigit() == True):
#             print("--------------------")
        
#             for i in range(0, int(num)):
#                 lotto = random.sample(range(1,46), 6)
#                 lotto.sort()
#                 print(lotto)
#         else:
#             print("------------------")
#             print("숫자만 입력하세요!")
#             continue

#         print("------------------")
#         print("*** 로또번호 생성 완료 ***")
#         cn = input("다시하시겠습니까? (y/n):")

#         while (cn != 'y' and cn != 'Y' and cn != 'n' and cn != 'N'):
#             print("------------------")
#             print("y 또는 n만 입력하세요!")
#             cn = input("다시하시겠습니까? (y/n):")

#     print("===================================")
#     print("***로또번호생성기 종료***")
#     print("===================================")


# generate_lotto_numbers()
        



