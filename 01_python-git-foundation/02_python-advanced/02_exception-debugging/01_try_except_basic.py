r"""try/except 기본 예제입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\02_exception-debugging\01_try_except_basic.py

이 예제의 목표:
    문자열을 숫자로 바꿀 때 발생할 수 있는 ValueError를 처리합니다.
"""


def to_int_or_default(value: str, default: int = 0) -> int:
    """문자열을 int로 바꾸고, 실패하면 기본값을 반환합니다."""

    print("\n[to_int_or_default] 함수 실행")
    print(f"입력 값: {value} | 자료형: {type(value)}")

    try:
        return int(value)
    except ValueError:
        print(f"'❌ {value}'는 숫자로 바꿀 수 없습니다. 기본값 {default}을 사용합니다.")
        return default

def divided(num1: int, num2: int) -> float | None:
    """두 숫자를 나누고, 에러 발생 시 에러 메시지를 출력한 뒤 None을 반환합니다."""
    try:
        return num1 / num2
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return None

def main() -> None:
    """ to_int_or_default 함수 테스트 """
    values = ["10", "abc", "30"]

    for value in values:
        number = to_int_or_default(value)
        print(f"변환 결과: {number} | 자료형: {type(number)}")

    """ divided 함수 테스트 """
    print(divided(10, 0))
    print(divided("10", "2"))
    print(divided(10, 2))

main()


