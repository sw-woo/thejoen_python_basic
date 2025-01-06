def plus_ten(x):

    return x+10

print(plus_ten(1))

plus_ten_lambda = lambda x: x+10

print(plus_ten_lambda)

print((lambda x: x + 10)(1))


# map(함수, 리스트) 함수는 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아주는 함수이다.

print(list(map(plus_ten,[1,2,3])))

print(list(map(lambda x: x+10, [1,2,3])))

# 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수 : 식1 if 조건식 else 식2
# 조건식이 참인 경우 식1이 실행되고, 조건식이 거짓인 경우 식2가 실행된다.
# 3의 배수인 경우에는 문자열로 변환하고, 3의 배수가 아닌 경우에는 그대로 숫자로 유지하는 코드
# lambda 익명함수에서 if 조건문을 사용할 때는 반드시 else를 같이 사용해야 한다.
# 그리고 람다 표현식 안에서는 elif를 사용할 수 없습니다.
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

#1은 문자열로 변환 2는 실수로 변환 3이상은 10을 더한 값으로 변환
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
    
print(list(map(f,a)))

a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y: x * y, a, b)))


# filter(함수, 리스트) 함수는 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어준다.

def f(x):
    return x > 5 and x <10 

a = [8,3,2,10,15,7,1,9,0,11]

print(list(filter(f,a)))

print(list(filter(lambda x: x>5 and x<10, a)))

# reduce(함수, 순서형 자료) 함수는 순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용시킨다.
from functools import reduce

def reduce_sum(x,y):
    return x + y

a = [1,2,3,4,5]

print(reduce(reduce_sum, a))

print(reduce(lambda x, y: x + y, a))

# 리스트 컴프리헨션: [표현식 for 항목 in 순서형 자료]
a = [8,3,2,10,15,7,1,9,0,11]

filteredList = [i for i in a if i>5 and i<10]

print(filteredList)

# 반복문으로 reduce 구현하기

a = [1,2,3,4,5]

x = a[0]

for i in range(len(a)-1):
    x = x + a[i+1]

print(x)