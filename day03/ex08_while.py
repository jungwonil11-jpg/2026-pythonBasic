# while 문
# 초기식
# while 조건식:
#   조건식이 참일때 실행할 문장
#   조건식이 참일때 실행할 문장
#   증감식
from email.headerregistry import Address

# 1-10까지 출력
i = 1
while i <= 10:
    print(f'{i}', end=' ')
    i += 1

print()

# 1-10까지 짝수 출력
i = 1
while i <= 10:
    if i % 2 == 0:
        print(f'{i}', end=' ')
    i += 1

print()

prompt = """""
1. Add
2. Del
3. List
4. Quit

Enter your choice: """

cnt = 0
while cnt != 4:
    print(prompt)
    cnt = int(input())
    print(f"당신의 선택 : {cnt}")

print("수고하셨습니다.")