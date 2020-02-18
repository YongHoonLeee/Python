def soultion(s):
    return s.lower().count('p') == s.lower().count('y')

#와.. 
# .lower() 로 소문자 만들고,
# . count('w') 로 숫자를 얻어버리네...
print( soultion('ppyy'))
print( soultion('ppy'))

print('ppy'.lower().count('p'))
######################################### 내풀이###
from collections import defaultdict

def solution(s):
    ss = s.lower()
    g ={}
    g =defaultdict(int)
    for w in ss:
        g[w]+=1
    print(g['p'],g['y'])
    if g['p']==g['y']:
        return True
    else:
        return False
