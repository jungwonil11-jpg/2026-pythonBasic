# 숫자형(Number)
# 정수(int), 실수(float), 복소수(complex)

#1. 정수
age = 18
print(f"{age=}, type={type(age)}")

#2. 실수
weight = 72.14
print(f"{weight=}, type={type(weight)}")

#3. 복소수
num = 415 + 34j
print(f"{num=}, type={type(num)}")

# 실수부분
print(f"{num.real=}, type={type(num.real)}")

# 허수부분
print(f"{num.imag=}, type={type(num.imag)}")

# 4. 지수 표현
height = 1.817e2 #1.817 * 10^2
print(f"{height=}, type={type(height)}")

height = 1.817e5 #1.817 * 10^5
print(f"{height=: ,}, type={type(height)}")

#5. 8진수(0o숫자)
num1 = 0o11
print(f"{num1=}, type={type(num1)}")

#6. 16진수(0x숫자)
num2 = 0x11
print(f"{num2=}, type={type(num2)}")





