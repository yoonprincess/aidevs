# # Assignment 02 - Condition Menu

# 조건문을 사용해 메뉴 기반 프로그램을 만듭니다.

# ## 과제 파일

# ```text
# submissions/assignment02_condition_menu.py
# ```

# ## 요구사항

# ```text
# 1. 메뉴를 출력합니다.
# 2. 메뉴 번호를 입력받습니다.
# 3. 1번: 점수 등급 계산
# 4. 2번: 숫자 양수/0/음수 판별
# 5. 3번: 사용자 역할 안내
# 6. 그 외: 알 수 없는 메뉴 안내
# ```

# ## 세부 조건

# 점수 등급 계산:

# ```text
# 90 이상: A
# 80 이상: B
# 70 이상: C
# 그 외: D
# ```

# 사용자 역할 안내:

# ```text
# admin: 관리자입니다.
# member: 일반 사용자입니다.
# guest: 게스트입니다.
# 그 외: 알 수 없는 역할입니다.
# ```

# ## 권장 문법

# ```text
# if
# elif
# else
# match-case
# ```

# ## 확인 기준

# ```text
# 여러 조건이 올바른 순서로 검사되는가?
# 잘못된 메뉴 입력도 처리하는가?
# match-case 또는 if/elif/else 중 적절한 방식을 선택했는가?
# ```

print("===============================")

print("------------- 메뉴 -----------")
print("1. 점수 등급 계산")
print("2. 숫자 양수/0/음수 판별")
print("3. 사용자 역할 안내")
print("--------------------------------")

menu = input("메뉴 번호를 입력하세요 (1~3): ")

match menu:
    case "1":
        print("[점수 등급 계산 메뉴]")

        score = input("점수를 입력하세요: ")
 
        # 숫자인지 먼저 검사
        if not score.isdigit():
            print("❌ 점수가 숫자가 아닙니다. 프로그램을 종료합니다.")
            print("============== 강제 종료 =================")
            exit()

        # 검증 후 정수 변환
        score = int(score)

        if (score >= 90):
            print("점수 등급: A")
        elif (score >= 80):
            print("점수 등급: B")
        elif (score >= 70):
            print("점수 등급: C")
        else:
            print("점수 등급: D")

    case "2":
        print("[숫자 양수/0/음수 판별 메뉴]")

        num = input("숫자를 입력하세요: ")

        # 마이너스(-) 기호를 제외한 순수 숫자인지 검사하거나, lstrip('-')을 활용합니다.
        if not num.lstrip("-").isdigit():
            print("❌ 입력값이 숫자가 아닙니다. 프로그램을 종료합니다.")
            print("============== 강제 종료 =================")
            exit()

        # 검증 후 정수 변환
        num = int(num)

        if (num > 0):
            print("입력한 숫자는 양수입니다.")
        elif (num < 0):
            print("입력한 숫자는 음수입니다.")
        else:
            print("입력한 숫자는 0입니다.")

    case "3":
        print("[사용자 역할 안내 메뉴]")

        role = input("사용자 역할을 입력하세요 (admin/member/guest): ")

        match role:
            case "admin":
                print("관리자입니다.")
            case "member":
                print("일반 사용자입니다.")
            case "guest":
                print("게스트입니다.")
            case _:
                print("알 수 없는 역할입니다.")

    case _:
        print("❌ 알 수 없는 메뉴입니다. 프로그램을 종료합니다.")
        print("============== 강제 종료 =================")
        exit()
