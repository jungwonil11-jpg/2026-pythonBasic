#정수를 실수
num = 27
res = float(num)
print(f"{num=}, {type(num)=}")
print(f"{res=}, {type(res)=}")


#실수를 정수
num = 27.443
res = int(num)
print(f"{num=}, {type(num)=}")
print(f"{res=}, {type(res)=}")
print()

# 소숫점 둘째자리 까지
num = 27.789
print(f"소수점 둘째자리까지 : {num:.2f}")

num = 27.789
print(f"소수점 둘째자리까지 : {num:.2f}")

#일의 자리 버림
num = 124567
result = (num // 10) * 10
print(f"{result:,}")

