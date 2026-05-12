# 정렬 : sort
#        주의 사항 : 자료형이 다르면 오류 발생
str = ['a', 'b', 'c', '1', '2', '3', 'A', 'B', '가', 'D']
str.sort()
print(str)
print('-' * 30)


#sort 에서 자료형이 다르면 오류
str = ['a', 'b', 'c', 1,2,3, 'A', 'B', '가', 'D']
str.sort()
print(str)
#정렬할때는 오류
#str.sort()
print('*'*30)

#reverse() : 뒤집기
str = ['a', 'b', 'c', 1,2,3, 'A','B','가','D']
str.reverse()
print(str)

#내림차순(sort + reverse)
str = ['a', 'b', 'c', 1,2,3, 'A','B','가','D']
str.sort()
str.reverse()
print(str)

#리스트 확장 - expend(리스트), 리스트 + 리스트
odd = [1,3,5,7,9]
even = [2,4,6,8,10]
res = odd + even
print(res)
print('*'*50)

#리스트1.expend(리스트2) : 리스트1에 리스트2가 추가


