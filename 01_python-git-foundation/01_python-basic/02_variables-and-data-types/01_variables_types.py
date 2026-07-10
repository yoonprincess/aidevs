"""변수와 자료형 예제입니다.

변수는 값을 담아 두는 이름입니다.
자료형은 값의 종류를 의미합니다.

이 예제에서는 문자열(str), 정수(int), 불(bool)을 확인합니다.
"""

# 변수는 값을 담는 이름입니다.
# 오른쪽 값을 왼쪽 변수 이름에 저장한다고 이해하면 됩니다.
user_name = "Jean"
user_name = 'kim'
# 큰따옴표, 작은따옴표 모두 문자열을 표현할 수 있습니다.
# 변수에 두 번 값을 저장하면 마지막 값이 최종적으로 저장됩니다.

user_age = 30
user_height = 175.5
is_beginner = True
# is_beginner = true    # true는 소문자로 작성하면 오류남

# 변수 이름 뒤에 : str, : int, : bool처럼 적는 것을 타입 힌트라고 합니다.
# name: str = "kim"은 "name 변수는 문자열로 사용할 예정"이라는 뜻입니다.
# 지금은 힌트처럼 이해하고, FastAPI/Pydantic을 배울 때 더 자주 만나게 됩니다.
name: str = "kim"
# name: str = 100   # type을 출력했을 때 int로 나옴
age: int = 20
height: float = 180.5
# weight: double = 70.5 # double은 Python에서 지원하지 않는 자료형(float을 사용)
is_student: bool = True

# 문자열, 숫자, True/False 값을 각각 출력합니다.
print("이름:", user_name, "입니다.")
print("나이:", user_age)
print("키:", user_height)
print("초보자인가요?", is_beginner)
print("타입 힌트 예시:", name, age, height, is_student)
print("-------------------------------")

# type()은 값이나 변수의 자료형을 확인하는 함수입니다.
# str은 문자열, int는 정수, bool은 참/거짓 값을 뜻합니다.
print("user_name의 자료형:", type(user_name))
print("user_age의 자료형:", type(user_age))
print("user_height의 자료형:", type(user_height))
print("is_beginner의 자료형:", type(is_beginner))
print("-------------------------------")
print("name의 자료형:", type(name))
print("age의 자료형:", type(age))
print("height의 자료형:", type(height))
print("is_student의 자료형:", type(is_student))
print("-------------------------------")

# input()으로 받은 값이나 따옴표로 감싼 숫자는 문자열입니다.
# 문자열 "1000"은 숫자 1000과 다르기 때문에 바로 계산할 수 없습니다.
price_text = "1000"

# int()는 숫자 모양의 문자열을 정수로 변환합니다.
price = int(price_text)
print("가격 + 500 =", price + 500)

# print("가격 + 500 =", price_text + 500)
# 에러 원인: 문자열(str) 데이터 타입인 'price_text' 변수와 정수(int)인 '500'을 '+' 연산자로 직접 더하려고 해서 발생한 TypeError입니다.
# 해결 방법: 'price_text'를 정수형(int)으로 변환한 뒤 연산하거나, 요새 많이 쓰는 f-string 스타일을 사용해야 합니다.

# 수정 방법 1: 정수형 변환 (int() 사용)
print("가격 + 500 =", int(price_text) + 500)

# 수정 방법 2: 요즘 많이 쓰는 개발 스타일 (f-string 내에서 변환 및 연산)
print(f"가격 + 500 = {int(price_text) + 500}")

a = 10
b = 3
c = 100

result = a + b / c
print("결과:", result)

result2 = a + int(b / c)
print("결과2:", result2)