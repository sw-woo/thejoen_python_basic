#데코레이터 시간을 측정해주는 함수
import time

def time_calculator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time() # 시작 시간 기록
        result = func(*args, **kwargs) # 실제 함수 호출 실행 
        end_time = time.time() # 종료 시간 기록

        elapsed_time = end_time - start_time # 경과 시간 계산 
        print(f"{func.__name__} 함수 실행 시간: {elapsed_time:.4f}초") # 함수 이름과 경과 시간 출력

        return result

    return wrapper

@time_calculator # 데코레이터 적용
def slow_function():
    total = 0
    for _ in range(10000000):
        total +=1
    return total

# 함수 호출 
result = slow_function()
print("결과:",result)

@time_calculator # 데코레이터 적용
def odd_function():
    total = 0
    for i in range(1, 10000000, 2):
        total += i
    return total
