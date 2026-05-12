#문자열(str):큰 따옴표, 작은 따옴표 모두 사용 가능
#여러줄 일때는 ''' 내용 ''', """ 내용 """
# 주요 연산자 : + (연결) , *(반복) , in(포함여부), not in(미포함 여부)

str = '헬로 python'
print(str, type(str))


str = "헬로 python"
print(str, type(str))


str = "Im Ok !!"
print(str, type(str))


str = 'Im Ok !!'
print(str, type(str))

#이스케이프 문자(리터럴 문자) : \n(줄바꿈), \t(탭) \"("), \'(')
# {'name' : 'hong'}
str = "{\'name\' : \'hong\'}"
print(str)

str = "{'name' : 'hong'}"
print(str, type(str))

str = "@"
print(str + str)

print(str * 5)


