# 입출력
import datetime # 날짜 모듈 가져옴

birth_year = 1997 # int(input('출생년도를 입력하세요 > ')) # 키보드 입력(무조건 string) > int()로 형변환 필요

print(f'당신의 출생년도는 {birth_year}년 입니다') # 콘솔출력
curr_year = datetime.datetime.now().year
# print(curr_year)
age = curr_year - birth_year
print(f'당신의 나이는 {age}세 입니다')

a = 123
a = [3, 6, 9]
print(a)

print('Life' 'is' 'short')
print('Life' + 'is' + 'short') # 위와 동일
print('Life', 'is', 'short') # 일반적
print('Life', 3.141592, True)

print(range(10))
print(len(range(10)))

for i in range(10):
    if i == (len(range(10)) - 1):
        print(i, end='\n') # 엔터를 없앨때 씀
    else:
        print(i, end=', ')

print('Life', 'is', 'short', sep='&') # 각 단어 연결 구분자 seq, 별로 안쓰임

pi = 3.14159265359

print(f'PI = {pi:.4f}') #format string
