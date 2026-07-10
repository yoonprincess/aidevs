import sys

print("=============================================")

input_data = "카드아님"

# if (input_data not in ["카드1", "카드2"]):
if (input_data != "카드1" and input_data != "카드2"):
    print("❌ 카드가 아닙니다. 다시 시도해 주세요.")
    print("================== 강제 종료 =======================")
    sys.exit()

if (input_data == "카드1"):
    print("✅ 카드1 업무 진행")
elif (input_data == "카드2"):
    print("✅ 카드2 업무 진행")

print("=============================================")
