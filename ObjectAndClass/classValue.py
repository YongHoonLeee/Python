class Person(object):
    kind = 'human'
    def __init__(self,name):
        self.name = name
    def who_are_you(self):
        print(self.name , self.kind)

a= Person('A')
b = Person('B')
print(id(a.kind) ,id( b.kind)) # 주소를 보면 같은 곳임. 공유한다는거임
# 근데 이게 리스트 같은경우엔 문제가 생김
a.who_are_you()
b.who_are_you()

print("#############")

class T(object):
    words=[] # 빈 리스트 생성. (근데 이게 공유됨)

    def add_word(self,word):
        self.words.append(word)

c =T()
d = T()

print(c.words) 
# d의 words 에 wow 추가.
d.add_word('wow') 
#근데 c 의 words 에서 wow가 추가됨 ㅇㅇ 이건 문제가 있움.
print(c.words)
