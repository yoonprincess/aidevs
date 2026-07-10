# import sys

# print("==============================================")

# while True:
#     print("Menu start")
#     cmd = input("Input cmd: ")
#     print(f"입력하신 정보는 {cmd}")

#     if cmd == "q":
#         print("Bye...")
#         sys.exit()

# # '도달 불가능한 코드(Unreachable Code)'입니다.
# # while True에서 무한 루프를 돌고 있기 때문에 아래 코드는 절대 실행되지 않습니다.
# print("==============================================")


######################################################
# 마지막 구문까지 출력하고 싶다면
import sys

print("==============================================")

while True:
    print("Menu start")
    cmd = input("Input cmd: ")
    print(f"입력하신 정보는 {cmd}")

    if cmd == "q":
        print("Bye...")
        # sys.exit()
        break  # sys.exit() 대신 break를 사용해 무한 루프만 안전하게 탈출

# 이제 프로세스가 종료되지 않고 자연스럽게 아래로 내려와 정상 실행됩니다.
print("==============================================")
