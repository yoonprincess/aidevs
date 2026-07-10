# # Assignment 03 - Loop Calculator

# 반복문을 사용해 계속 사용할 수 있는 계산기 프로그램을 만듭니다.

# ## 과제 파일

# ```text
# submissions/assignment03_loop_calculator.py
# ```

# ## 요구사항

# ```text
# 1. while True를 사용합니다.
# 2. 첫 번째 숫자를 입력받습니다.
# 3. 첫 번째 입력값이 q이면 프로그램을 종료합니다.
# 4. 두 번째 숫자를 입력받습니다.
# 5. 연산자 +, -, *, / 중 하나를 입력받습니다.
# 6. 계산 결과를 출력합니다.
# 7. 0으로 나누는 경우 안내 문장을 출력합니다.
# 8. 계산 후 다시 다음 계산을 받을 수 있어야 합니다.
# ```

# ## 추가 요구사항

# ```text
# 1. 사용자가 잘못된 연산자를 입력하면 안내 문장을 출력합니다.
# 2. continue를 최소 1번 사용합니다.
# 3. break를 최소 1번 사용합니다.
# ```

# ## 확인 기준

# ```text
# q 입력 시 정상 종료되는가?
# 계산 후 반복이 계속되는가?
# continue와 break의 역할을 설명할 수 있는가?
# ```

while True:
    # 첫 번째 숫자
    num = input("첫 번째 숫자를 입력하세요 (종료: q): ")

    # q 입력 시 종료
    if num == "q":
        print("👋 프로그램을 종료합니다. Bye...")
        break

    # 숫자가 아니어도 종료
    if not num.isdigit():
        print("숫자가 아닙니다. 프로그램을 종료합니다.")
        break
    # 두 번째 숫자
    num2 = input("두 번째 숫자를 입력하세요: ")

    # q 입력 시 종료?
    if num2 == "q":
        print("👋 프로그램을 종료합니다. Bye...")
        break

    # 숫자가 아니어도 종료
    if not num2.isdigit():
        print("숫자가 아닙니다. 프로그램을 종료합니다.")
        break

    # 연산자 입력
    operator = input("연산자를 입력하세요 (+, -, *, /): ")

    # 잘못된 연산자 입력 시 프로그램 종료가 아닌, 안내 후 처음으로 되돌리기
    if operator not in ("+", "-", "*", "/"):
        print("❌ 오류: 잘못된 연산자입니다. (+, -, *, /) 중 하나를 입력하세요.")
        continue

    # 계산 수행
    num1 = int(num)
    num2 = int(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("❌ 오류: 0으로 나눌 수 없습니다. 다시 입력해 주세요.")
            continue
        result = num1 / num2

    print(f"✅ 계산 결과: {num1} {operator} {num2} = {result}")

