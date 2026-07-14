r"""JSON 파일을 안전하게 읽는 예제입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\02_exception-debugging\03_read_json_safely.py

이 예제의 목표:
    1. JSON 파일을 읽습니다.
    2. 파일이 없을 때의 오류를 처리합니다.
    3. JSON 문법이 깨졌을 때의 오류를 처리합니다.
"""

import json
import logging
from pathlib import Path

# 실무에서는 print 대신 체계적인 추적을 위해 logging 라이브러리를 사용합니다.
logger = logging.getLogger("DataLogger")

CURRENT_DIR = Path(__file__).parent

def read_json_safely(file_name: str) -> dict:
    """JSON 파일을 읽고 dict로 반환합니다.

    오류가 나면 프로그램을 바로 종료하지 않고 빈 dict를 반환합니다.
    """

    # 1. 예외 방어: 입력받은 파일명이 문자열이 아니거나 비어있을 때 즉시 예방
    if not isinstance(file_name, str) or not file_name.strip():
        logger.error(f"유효하지 않은 파일 이름 형식입니다: {type(file_name)}")
        return {}

    # Path 객체의 / 연산자를 사용해 운영체제 호환성이 확보된 절대 경로 생성
    file_path = CURRENT_DIR / file_name

    try:
        # text = file_path.read_text(encoding="utf-8")

        # # JSON 파일을 dict로 변경
        # return json.loads(text)
    
        # 2. 예외 방어: 빈 파일인 경우 read_text()는 성공하지만 JSON 파서가 터지므로 사전 체크
        if file_path.is_file() and file_path.stat().st_size == 0:
            logger.warning(f"파일이 비어 있습니다: {file_path}")
            return {}
        
        return json.loads(file_path.read_text(encoding="utf-8"))
    
    except FileNotFoundError:
        # print(f"파일을 찾을 수 없습니다: {file_path}")
        # return {}
        logger.error(f"파일이 경로에 존재하지 않습니다: {file_path}")
    except PermissionError:
        # 추가 예외: 파일이 읽기 전용이거나 권한이 없을 때 (서버 환경에서 빈번히 발생)
        logger.error(f"파일 읽기 권한이 없습니다: {file_path}")
    except json.JSONDecodeError as error:
        # print(f"JSON 문법이 올바르지 않습니다: {file_path}")
        # print("오류 위치:", error)
        # return {}
        logger.error(f"JSON 문법 오류 발생: {file_path} (위치: 행 {error.lineno}, 열 {error.colno})")
    except Exception as error:
        # 4. 최종 방어선: OS 가상 메모리 부족, 하드웨어 I/O 장애 등 예측 불가능한 시스템 에러 감지
        logger.critical(f"예상치 못한 치명적인 시스템 오류 발생: {type(error).__name__} - {error}")

    return{}


def main() -> None:
    # 테스트용 파일 목록 [정상 파일, 없는 파일, 문법 에러 파일]
    file_names = ["config.json", "missing.json", "broken_config.json"]

    for file_name in file_names:
        print(f"\n📂 [파일 읽기 시도] : {file_name}")
        print(f"   ➡️ [최종 반환 결과]: {read_json_safely(file_name)}")


if __name__ == "__main__":
    main()