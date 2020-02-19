import string
#text file 불러와서 조작하기 신기.
with open('FileSystem/email_format.txt') as f:
    t = string.Template(f.read())
result = t.substitute(name ="yonghoon",contents='How are you today?')
print(result)

print("##################")
# 원본이 훼손되지 않으니 좋다.
# 신기하네..

d = { 'yonghoon':'good morning',
        'kimkiju':'go Doksesil'}
#print(d,type(d))

for i in d:
    print(t.substitute(name =i,contents =d[i]))
    print("################")