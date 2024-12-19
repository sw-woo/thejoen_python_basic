# person_info = {"name":"우성우","job":"개발자","age":32,"gender":"남자","phone":"010-2222-2222"}
# print(person_info)
# print(person_info.get("address","지정하신 값이 없습니다."))
# print(person_info.get("name"))

# #딕셔너리에 값을 추가로 더하는 부분
# person_info["address"]="서울시 강서구 가양동"

# print(person_info)
# print(person_info.get("address","지정하신 값이 없습니다."))


# #딕셔너리에 기존에 키값에 값을 업데이트 하는 부분
# person_info["address"]= "인천광역시 송도 "
# print(person_info)
# print(person_info.get("address","지정하신 값이 없습니다."))

# person_info = {"name":"우성우","job":"개발자","age":32,"gender":"남자","phone":"010-2222-2222"}

# # 키 존재 여부 확인:
# if 'address' in person_info:
#     print('존재합니다.')
# else : 
#     person_info['address'] = '서울시 강서구 가양동'
#     print(f'{person_info}에 값을 추가하였습니다.')


# #딕셔너리 순회하기

# for key, value in person_info.items():
#     # print(key,value)
#     if key == 'name' and value == '우성우':
#         print("우성우라는 사람을 찾았습니다.")


# #딕셔너리 합치기:
# dict_one = {'a':'A','b':'B'}
# dict_two ={'c':'C','d':'D'}
# merged_dict = {**dict_one,**dict_two}
# print(merged_dict)

# #딕셔너리 컴프리핸션:
# squares = {x : x*2 for x in range(10)}
# print(squares)

# squares = {}
# for x in range(10):
#     squares[x] = x * 2
# print(squares)

# #기본 딕셔너리 설정:
# from collections import defaultdict
# my_default_dict = defaultdict(int)
# my_default_dict['key'] = "1" 
# print(my_default_dict)



# #키로 정렬된 딕셔너리 출력:
# for key in sorted(squares):
#     print(key,squares[key])


# person_info2 = {'name':"우성우",'age':30,"city":'서울시'}


#enumerate와 items() 조합으로 딕셔너리 순회:
# for index, (key, value) in enumerate(person_info2.items()):
#     print(index+1, key, value)


# for index,key in enumerate(person_info2.keys()):
#     print(index, key)

# for index,key in enumerate(person_info2.values()):
#     print(index, key)


# 리스트를 묶어서 딕셔너리로 변환하기
    
# names = ["john","jane","alice","Bob"]
# ages =[30,20,40,50]

# for name, age in zip(names, ages):
#     print(name,age)

# person_dic = dict(zip(names, ages))
# print(person_dic)


# name_list = list(person_dic.keys())
# print(name_list)

# age_list = list(person_dic.values())
# print(age_list)


#리스트 컴프리핸션:
# squares = [x**2 for x in range(10)]
# print(squares)

# squares2 = []
# for x in range(10):
#     squares2.append(x**2)
# print(squares2)

# numbers = list(range(10))
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# evens2= []
# for num in numbers:
#     if num % 2 == 0:
#         evens2.append(num)
# print(evens2)

#리스트의 문자열에서 첫 글자만을 추출하는 리스트 생성:
# words =["apple.txt","banana.txt","cherry.jpg"]
# first_letters =[word[-3:] for word in words]
# print(first_letters)

# evens3 = [num for num in range(1,21) if num % 2==0]
# print(evens3)
# increment_three = [num*3 for num in evens3]
# print(increment_three)

#리스트 컴프리핸션 예제 3

# temperatures = [0,22.5,40,100]
# coditions = ["Freezing" if temp <=0 else "Boiling" if temp >= 100 else "warm" for temp in temperatures]

# print(coditions)

# temperatures = [0, 22.5, 40, 100]
# conditions = []

# for temp in temperatures:
#     if temp <= 0:
#         conditions.append("Freezing")
#     elif temp >= 100:
#         conditions.append("Boiling")
#     else:
#         conditions.append("Warm")

# print(conditions)


#이중 반복문 리스트 컴프리핸션:

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# flattened_matrix = [num for rows in matrix for num in rows]
# print(flattened_matrix)

# flattened_matrix2 = []
# for row in matrix:
#     for num in row:
#         flattened_matrix2.append(num)
# print(flattened_matrix2)

# #딕셔너리 컴프리핸션 이중 반복 사용 예제:

# products = {
#     "Fruits": {"Apple":1000,"Banana":2000},
#     "Vegetables":{"Carrot":500, "Potato":300},
# }
# # 모든 제품의 이름을 키로 하고 가격을 값으로 하는 딕셔너리 생성 
# product_prices = {
#     product: price for category in products.values() for product, price in category.items()
# }
# print(product_prices)

# product_prices2 = {}
# for category in products.values():
#     for product,price in category.items():
#         product_prices2[product] = price
# print(product_prices2)


#문제: 주어진 문자열 리스트에서, 글자 수가 5개 이상인 문자열만 포함하는 새로운 리스트를 리스트 컴프리헨션을 사용하여 생성하세요.

words = ["apple", "it", "creek", "pelican", "subdermatoglyphic", "is"]

filtered_words = [word for word in words if len(word) >= 5]

print(filtered_words)

#문제:문제: 주어진 이름과 나이의 리스트에서, 나이가 18세 이상인 사람들만을 포함하는 딕셔너리를 딕셔너리 컴프리헨션을 사용하여 생성하세요. 
#이름을 키로, 나이를 값으로 사용하세요.

# people = [("John", 15), ("Jane", 22), ("Dave", 18), ("Sally", 12), ("Margot", 29)]

# adults = {name:age for name, age in people if age >= 18}

# print(adults)

# adults_ages = {age:name for name,age in adults.items()}

# print(adults_ages)

#데이터 타입 정리, 리스트,튜플, 딕셔너리, 집합
# a = []
# a.append(1)
# print(type(a), a)
# b= (1)
# b[2]=2
# print(type(b), b)
# c= {}
# d= set(['a','b','c'])
# print(type(d), d)
# d.add("e")
# d.remove('a')
# print(d)



# from function_cal import day_03_function as calculator
# import function_cal.day_03_function as calculator
# from function_cal.day_03_function import add, mul, sub, div

# print(calculator.add(10,20))
# print(calculator.mul(30,30))

# print(add(40,50))
# print(sub(70,60))
# print(div(80,90))

# from day03_random import *

# def main():
#     num_student = int(input("몇명의 학생이 있는가요?:"))
#     student = [input(f"학생{i+1}의 이름을 입력하세요")for i in range(num_student)]
#     print(play_selection_game(student))

# if __name__ == "__main__":
#     main()

#재귀함수: 함수가 자기 자신을 호출하는 것.
# def factorial(n):
#     if n ==1:
#         return 1
#     else :
#         return n+factorial(n-1)
    
# print(factorial(5))

# #재귀함수를 사용하여 피보나치 수열을 구하세요.
# def fibonacci(n):
#     if n ==0 or n==1 :
#         return 1
#     else: 
#         return fibonacci(n-2)+fibonacci(n-1)
# print(fibonacci(5))

#딕셔너리의 키워드 동적 인자: **kwargs
def group_by_age(**kwargs):
    for key, value in kwargs.items():
        print(key,value)


group_by_age(name="John", age=30, gender='M', address="Seoul", phone="010-2987-456")

#호출 단계에서 다입력을 받을수 있는 키워드 인자 : *args , **kwargs
def free_args(*args,**kwargs):
    print(args)
    print(kwargs)  

free_args(10,20,30,"a","b","c",[1,2,3],name="John", age=45, gender='M', address="Seoul")


















