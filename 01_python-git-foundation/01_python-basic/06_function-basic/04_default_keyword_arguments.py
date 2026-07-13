"""기본값 매개변수와 키워드 인자 예제입니다.

기본값 매개변수:
    함수를 호출할 때 값을 넣지 않으면 미리 정한 기본값을 사용합니다.

키워드 인자:
    함수 호출 시 매개변수 이름을 직접 적어 값을 전달합니다.
    값의 의미가 더 분명해집니다.
"""

# 수정: name과 language는 문자열(str)을 받고, 최종적으로 문자열(str)을 반환함을 명시
def greet(name: str, language="ko") -> str:
    if language == "ko":
        return f"{name}님, 안녕하세요."

    if language == "en":
        return f"Hello, {name}."

    return f"{name}, 지원하지 않는 언어입니다."


print(greet("Jean"))
print(greet("Jean", "en"))

# 키워드 인자를 사용하면 순서를 헷갈릴 가능성이 줄어듭니다.
print(greet(name="Mina", language="ko"))
print(greet(language="en", name="Mina"))


"""
함수명: create_user
매개변수: name, role, active
기본값: role="member", active=True
사용자 정보를 넣으면 dict 형태로 변환합니다.
"""
# 수정: 반환하는 딕셔너리의 key는 문자열(str)이고, 
# value에는 Union 기호(|)를 사용해 'str | bool'로 정확히 명시
def create_user(name: str, role: str="member", active: bool=True) -> dict[str, str | bool]:
    return {
        "name": name,
        "role": role,
        "active": active,
    }

# 수정: 생성된 각 유저 변수에도 동일한 딕셔너리 타입 선언 적용
user1: dict[str, str | bool] = create_user("Jean")
user2: dict[str, str | bool] = create_user("Admin", role="admin")
user3: dict[str, str | bool] = create_user("Guest", active=False)

print(user1)
print(user2)
print(user3)
