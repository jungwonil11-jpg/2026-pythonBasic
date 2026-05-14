# 다중 if문
# if 조건식1:
#   조건식1이 참일때 실행할 문장
#   조건식1이 참일때 실행할 문장
# elif 조건식2:
#   조건식1이 거짓이면서 조건식2이 참일때 실행할 문장
#   조건식1이 거짓이면서 조건식2이 참일때 실행할 문장
# elif 조건식3:
#   조건식1,2이 거짓이면서 조건식3이 참일때 실행할 문장
#   조건식1,2이 거짓이면서 조건식3이 참일때 실행할 문장
# [else:
#   조건식1,2,3 모두 거짓일때 실행 (나머지)
# ]

# 이름, 국어, 영어, 수학, 점수 받아서 총점, 평균(소숫점 첫째자리까지), 학점을 구하자

name = input("이름: ")
kor = int(input("국어: "))
eng = int(input("영어: "))
math = int(input("수학: "))

total = kor + eng + math
avg = round(total / 3, 1)

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{name}의 총점: {total}, 평균: {avg}, 학점: {grade}")