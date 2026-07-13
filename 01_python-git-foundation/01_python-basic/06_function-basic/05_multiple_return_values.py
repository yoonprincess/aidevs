"""여러 값을 반환하는 함수 예제입니다.

Python 함수는 여러 값을 한 번에 반환할 수 있습니다.
실제로는 tuple 형태로 반환되고, 이를 여러 변수에 나누어 받을 수 있습니다.
"""

# def calculate(a, b)
def calculate(a: int | float, b: int | float) -> tuple[float, float, float, float]:
    add_result = a + b
    subtract_result = a - b
    multiply_result = a * b
    divide_result = a / b

    return add_result, subtract_result, multiply_result, divide_result

# 패킹(Packing)된 튜플 형태 그대로 받아서 순회
result: tuple[float, float, float, float] = calculate(10, 2)

for r in result:
    print(r)
print("--------------------------------------")

# 튜플 언패킹(Tuple Unpacking)
# > Tuple 안의 값을 여러 변수에 나누어 담을 수 있음
plus, minus, multiply, divide = calculate(10, 2)

print("더하기:", plus)
print("빼기:", minus)
print("곱하기:", multiply)
print("나누기:", divide)
print("--------------------------------------")

# def get_min_max(numbers):
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest


scores = [80, 95, 70, 88]
min_score, max_score = get_min_max(scores)

print("최저 점수:", min_score)
print("최고 점수:", max_score)


print("============================================")

# 숫자로 되어 있는 List를 입력하면
# 최소값과 최대값의 합계 평균을 반환하는 함수,
# dict 형태로 반환하는 함수를 구현
datas = [10, 20, 30, 40, 50, 60]

def get_min_max_stats(n: list[int]) -> dict[str, float]:
    min_val = min(n)
    max_val = max(n)
    total_sum = min_val + max_val
    avg_val = (min_val + max_val) / 2

    return {
        "min": min_val,
        "max": max_val,
        "sum": total_sum,
        "avg": avg_val,
    }

# print(get_min_max_stats(datas))
# 함수 호출 및 출력 테스트
scores: list[int] = [80, 95, 70, 88, 62]
result: dict[str, int | float] = get_min_max_stats(scores)

print(f"결과 딕셔너리: {result}")
print(f"최소값: {result['min']}, 최대값: {result['max']}, 두 값의 합계: {result['sum']}, 평균: {result['avg']:.1f}")

