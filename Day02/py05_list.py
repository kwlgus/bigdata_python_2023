# 리스트 계속

a = [1, 2, 3]
print(a)

# 자료구조 stack에 있는 pop 기능 구현
print(a.pop()) # 리스트 맨 마지막 요소를 꺼내라
print(a) # 1,2만 남아있음

a.append(10) # 10 넣기
print(a)

print(a.count(3)) # list안에 해당값이 몇개 있는지 확인

# 리스트 확장 a = 1, 2, 10
a.extend([5, 3, 2])
print(a)

print(a.count(2))
