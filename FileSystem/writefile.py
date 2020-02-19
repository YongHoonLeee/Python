#file open  ,   'w' =write
# f= open('test.txt','w')
# f.write('hello yonghoon')
# f.write('\n')
# print('wow jonjam',file=f)
# f.close()

#with open , 'a' = append

# with open('test.txt','a') as f:
#     for i in range(5):
#         f.write('with open good')

#auto close()

# with open('test.txt','r') as f:
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

# 2개씩 끊어서 읽어서 처리 ~
# with open('test.txt','r') as g:
#     while True:
#         chunk =2
#         flip = g.read(chunk)
#         print(flip)
#         if not flip:
#             break

# seek 로 이동하기

with open('test.txt','r') as f:
    print(f.tell()) #현재위치 0
    print(f.read(1))
    f.seek(1)
    print(f.read(2))
    f.seek(2)
    print(f.read())
    #2번째부터 전체 읽기도 됨.
