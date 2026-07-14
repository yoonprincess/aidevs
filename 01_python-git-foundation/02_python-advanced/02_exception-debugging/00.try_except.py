def safe_processor(data_dict: dict, file_name: str) -> None:
    """전달받은 딕셔너리와 파일명을 안전하게 처리하는 함수"""
    try:
        # 1. KeyError 예방 (기본값 20)
        age = data_dict.get("age", 20)
        
        # 2. ValueError / TypeError 발생 가능 구역
        print(f"내년 나이: {int(age) + 1}")
        
        # 3. FileNotFoundError 발생 가능 구역
        with open(file_name, "r", encoding="utf-8") as f:
            print(f"파일 내용: {f.read().strip()}")
            
    except ValueError:
        print("❌ 에러: 숫자로 변환할 수 없는 값입니다.")
    except FileNotFoundError:
        print(f"❌ 에러: '{file_name}' 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"💥 예상치 못한 에러 발생: {type(e).__name__} - {e}")


def main() -> None:
    # 주석: 테스트를 위한 임시 파일 생성 (with 문을 사용해 즉시 닫기)
    with open("temp_profile.txt", "w", encoding="utf-8") as f:
        f.write("안녕하세요! 개발자 김프로의 프로필 파일입니다.")

    # 주석: 상황별 데이터 매개변수 정의 (직관적인 딕셔너리 리스트 구조)
    test_cases = [
        {
            "desc": "1. 모든 데이터가 정상인 경우",
            "data": {"age": "28"},
            "file": "temp_profile.txt"
        },
        {
            "desc": "2. age 키가 없어서 기본값(20)이 적용되는 경우 (KeyError 예방)",
            "data": {"name": "kim"},
            "file": "temp_profile.txt"
        },
        {
            "desc": "3. age에 숫자가 아닌 값이 들어온 경우 (ValueError 발생)",
            "data": {"age": "twenty-eight"},
            "file": "temp_profile.txt"
        },
        {
            "desc": "4. 존재하지 않는 파일명을 넘긴 경우 (FileNotFoundError 발생)",
            "data": {"age": "28"},
            "file": "not_exist_file.txt"
        },
        {
            "desc": "5. 리스트가 전달되어 int 변환이 불가능한 경우 (Exception 최종 방어선 작동)",
            "data": {"age": [10, 20]},
            "file": "temp_profile.txt"
        }
    ]

    # 주석: 각 테스트 케이스를 순회하며 함수 실행
    for case in test_cases:
        print(f"\n--- {case['desc']} ---")
        safe_processor(case["data"], case["file"])


if __name__ == "__main__":
    main()