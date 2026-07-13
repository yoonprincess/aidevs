"""반환값(return) 기초 예제입니다.

return은 함수의 결과를 함수 밖으로 돌려주는 문법입니다.

print는 화면에 보여 주는 것이고,
return은 값을 다음 계산이나 다른 함수에서 다시 사용할 수 있게 해 줍니다.
"""


# def add(a: int, b: int) -> int:
#     result = a + b
#     return result

def add(a: int | float, b: int | float) -> float:
    print("=== add 함수 실행 ===")
    result = a + b
    return result

def divide(a: int | float, b: int | float) -> float | str:
    print("=== divide 함수 실행 ===")
    # 수정: 분모(b)가 0인 예외 상황을 먼저 쳐내어 에러를 원천 봉쇄
    if b == 0:
        # return None   # float | None
        return "0으로 나눌 수 없습니다."
    return a / b

def make_greeting(name: str) -> str:
    print("=== make_greeting 함수 실행 ===")
    message = f"{name}님, 안녕하세요."
    return message


sum_result = add(3, 5)
print("더하기 결과:", sum_result)

# return으로 받은 값을 다시 계산에 사용할 수 있습니다.
double_result = sum_result * 2
print("두 배 결과:", double_result)

# if b == 0: 
# > 이 라인이 없으면 0으로 나눌 때 ZeroDivisionError: division by zero 발생
print("나누기 결과:", divide(10, 0))
print("나누기 결과:", divide(10, 2))

# 함수는 문제없이 실행되지만...
result = divide(10, 0)  # result에 None이 담김

# 사용하는 곳에서 O(1)로 터짐
print(f"결과: {result:.2f}")  # TypeError: unsupported format string passed to NoneType
final_score = result + 5     # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

greeting = make_greeting("Jean")
print(greeting)

print("--------------------------------")

# return을 만나면 함수는 즉시 종료됩니다.
def check_number(number: int) -> str:
    if number < 0:
        return "음수입니다."

    return "0 또는 양수입니다."


print(check_number(-3))
print(check_number(10))

