l = ['good morning', 'good afternoon' , 'good night']

for i in l:
    print(i)

def greeting():
    yield 'good lee'
    yield 'good yong'
    yield 'good hoon'

print("################")
for g in greeting():
    print(g)
print("################")
g = greeting()
print(next(g))
print("wow")
print(next(g))
print("woooow")
print (next(g))
print(next(g))

# 제너레이터는 반복처리를 하는데 한 요소씩 빼서 쓰는것
# 반복 중간중간 다른 걸 할 수 있다.
#선입 선출 ㅇㅇ
