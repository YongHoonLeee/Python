import dbm

# 간단한 디비 할때 ㅇㅇ 문자열밖에 안됨 정수형 안됨.
with dbm.open('cache', 'c') as db:
    db['1'] = 'yonghoon'
    db['2'] = 'woowowo'

with dbm.open('cache','r') as db:
    print(db.get('1'))