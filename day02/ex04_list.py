#list : [항목, 항목, 항목, 항목]
#        가변형 => 수정 가능, 삽입, 추가, 삭제도 가능

odd = [1, 3, 5, 7, 9]
str = ["hi", "bye", 'good']

person = ["홍길동", 24, 178.45, 'A', True]
print(odd, type(odd))
print(person, type(person))
print('*'*30)

#list의 인덱싱, 슬라이싱 가능
print(odd[3]), type(odd[3])
print(person[3], type(person[3]))
print('*'*30)

print(odd[:3], type(odd[:3]))
print(odd[2:4], type(odd[2:4]))
print(odd[-3:-2], type(odd[-3:2]))

even = [2,4,odd,8,10]
print(even, type(even))

# even 안에 있는 8 호출
print(even[4])
print(even[-2])

# even 안에 있는 7 호출
print(even[2][3])

person = ["홍길동", 24, 178.45, 'A', True]

# 홍길동
print(person[0], type(person[0]))
#길
print(persion[0][1], type(person[0][1]))

