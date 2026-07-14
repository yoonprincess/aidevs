
def build_chat_response(request_data: dict) -> dict:
    """질문 dict를 받아 응답 dict를 만듭니다.

    request_data 예시:
        {
            "user": "kim",
            "message": "FastAPI란?",
            "model": "practice-model"
        }
    """
    # dict.get(key, default)
    # > key: 딕셔너리에서 찾고 싶은 Key(키)입니다.
    # > default: 만약 딕셔너리에 그 키가 존재하지 않을 때 대신 반환할 기본값입니다.

    user = request_data.get("user", "anonymous")
    message = request_data.get("message", "").strip()
    model = request_data.get("model", "practice-model")
    # user = request_data["user"]
    # message = request_data["message"]
    # model = request_data["model"]

    return {
        "user": user,
        "message": message,
        "model": model,
        "answer": f"{user}님, '{message}'에 대한 연습용 답변입니다.",
    }
