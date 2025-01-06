#1. 기본 try -except 구분 

# def safe_division(a, b):
#     try:
#         result = a / b
#         print(f"결과: {result}")
#     # except Exception as e:
#     #     print(f"에러 발생: {e}")
#     except ZeroDivisionError:
#         print("0원으로 나눌 수 없습니다!")

# #테스트 
# safe_division(10, 2)
# safe_division(10, 0)

# def process_data(data):
#     try: 
#         # 데이터는 무조건 리스트 형태라고 가정 
#         total = 0
#         for item in data:
#             total += item 
#         print("합격:", total)
    
#     # except TypeError :
#     #     print("데이터 안에 숫자가 아닌 값이 포함되어 있습니다.")

#     except AttributeError:
#         print("리스트가 아닌 데이터가 들어왔습니다.")

#     except Exception as e:
#         print(f"알 수 없는 오류가 발생하였습니다.: {e}")

# process_data([1,2,3])
# process_data([1,2,"python"])
# process_data("Hello")
# process_data(None)



# try ~ except ~ else ~ finally 구문 

# def file_read_example(filename):
#     try:
#         f = open(filename, 'r', encoding='utf-8')
#         content = f.read()
#     except FileNotFoundError:
#         print(f"파일을 찾울 수 없습니다: {filename}")
#     else:
#         # 예외가 발생하지 않았을 때 실행되는 코드 
#         print("파일을 성공적으로 읽었습니다.")
#         print("내용", content)
#     finally:
#         # 예외 발생 여부와 상관없이 무조건 실행되는 코드
#         print("파일을 닫습니다.")
#         try:
#             f.close()
#             print("파일을 닫았습니다.")
#         except NameError: 
#             pass

# # 테스트
        
# file_read_example("test.txt")
# file_read_example("not_exist.txt")


# raise 키워드를 사용하면 현재 코드에서 특정 예외를 명시적으로 발생시킬 수 있습니다.

# def get_positive_value(value):
#     if value < 0:
#         raise ValueError("음수는 사용할 수 없습니다.")
#     return value

# # 테스트 
# # print(get_positive_value(1))
# # print(get_positive_value(-1))

# try:
#     val = get_positive_value(-1)
# except ValueError as e:
#     print(f"예외 발생: {e}")


# 5. 사용자 정의 예외 (Custom Exception)
# 파이썬 내장 예외가 아닌, 프로그램 로직에 맞는 예외를 직접 만들어 사용할 수도 있습니다.

class NotEnoughFundsError(Exception):
    """ 잔액이 부족할 때 발생하는 오류"""
    pass

def withdraw_money(balance, amount):
    if balance < amount:
        raise NotEnoughFundsError("잔액이 부족합니다.")
    return balance - amount
    

# 테스트 
try: 
    new_balance = withdraw_money(1000, 2000)
except NotEnoughFundsError as e:
    print(f"예외 발생: {e}")