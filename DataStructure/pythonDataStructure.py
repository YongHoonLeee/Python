l = [1,20,4,50]
# 전체출력.
print(l)

# index 출력가능.

print(l[0])

# index = 음수일경우 뒤에서부터 ㅋㅋ 문제풀때 유용할듯.

print(l[-1])

#  [ : ] 을 이용해서 자르기 가능 .

print(l[0:2])

# len() 으로 길이출력가능.
print(len(l))

#type 은 list

print(type(l))

# 한번에 넣기 가능.
wow = list('abcde"')
print(wow)

# 다양한 기능들.
n = [1,2,3,4,5,6,7,8,9,10]
print(n[::2])
print(n[::3])
print(n[::-1]) # 거꾸로 출력 가능 ; 개좋다..
print("################")
array = [n,wow]
print(array) #리스트안에 리스트들 넣는거 가능 약간 2차원 배열같은 느낌. 

print("##################################")

r = [1,2,3,4,5,1,2,3]
print(r.index(3))
print(r.index(3,4))  # 3을 4번째 자리부터 검색 ㄱ

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)

r.reverse() #원래대로 되돌리기 ; 개사기.
print(r)

s = "My name is yonghoon"
to_split = s.split(' ') # ' ' 공백으로 s 를 나누어서 각 요소를 리스트에 넣음ㅋ
print(to_split) 

x = ' '.join(to_split) # to_splite 의 요소들을 ' '공백을 끼워서 문자열롴
print(x)

print("########################")

i = [1,2,3,4,5]
j =[]
print(i)
print(j)
j.append(100)

print(i)
print(j)

# 둘다 바뀌는 이유가 list 끼리 같다고 하면 참조가 됨. 주소값을 반환.

print(id(i) ,id(j)) # 신기. 그래서 .copy() 함수를 씀.

j.count(i)

print(i)
print(j)
j.count(i)
j.append(100)

print(i)
print(j)


print("######################")
# Tuple 형 .

a = (1,2,3)
print(a)

#a[0] = 5

# 튜플형은 약간 const list 형이라고 생각하면 될듯 나머지는 비슷동일.

# 사전형.
# key ,value 값을 가지므로 c++ 에서 map 과 비슷한듯하다.

# 집합형.

# c++의 set 과 비슷하지만 ,중복 없음 ,자동 정렬.
# 근데 많은 연산자를 지원해서 편할듯 하다. 차집합 교집합 등등
#파이썬 신기.
a = {7,2,2,3,3,4,5,5,6}
print(a)

b = { 2,3,4,9}
print("############")
print(a-b)
print(b-a)
print(a^b)
print(a|b)
print(a&b)

#너무 좋을듯 ㅎ
