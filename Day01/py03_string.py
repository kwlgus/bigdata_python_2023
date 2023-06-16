# 문자열

value = "Hello World"
print(value)
print('Hello World')

print('저는 "김지현"입니다')
print("저는 '김지현'입니다")

value = '''
안녕하세요.
저는 프로그래머입니다.
프로그래밍 합니다.
''' # 여러줄 문장

print(value)

'''
얘는 여러줄 주석으로 대체합니다.
파이썬에는 여러줄 주석이 없어서 
여러줄 문자열로 이역할을 대신합니다.
'''

print('Hello' + ' World!') # (* 문자열 안됨)
print('Hello' * 4) # Hello를 3번 반복하라 (+ 숫자는 안됨)

print(len('Life is short')) # 13자리
print(len('인생은 짧아요.')) # 8자리

origin = 'Life is short, You need python'
print(origin[13])
print(origin[0] + origin[16] + 
      origin[19] + origin[20] + 
      origin[0].lower() + origin[15].lower())
print(origin[0:4]) # == print(origin[:4])
print(origin[8:13])