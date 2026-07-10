# ## 요구사항

# ```text
# 1. 이름을 입력받습니다.
# 2. 나이를 입력받습니다.
# 3. 관심 있는 기술을 입력받습니다.
# 4. 하루 학습 가능 시간을 입력받습니다.
# 5. 입력받은 값을 변수에 저장합니다.
# 6. 나이는 int로 변환합니다.
# 7. 하루 학습 가능 시간은 float으로 변환합니다.
# 8. type()으로 각 변수의 자료형을 출력합니다.
# 9. f-string으로 자기소개 문장을 출력합니다.
# ```

# ## 예상 실행 흐름

# ```text
# 이름을 입력하세요: Jean
# 나이를 입력하세요: 25
# 관심 기술을 입력하세요: FastAPI
# 하루 학습 가능 시간을 입력하세요: 3.5

# Jean님은 25세입니다.
# 관심 기술은 FastAPI입니다.
# 하루 3.5시간 학습할 수 있습니다.
# ```

# ## 확인 기준

# ```text
# 문자열, 정수, 실수 자료형을 구분했는가?
# input()으로 받은 값을 필요한 자료형으로 변환했는가?
# 출력 문장이 자연스럽게 구성되었는가?
# ```

##################################################################################
print("================================")

print("[입력]")
name : str = input("이름을 입력하세요: ")
age : int = int(input("나이를 입력하세요: "))
interest : str = input("관심 기술을 입력하세요: ")
study_time : float = float(input("하루 학습 가능 시간을 입력하세요: "))

print("[자료형 확인]")
print(f"이름의 타입: {type(name)}")
print(f"나이의 타입: {type(age)}")
print(f"관심 기술의 타입: {type(interest)}")
print(f"하루 학습 시간의 타입: {type(study_time)}")

print("[출력]")
print(f"{name} 님은 {age}세입니다.\n관심 기술은 {interest}입니다.\n하루 {study_time}시간 학습할 수 있습니다.")

# ## 예상 에러 > 예외 상황
# 나이를 입력할 때 숫자가 아닌 문자를 입력하면 ValueError가 발생합니다.
# Traceback (most recent call last):
#   File "C:\aidevs\01_python-git-foundation\01_python-basic\20_assignments\submissions\assignment01_profile.py", line 19, in <module>
#     age : int = int(input("나이를 입력하세요: "))
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'dd'