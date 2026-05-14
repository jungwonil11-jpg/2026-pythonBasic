# if ~ else
# if 조건식:
#   조건식이 참일때 실행할 문장
#   조건식이 참일때 실행할 문장
#   조건식이 참일때 실행할 문장
# else:
#   조건식이 거짓일때 실행할 문장
#   조건식이 거짓일때 실행할 문장
#   조건식이 거짓일때 실행할 문장

# 받은 점수가 80 이상이면 합격, 아니면 불합격
# su1 = (int)(input('입력하세요>>> '))
# if (su1 >= 80):
#     print("합격")
# else:
#     print("불합격")
#
# # 받은 숫자가 홀수인지, 짝수인지 판별하자
# su2 = int(input('홀짝감별기>>> '))
# if (su2%2== 0):
#     print("짝수")
# else:
#     print("홀수")

# 항목 in 리스트, 튜플, 문자열 => 항목이 존재하면 True, 존재하지 않으면 False
# 항목 not in 리스트, 튜플, 문자열 => 항목이 존재하면 True, 존재하지 않으면 False
print (1 in [1,3,5,7,9]) # True
print (1 not in (1,3,5,7,9)) # False

pocket = ['phone', 'money', 'paper']
if('money' in pocket):
    print("택시 타고 가자")
else:
    print("뛰어가자")

#pass : 아무런 일도 하지 않도록 설정할때 사용하는 예약어
pocket = ['phone', 'money', 'paper']
if('money' in pocket):
    pass
else:
    print("뛰어가자")

#조건부 표현식 : 변수 = 참인경우 if 조건식 else 거짓인 경우
#보통 간단한 계산식일때 사용
str = "택시 타고 가자" if('money' in pocket) else "뛰어가자"
print(str)

