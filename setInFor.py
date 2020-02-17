s= set()

for i in range(10):
    s.add(i)
print(s)

s2  = { i for i in range(10) if i%2==0}
s3 = {j for j in range(10) if j%2!=0}

s4 = s2|s3

print(s2)
print(s3)
print(s4)

s5 = s2&s3

print('s5 = ',s5)


#wow....