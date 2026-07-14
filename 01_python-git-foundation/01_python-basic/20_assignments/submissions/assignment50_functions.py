########### 과제 #############
"""
1. 프로그램을 실행합니다.
2. 이름을 입력받습니다.
3. 직업을 선택합니다.
    1. 전사
    2. 마법사
    3. 궁수
4. 레벨을 입력받습니다.
5. 레벨이 1보다 작으면 다시 입력받습니다.
6. 선택한 직업과 레벨을 출력합니다.
7. 첫 번째 입력에서 q를 입력하면 프로그램을 종료합니다.
"""

# print("======================= 과제 =======================")
# def start_rpg_character_creator() -> None:
#     # 1. 프로그램을 실행합니다.
#     print("----------- 프로그램 실행 ------------")

#     # 2. 이름을 입력받습니다.
#     name: str = input("이름을 입력하세요 (종료하려면 'q' 입력): ").strip()
#     # (7. 첫 번째 입력에서 'q'를 입력하면 종료합니다.)
#     if name.lower() == 'q':
#         print("프로그램을 종료합니다.")
#         return

#     # 3. 직업을 선택합니다.
#     print("직업을 선택하세요:\n1. 전사\n2. 마법사\n3. 궁수")
    
#     # 올바른 직업을 선택할 때까지 반복
#     while True:
#         job_choice: str = input("직업 번호 선택: ").strip()
        
#         # 1, 2, 3일 때만 job을 정하고 break로 내부 루프 탈출
#         match job_choice:
#             case "1":
#                 job = "전사"
#                 break
#             case "2":
#                 job = "마법사"
#                 break
#             case "3":
#                 job = "궁수"
#                 break
#             case _:
#                 # 잘못 입력하면 break를 만나지 못하므로 while 루프 처음으로 돌아가 다시 입력받음
#                 print("올바른 직업 번호가 아닙니다. 직업을 다시 선택하세요.")
#                 print("-------------------------------")

#     # 4. 레벨을 입력받습니다.
#     while True:
#         level_input: str = input("레벨을 입력하세요: ").strip()

#         if not level_input.isdigit():
#             print("올바른 숫자로 레벨을 입력해주세요.")
#             print("-------------------------------")
#             continue
            
#         level = int(level_input)
        
#         # 5. 레벨이 1보다 작으면 다시 입력받습니다.
#         if level < 1:
#             print("레벨은 1 이상이어야 합니다. 다시 입력해주세요.")
#             print("-------------------------------")
#             continue
#         break

#         # 6. 선택한 직업과 레벨을 출력합니다.
#         print(f"\n[생성 완료] 이름: {name} | 직업: {job} | 레벨: {level}\n")
#         print("-" * 40)
#         print("=== 프로그램을 종료합니다. ===")


def _get_job_choice() -> str:
    """직업을 선택받고 검증하는 전담 함수"""
    print("\n[직업 목록]\n1. 전사\n2. 마법사\n3. 궁수")
    while True:
        # 수정: 입력받은 즉시 match-case로 검증하여 임시 변수 제거
        match input("직업 번호 선택: ").strip():
            case "1": return "전사"
            case "2": return "마법사"
            case "3": return "궁수"
            case _: print("❌ 올바른 직업 번호가 아닙니다. 직업을 다시 선택하세요.\n")


def _get_level_input() -> int:
    """레벨을 입력받고 검증하는 전담 함수"""
    while True:
        level_input: str = input("레벨을 입력하세요: ").strip()
        
        if not level_input.isdigit():
            print("❌ 올바른 숫자로 레벨을 입력해주세요.\n")
            continue
            
        level = int(level_input)
        if level < 1:
            print("❌ 레벨은 1 이상이어야 합니다. 다시 입력해주세요.\n")
            continue
            
        return level # 수정: 조건 만족 시 즉시 int 반환하며 루프 탈출


def start_rpg_character_creator() -> tuple[dict[str, str | int], ...]:
    print("=== 프로그램을 실행합니다. ===")
    character_list: list[dict[str, str | int]] = []

    while True:
        name: str = input("이름을 입력하세요 (종료하려면 'q' 입력): ").strip()
        if name.lower() == 'q':
            break

        # 수정: 내부 while 루프들을 별도 함수로 위임하여 메인 흐름 단순화
        job = _get_job_choice()
        level = _get_level_input()

        print(f"\n[생성 성공] 이름: {name} | 직업: {job} | 레벨: {level}\n" + "-" * 40)
        character_list.append({"name": name, "job": job, "level": level})

    print("\n=== 프로그램을 종료합니다. ===")
    return tuple(character_list)


# 실행 및 출력
if __name__ == "__main__":
    created_characters = start_rpg_character_creator()
    print(f"\n✨ 최종 생성된 캐릭터 목록 (총 {len(created_characters)}명):")
    for char in created_characters:
        print(f"- {char['name']} ({char['job']}, Lv.{char['level']})")
