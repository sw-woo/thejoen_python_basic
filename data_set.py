# set 자료형을 이용한 예시 

#1. set 생성 

fruits = {'apple','banana','cherry','banana'}
print(fruits)

#2. 요소 확인
if "apple" in fruits:
    print("apple is in fruits")

#. 요소 추가/삭제 

fruits.add("orange")
fruits.remove('banana') #remove()는 요소가 없을 경우 오류를 발생시킴
print(fruits)

#4. 집합 연산 
more_furits = {"cherry","mango","grape"}
common = fruits.intersection(more_furits) #교집합 
print(common)
diff = fruits.difference(more_furits)#차집합 
print(diff)

#5. 집합의 크기 확인
print(len(fruits))

#6. 집합의 합집합 구하기 
union = fruits | more_furits #합집합 
print(union)

#7. 집합의 차집합 구하기 
diff = fruits - more_furits #차집합 
print(diff)

#8. 집합의 대칭차집합 구하기 
symm_diff = fruits ^ more_furits #대칭차집합 
print(symm_diff)

