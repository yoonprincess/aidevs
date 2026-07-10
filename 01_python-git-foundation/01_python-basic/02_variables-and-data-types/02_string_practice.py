"""문자열 기초 예제입니다.

문자열은 글자들의 모음입니다.
Python에서는 문자열의 특정 위치를 가져오거나, 일부만 잘라내거나,
대소문자를 바꾸는 작업을 쉽게 할 수 있습니다.
"""

# 1. 데이터 선언
# message 변수에 문자열을 저장합니다.
message : str = "Python Basic"

print("전체 문자열:", message)
print("문자열 길이:", len(message)) # len()은 문자열 길이를 확인하는 함수입니다.
print(f"문자열 길이: {len(message)}") # f-string을 사용하면 문자열 안에 변수 값을 넣을 수 있습니다.
print(f"문자열\t길이:\n{len(message)}") # \t는 탭(tab) 공백, \n은 줄바꿈을 의미
print("-------------------------------")

# 2. 인덱싱 (0부터 시작)
print(f"문자열 첫 글자: {message[0]}")  # 'P'

# 3. 슬라이싱 [시작:끝] -> 끝 위치 '전'까지 잘라내기
# "Python Basic"에서 인덱스 0부터 5까지는 'P', 'y', 't', 'h', 'o', 'n'입니다.
print(f"문자열 앞에서 6글자: {message[:6]}")  # 'Python'

# 4. [4:6] 슬라이싱 범위 지정 (인덱스 4부터 5까지만 추출)
# "Python Basic"에서 인덱스 4는 'o', 5는 'n'입니다.
print(f"문자열 [4:6]: {message[4:6]}")  # 'on'

# 5. 음수 인덱싱 (뒤에서부터 역순)
# 인덱스 -1, -2, -3, -4, -5는 각각 'c', 'i', 's', 'a', 'B'입니다.
print(f"문자열 뒤에서 5글자: {message[-5:]}")  # 'Basic'

# lower()는 모든 영문자를 소문자로 바꿉니다.
print("소문자:", message.lower())

# upper()는 모든 영문자를 대문자로 바꿉니다.
print("대문자:", message.upper())

name = "Jean"
score = 95

# f-string은 문자열 안에 변수 값을 넣을 때 사용하는 편리한 문법입니다.
# 문자열 앞에 f를 붙이고, 중괄호 { } 안에 변수 이름을 넣습니다.
print(f"{name}님의 점수는 {score}점입니다.")
