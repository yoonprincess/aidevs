########### 과제 #############
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


# # 프로그램 실행
# start_rpg_character_creator()


def start_rpg_character_creator() -> tuple[dict[str, str | int], ...]:
    print("=== 프로그램을 실행합니다. ===")
    
    # 수정: 생성된 캐릭터들을 임시로 수집할 리스트 (최종 반환 시 튜플로 변환)
    character_list: list[dict[str, str | int]] = []

    while True:
        # 2. 이름을 입력받습니다. (7. 첫 번째 입력에서 'q'를 입력하면 종료)
        name: str = input("이름을 입력하세요 (종료하려면 'q' 입력): ").strip()
        if name.lower() == 'q':
            break # 바깥쪽 루프를 탈출하여 최종 결과 반환 단계로 이동

        # 3. 직업을 선택합니다.
        print("\n[직업 목록]\n1. 전사\n2. 마법사\n3. 궁수")
        while True:
            job_choice: str = input("직업 번호 선택: ").strip()
            
            match job_choice:
                case "1": job = "전사"; break
                case "2": job = "마법사"; break
                case "3": job = "궁수"; break
                case _:
                    print("❌ 올바른 직업 번호가 아닙니다. 직업을 다시 선택하세요.\n")

        # 4. 레벨을 입력받습니다.
        while True:
            level_input: str = input("레벨을 입력하세요: ").strip()
            
            if not level_input.isdigit():
                print("❌ 올바른 숫자로 레벨을 입력해주세요.\n")
                continue
                
            level = int(level_input)
            
            # 5. 레벨이 1보다 작으면 다시 입력받습니다.
            if level < 1:
                print("❌ 레벨은 1 이상이어야 합니다. 다시 입력해주세요.\n")
                continue
            break  

        # 6. 선택한 직업과 레벨을 출력하고 리스트에 추가합니다.
        print(f"\n[생성 성공] 이름: {name} | 직업: {job} | 레벨: {level}\n")
        print("-" * 40)
        
        # 생성된 캐릭터 정보를 딕셔너리로 묶어서 리스트에 적재
        character_list.append({"name": name, "job": job, "level": level})

    print("\n=== 프로그램을 종료합니다. ===")
    
    # 수정: 수집된 캐릭터 리스트를 불변(Immutable) 객체인 튜플로 변환하여 반환
    return tuple(character_list)


# 출력
# 함수가 최종적으로 캐릭터들이 담긴 튜플을 반환합니다.
created_characters = start_rpg_character_creator()

print(f"\n최종 생성된 캐릭터 목록 (총 {len(created_characters)}명):")
for char in created_characters:
    print(f"- {char['name']} ({char['job']}, Lv.{char['level']})")
