# yield의 동작 방식 살표보기 
# 아래 함수는 카운트를 n번부터 반복해서 하나씩 꺼네주는 제너레이터 함수 입니다.
# yield는 값을 반환하고 함수를 일시정지 시킵니다. 즉 함수를 호출한 쪽에서 값을 꺼내서 사용할 수 있고
# 다시 함수를 호출하면 일시정지된 부분부터 다시 실행됩니다.
# def countdown(n):
#     print('카운트다운을 시작합니다.')
#     while n > 0:
#         yield n
#         n -= 1
#     print("카운트다운 종료!")

# # 제너레이터 생성 
    
# gen = countdown(3) # gen은 제너레이터 객체입니다.

# # # 값을 하나씩 꺼내면서 출력합니다.

# print(next(gen))
# print(next(gen))
# print("2번째는 짝 수 입니다.")
# print(next(gen))

#제너레이터를 사용 하는 이유 
# 메모리 효율성:
# 한 번에 모든 결과물을 리스트나 다른 자료구조로 만들어서 반환하지 않고, 필요할 때마다 값을 꺼내쓸 수 있으므로
# 메모리를 효율적으로 사용할 수 있습니다.
# 느긋한 계산(Lazy Evaluation):
# 모든 데어트를 미리 계산하지 앟ㄴ고, 요청이 있을때(next 호출 시)에만 값을 생성(계산)하여 방출합니다.
# 계산 비용이 큰 작업을 단계적으로 처리할 때 유리합니다.
# 구현의 간결성 
# 제너레이터를 사용하면 복잡한 반복문을 작성할 필요가 없어져서 코드가 간결해집니다.




# def countdown_while(n):
#     print('카운트다운을 시작합니다.')
#     while n > 0:
#         print(n)
#         if n == 2:
#             print("2번째는 짝 수 입니다.")
#         n -= 1
#     print("카운트다운 종료!")

# countdown_while(3)

# 제너레이터 yield 구구단 출력해보기

def multiplication_table(n):
    """
    n단의 구구단을 출력하는 제너레이터 함수
    """

    for i in range(1,10):
        yield f"{n} X {i} = {n*i}"

gugudan = multiplication_table(3)

# for i in gugudan:
#     print(i)

for _ in range(4):
    print(next(gugudan))
print("즐거운 구구단")

for _ in range(5):
    print(next(gugudan))
print("즐거운 구구단")



# try:
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
#     print("구구단은 즐겁다.")
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
#     print(next(gugudan))
# except StopIteration as e:
#     print("더 이상 구구단이 없습니다.",e)