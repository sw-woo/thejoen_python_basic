# def add(a, b,c):
#     result = a + b+c
#     return result

#파라메터 갯수를 동적으로 처리하는 방법 **
# def add(*arg):
#     print(type(arg), arg)
#     for i in arg:
#         print(i)
#     result = 0
#     for i in arg:
#         result += i
#     return result

# print(add(10,20,30,50,60))


def add(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def mul(a,b):
    result = a*b
    return result

def div(a,b):
    div = a//b
    remain = a%b
    return div,remain

# print(add(10,20))
# print(sub(30,50))
# print(mul(40,60))
# print(div(80,80))


















