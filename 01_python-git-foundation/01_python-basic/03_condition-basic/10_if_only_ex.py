# 1~10 사이의 숫자를 입력 받는다
# 1~10 사이의 숫자가 아니면 프로그램 종료
# 1~10 사이의 숫자가 숫자이면 출력

# import sys

# input_str = int(input("1부터 10까지의 숫자 입력: "))
# input_num = int(input_str)

# if (input_num < 0 or input_num > 10):
#     print(f"숫자가 입력 범위를 넘었습니다. 프로그램을 종료합니다. (입력값 : {input_num})")
#     sys.exit()

# print(f"1~10 사이의 숫자가 입력되었습니다. (입력한 숫자 : {input_num})")

import sys

# 1. 사용자 입력 받기 (문자열 상태)
input_data = input("1부터 10까지의 숫자 입력: ").strip()

# 2. 첫 번째 검사: 입력값이 숫자인지 확인 (숫자가 아니면 즉시 종료)
if not input_data.isdigit():
    print("숫자가 아닙니다. 프로그램을 종료합니다.")
    sys.exit()

# 숫자인 것이 확인되었으므로 안전하게 정수로 변환 (변수 최소화)
input_num = int(input_data)

# 3. 두 번째 검사: 범위를 벗어났는지 확인 (범위 밖이면 즉시 종료)
if input_num < 1 or input_num > 10:
    print(f"숫자가 입력 범위를 넘었습니다. (입력한 숫자 : {input_num})")
    sys.exit()

# 4. 모든 조건(if)을 통과한 경우에만 실행되는 정상 출력부
print(f"정상 입력되었습니다. 입력한 숫자: {input_num}")
