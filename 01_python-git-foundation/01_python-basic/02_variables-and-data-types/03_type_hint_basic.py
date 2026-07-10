r"""타입 힌트 기초 예제입니다.

실행:
    cd C:\aidev\01_python-git-foundation
    .\.venv\Scripts\Activate.ps1
    python .\01_python-basic\02_variables-and-data-types\03_type_hint_basic.py

타입 힌트는 변수가 어떤 종류의 값을 사용할 예정인지 표시하는 문법입니다.
Python은 기본적으로 실행 중에 타입 힌트를 강제로 검사하지는 않습니다.
하지만 VS Code가 코드를 이해하고, 잘못된 값을 넣었을 때 미리 알려 주는 데 도움이 됩니다.

함수에 타입 힌트를 붙이는 방법은 나중에 06_function-basic에서 다시 다룹니다.
"""

# 타입 힌트를 붙인 변수 선언입니다.
# name: str = "kim"은 name 변수에 문자열(str)을 넣어 사용할 예정이라는 뜻입니다.
name: str = "kim"
age: int = 20
height: float = 175.5
is_student: bool = True

print("이름:", name)
print("나이:", age)
print("키:", height)
print("학생인가요?", is_student)
print("-------------------------------")


msg = "       10000          "
print(f"입력{msg}입니다.")
print(f"입력{msg.strip()}입니다.")  # strip()은 문자열 양쪽 공백을 제거

# 원리: int() 함수는 내부적으로 문자열 양쪽의 공백을 자동으로 무시(strip 알고리즘 포함)하고,
# 순수 숫자 형태의 문자들만 파싱하여 정수형(int) 데이터로 변환합니다.
num = int(msg)
print(f"입력{num}입니다.")  # int()는 문자열을 정수로 변환

msg2 : str = "12,000,000"
num2 : int = int(msg2.replace(",", ""))  # replace()는 문자열 안의 특정 문자를 다른 문자로 바꿉니다.
print(f"입력{num2}입니다.")
print("-------------------------------")

# jmlee@tonesol.com
# id 변수에 jmlee 입력
# domain 변수에 tonesol.com 입력
# id와 domain을 합쳐서 이메일 주소를 출력
# "ID는 {id}이고, 도메인은 {domain}입니다." 출력

# id: str = input("아이디를 입력하세요: ")
# domain: str = input("도메인을 입력하세요: ")
# print(f"ID는 {id}이고, 도메인은 {domain}입니다. (이메일 주소: {id}@{domain})")

data : str = "jmlee@tonesol.com"
# 1. split()을 활용한 효율적인 압축 알고리즘 (추천 스타일)
# @ 기준으로 먼저 자른 뒤, 도메인 부분만 다시 . 기준으로 쪼갭니다.
id2, full_domain = data.split("@")
domain2: str = full_domain.split(".")[0]  # 'tonesol.com'에서 '.' 앞부분만 추출
print(f"ID는 {id2}이고, 도메인은 {domain2}입니다.")

id3 : str = data[:data.index("@")]  # index()는 특정 문자가 문자열에서 처음 나타나는 위치를 반환합니다.
domain3 : str = data[data.index("@")+1:data.index(".")]  # 슬라이싱을 사용하여 @ 뒤부터 . 앞까지 추출
print(f"ID는 {id3}이고, 도메인은 {domain3}입니다.")
