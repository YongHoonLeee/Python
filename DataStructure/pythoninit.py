# 8
# 타 언어와 다르게 타입 지정을 안해줘도 된다.
num =1
name ="YongHoon"

print(num,type(num))
print(name,type(name))

num = name
# 그냥 간단하게 형변환도 된다. (사용하는데 주의해야될듯)
print(num,type(num))


#9
# sep 와 end

print('Hi','YongHoon')
print('Sep','end',sep=',',end='.\n')

#10
# import math
import math

x = 1
print (x)

#문자열. 상당히 다루기 쉽다.

print('Py'+'thon')
print("""hello
word""")

print('hi' ' ''mike')

#문자열 슬라이스

word = 'Python'
print(word[1])
print(word[2:])
#문자열 안에 대입이 안되서 바꾼거랑 원래꺼를 잘라서 붙여준다. 신기.
word = 'J'+word[1:]
print(word)
#문자열 매소드도 많다.

name = "My name is Y H"
test = name.find('Y')
print(test,type(test))

isstart = name.startswith('My')
print(isstart)

cnt = name.count('n')
print(cnt)
print("################")
name.replace("My","Hi")
print(name)

new_name =name.replace('name','wow')
print(new_name)

wow = "hello {} {} {}"
new_wow = wow.format('yong', 'hoon','good')
print(new_wow)