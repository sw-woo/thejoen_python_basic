# 1. 기본 try-except 사용
# 가장 간단한 예외 처리 구문은 try-except입니다. 특정 코드 블록을 실행(try)해보다가 예외가 발생하면(except) 해당 예외를 처리하는 식입니다.

def safe_division(a, b):
    try:
        result = a / b
        print(f"결과: {result}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")

# 테스트
# safe_division(10, 2)   # 정상 계산 -> 결과: 5.0
# safe_division(10, 0)   # 예외(ZeroDivisionError) -> 0으로 나눌 수 없습니다!
# safe_division 함수는 두 수를 나누는 과정에서 0으로 나누는 오류가 발생하면, 프로그램이 강제 종료되지 않고 "0으로 나눌 수 없습니다!" 메시지를 출력하고 넘어갑니다.
# 2. 여러 개의 except 처리
# 여러 종류의 예외를 구분해서 처리할 때는 except를 연달아 쓰거나, except (예외1, 예외2)처럼 묶어서 처리할 수 있습니다.


def process_data(data):
    try:
        # 데이터는 무조건 리스트 형태라고 가정
        total = 0
        for item in data:
            total += item
        print("합계:", total)
    except TypeError:
        # 예: 리스트 안에 정수가 아닌 값이 들어 있어 + 연산에 문제가 생겼을 때
        print("데이터 안에 숫자가 아닌 값이 포함되어 있습니다.")
    except AttributeError:
        # 예: data가 리스트가 아니라 .append 등 리스트 메서드 호출이 불가능할 때
        print("리스트가 아닌 데이터가 들어왔습니다.")
    except Exception as e:
        # 다른 예외를 모두 처리하고 싶다면
        print("알 수 없는 오류가 발생했습니다:", e)

# 테스트
process_data([1, 2, 3])        # 정상 -> 합계: 6
process_data([1, 2, "Python"]) # TypeError -> "데이터 안에 숫자가 아닌 값이..."
process_data("Hello")          # AttributeError -> "리스트가 아닌 데이터가..."
process_data(None)             # 다른 예외 -> "알 수 없는 오류가 발생했습니다: ..."
# 구체적인 예외를 위에서부터 차례대로 핸들링할 수 있습니다.
# except Exception as e: 구문으로 모든 예외를 포괄 처리할 수도 있습니다.
# 3. else와 finally
# 예외 처리 구문에는 else, finally 블록을 함께 사용할 수 있습니다.

# else: try 블록 안에서 예외가 전혀 발생하지 않았을 때만 실행되는 블록
# finally: 예외 발생 여부와 상관없이 항상 실행되는 블록 (자원 정리, 파일 닫기 등에 유용)
# 파일 읽기 예시
def file_read_example(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        content = f.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
    else:
        # 예외가 발생하지 않았을 때만 실행
        print("파일을 성공적으로 읽었습니다.")
        print("내용:", content)
    finally:
        # 파일 객체가 있다면 닫아주기
        try:
            f.close()
            print("파일을 닫았습니다.")
        except NameError:
            # f가 정의되지 않았다면(파일을 못 열었다면) pass
            pass

# 테스트
file_read_example("존재하는파일.txt")  # 파일을 성공적으로 읽고 else와 finally가 실행
file_read_example("존재하지않는파일.txt")  # except와 finally가 실행
# finally 블록은 무조건 실행되므로, 파일 닫기(I/O 자원 정리), 데이터베이스 커넥션 종료, 락 해제 등과 같은 후속 처리를 하는 데 적합합니다.
# 4. 예외 발생(raise)하기
# 가끔은 함수 안에서 직접 예외를 발생시켜 의도적으로 에러 상황을 알리는 경우도 있습니다.


def get_positive_value(value):
    if value < 0:
        raise ValueError("음수는 허용되지 않습니다.")
    return value

# 테스트
try:
    val = get_positive_value(-5)
except ValueError as e:
    print("오류 발생!", e)  # -> 오류 발생! 음수는 허용되지 않습니다.

# raise 키워드를 사용하면 현재 코드에서 특정 예외를 명시적으로 발생시킬 수 있습니다.
# 이렇게 하면 잘못된 입력을 빨리 감지하고, 상위 로직에서 어떻게 처리할지 결정할 수 있습니다.
# 5. 사용자 정의 예외(Custom Exception)
# 파이썬 내장 예외가 아닌, 프로그램 로직에 맞는 예외를 직접 만들어 사용할 수도 있습니다.


class NotEnoughFundsError(Exception):
    """잔액이 부족할 때 발생시키는 사용자 정의 예외"""
    pass

def withdraw_money(balance, amount):
    if balance < amount:
        # 커스텀 예외 발생
        raise NotEnoughFundsError("잔액이 부족합니다!")
    return balance - amount

# 테스트
try:
    new_balance = withdraw_money(1000, 2000)
except NotEnoughFundsError as e:
    print("출금 실패:", e)  # -> 출금 실패: 잔액이 부족합니다!

# Exception 클래스를 상속해 새로운 예외 클래스를 정의할 수 있습니다.
# 이렇게 하면 에러 상황을 보다 직관적이고 구체적으로 표현하여, 큰 규모의 프로젝트에서도 에러 유형을 쉽게 식별할 수 있습니다.
# 6. 실전 예시: API 호출과 예외 처리
# 실제 업무에서 자주 하는 웹 API 요청 예시입니다.


import requests

def fetch_data_from_api(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 4xx/5xx 발생 시 HTTPError 예외 발생
    except requests.Timeout:
        print("요청 시간이 초과되었습니다.")
    except requests.ConnectionError:
        print("네트워크 연결 오류가 발생했습니다.")
    except requests.HTTPError as e:
        print(f"HTTP 오류 발생: {e.response.status_code}")
    else:
        print("API 요청 성공!")
        return response.json()

# 테스트
data = fetch_data_from_api("https://api.github.com/users/octocat")
if data:
    print(data["name"])  # "The Octocat"

# requests.get() 시도 중 시간 초과가 발생하면 requests.Timeout 예외를 처리
# 네트워크 연결 실패 시 requests.ConnectionError 예외를 처리
# response.raise_for_status()로 HTTP 상태 코드가 4xx/5xx일 경우 requests.HTTPError 예외
# 예외가 전혀 없으면(else) JSON 데이터를 받아서 반환
# 이처럼 에러를 구체적으로 분기 처리해주면, API 호출이 실패했을 때의 원인을 정확히 파악할 수 있고, 후속 조치(재시도, 대체 로직 등)를 취하기가 수월해집니다.

# 7. 예외 처리 시 주의 사항
# 과도한 범위의 except: pass
# 모든 예외를 무조건 pass로 처리하면 디버깅이 어려워집니다. 필요한 경우가 아니라면 피하세요.
# 구체적 예외의 순서
# 여러 예외를 except로 처리할 때, 가장 구체적인 예외부터 작성하고, 마지막에 Exception처럼 가장 광범위한 예외를 처리하세요.
# 로그(logging)
# 실제 운영 환경에서는 print 대신 logging 모듈을 사용하여 예외 정보를 로그로 남기는 것이 일반적입니다.
# 예외 재발생(Raise)
# 예외를 잡고도 완전히 해결할 수 없는 경우, raise로 다시 예외를 던져 상위 레벨에서 처리하도록 하는 방법도 있습니다.
# 마무리
# 예외 처리를 통해 프로그램이 의도하지 않은 상황을 만났을 때 우아하게 대응할 수 있습니다.
# try-except-else-finally 구문을 적절히 사용하면, 로직이 복잡하더라도 명확한 예외 흐름을 유지할 수 있습니다.
# 사용자 정의 예외나 raise를 통해 에러 상황을 직접 설계할 수 있으며, 이는 대규모 프로젝트에서 매우 중요한 패턴입니다.
# 이렇게 파이썬 예외 처리를 잘 활용하면, 안정적인 코드와 효율적인 디버깅 환경을 구축할 수 있습니다