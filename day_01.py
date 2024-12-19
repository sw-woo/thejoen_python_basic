# print("우성우")
# print(32)
# print("서울시 강서구")
# print("swpheus1@gmail.com")

# print(32*2)

# name = "우성우"
# age = 32
# address = "서울시 강서구"
# email = "<EMAIL>"
# print(f"이름은{name} 나이는{age} 주소는{address} 이메일은{email}")
# print(f"이름은 {name}\n나이는 {age}\n주소는 {address}\n이메일은 {email}")

# print(f"""
# 이름은 {name}
# 나이는 {age}
# 주소는 {address}
# 이메일은 {email}
# """)


# milks = ["초코","딸기","바나나","수박",10]
# print(f"""
#     {milks[:-5:-1]}
#  """)

#회원 정보를 저장하는 리스트를 만들어봅시다.
# name = input("이름을 입력해주세요")
# age = int(input("나이를 입력해주세요"))
# address = input("주소를 입력해주세요")
# email = input("이메일을 입력해주세요")

# person_info = [name, age, address, email]

# print(f"회원가입을 축하드립니다. 입력하신 정보가 아래와 같나요? \n{person_info}")
# print(f"회원님의 이름은{person_info[0]}")

# person_info.append(input("직업을 입력해주세요 !"))

# print(f"회원가입을 축하드립니다. 입력하신 정보가 아래와 같나요? \n{person_info}")


# number = [1,2,2,3,4]
# number.remove(2)
# print(number)

# color = ["red","green","blue"]
# last_color = color.pop()
# last_color = color[-1]
# print(last_color)


# ages = [3,45,1,3,20]
# ages.sort()
# print(ages)
# ages.sort(reverse=True)
# print(ages)

# number=[1,2,3,2,4]
# while 2 in number:
#     number.remove(2)
# print(number)

# for num in [1,2,3]:
#     print(num)


# name = "우성우"
# age = 32
# address = "서울시 강서구"
# email = "<EMAIL>"

# person_info_1 = [name,age,address,email]
# person_info_2 = [name,age,address,email]

# person_infos = [person_info_1,person_info_2]

# for info in person_infos:
#     print(f"{info}")
#     for name in info:
#         print(f"{name}")

# a= range(10)
# print(type(a))
# b= "성우"
# print(type(b))
# c= 20
# print(type(c))
# d= 20.20
# print(type(d))
# e = True
# print(type(e))

# for i in range(10):
#     print(i)

# print("------------------")

# for i in range(1,11):
#     print(i)

# for i in range(1,21):
#     if i % 2 == 1:
#         print(f"{i} 홀수")
#         if i % 3 ==0:
#             print(f"{i} 홀수중에서 3의 배수")


# total = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i
# print(total)

# num = range(1,5)

# for i in num:
#     print(i)
# print(num)


# status = True
# while status :
#     eng = int(input("영어 점수를 입력해주세요: "))

#     if eng >= 80:
#         print("합격")
#     else :
#         print("불합격")
#     if eng == 0:
#         status = False


# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print("----------------")


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()


























