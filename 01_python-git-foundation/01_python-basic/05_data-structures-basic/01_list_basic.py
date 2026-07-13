"""list 기초 예제입니다.

list는 여러 값을 순서대로 저장하는 자료구조입니다.

특징:
1. 순서가 있습니다.
2. 값을 추가, 수정, 삭제할 수 있습니다.
3. 같은 값이 여러 번 들어갈 수 있습니다.

실제 백엔드 개발에서는 사용자 목록, 게시글 목록, 대화 메시지 목록처럼
여러 개의 데이터를 순서대로 다룰 때 list를 자주 사용합니다.
"""

# 대괄호 [ ]를 사용해 list를 만듭니다.
todos = ["Python 설치", "변수 연습", "조건문 연습"]
todos : list[str] = ["Python 설치", "변수 연습", "조건문 연습"]

temp : list = [1, 2, 3, True, "문자열", [1, 2, 3]]    # 가능하긴 함
temp : list[object] = [1, 2, 3, True, "문자열", [1, 2, 3]]

print("처음 할 일 목록:", todos)
print("자료형:", type(todos))
print("temp:", temp)
print("자료형:", type(temp))
print("--------------------------------------")

# append()는 list의 끝에 새 값을 추가합니다.
todos.append("반복문 연습")
print("append 후:", todos)
print("--------------------------------------")

# insert()는 list의 특정 위치에 새 값을 추가합니다.
todos.insert(1, "1")
print("insert 후:", todos)
print("--------------------------------------")

# list는 순서가 있으므로 번호(index)로 값을 꺼낼 수 있습니다.
# Python의 index는 0부터 시작합니다.
print("첫 번째 할 일:", todos[0])
print("두 번째 할 일:", todos[1])

todos.index("1")    # 1이라는 값이 들어 있는 index를 반환합니다.
print("1의 index:", todos.index("1"))   # 1
print("--------------------------------------")

# list의 값은 수정할 수 있습니다.
todos[1] = "xxxxxxxx"
print("수정 후:", todos)
print("--------------------------------------")

# pop()은 마지막 값을 꺼내면서 list에서 제거합니다.
last_todo = todos.pop()
print("꺼낸 값:", last_todo)
print("pop 후:", todos)
print("--------------------------------------")

# len()은 list 안에 들어 있는 값의 개수를 알려줍니다.
print("할 일 개수:", len(todos))

# for 반복문으로 list 값을 하나씩 꺼낼 수 있습니다.
print("\n[할 일 목록 출력]")
for todo in todos:
    print("-", todo)

# enumerate()를 사용하면 번호와 값을 함께 꺼낼 수 있습니다.
print("\n[번호가 있는 할 일 목록]")
for index, todo in enumerate(todos, start=1, step=2):
    print(index, todo)
