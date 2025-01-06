#람다 표현식 알아보기

def plus_ten(x = 10):
    return x + 10

print(plus_ten())


plus_ten_lambda = lambda x: x +10
print(plus_ten_lambda)
print(plus_ten_lambda(1))

print((lambda x : x +10)(1))


y=20 

z = (lambda x : x + y)(1)

print(z)

print(list(map(lambda x : x + 10, [1, 2, 3])))


print(list(map(plus_ten, [1, 2, 3])))

#람다 표현식에 map 함수를 사용해서 제곱값을 구하는 코드를 작성해주세요 

def square(x):
    return x ** 2

print(list(map(square, [1,2,3])))

print(list(map(lambda x : x ** 2, [1,2,3])))


#람다 표현식에서 조건부 표현식 사용하기
# lambda 매개변수 : 식1 if 조건식 else 식2
# 조건식이 참인 경우 식1이 실행되고, 조건식이 거짓인 경우 식2가 실행된다.
# 3의 배수인 경우에는 문자열로 변환하고, 3의 배수가 아닌 경우에는 그대로 숫자로 유지하는 코드
# lambda 익명함수에서 if 조건문을 사용할 때는 반드시 else를 같이 사용해야 한다.
# 그리고 람다 표현식 안에서는 elif를 사용할 수 없습니다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b =list(range(1,11))

print(list(map(lambda x : str(x)if x % 3 == 0 else x, a)))

#1은 문자열로 변환 2는 실수로 변환 3이상은 10을 더한 값으로 변환
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

#map 여러 객체 넣어보기 

a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y: x - y, a, b)))


#filter 함수 사용하기
def f(x):
    return x > 5 and x <10 

a = [8,3,2,10,15,7,1,9,0,11]

print(list(filter(f,a)))

#람다 표현식으로 filter 함수 사용하기

print(list(filter(lambda x : x > 5 and x < 10, a)))

#람다 표현식으로 10이하의 숫자만 필터링해보세요

print(list(filter(lambda x : x <= 10, a)))

#reduce 함수 사용하기 
from functools import reduce 

def reduce_sum(x,y):
    return x + y

a = list(range(1,6))

print(reduce(reduce_sum, a))


total = 0
for i in range(1,6):
    total += i

print(total)

# 람다 표현식으로 reduce 함수 사용하기
print(reduce(lambda x, y : x + y, a))





