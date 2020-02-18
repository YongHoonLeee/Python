def g():
    for i in range(10):
        yield i

g = g()

print(type(g))
print(next(g))
print("#######")
for i in range(5):
    print(next(g))

# 신기하군. 
g2 = (i for i in range(10)) # tuple 안쓰면 제너레이터
g3 = tuple(i for i in range(10)) # 써줘야 튜플형.

print(type(g2),type(g3))

#진귀하군.

