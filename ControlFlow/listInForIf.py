t = ( 1,2,3,4,5)
t2 = ( 6,7,8,9,10)

r = []
for i in t:
    r.append(i)

print(r)

r2 = [i for i in t2]

print(r2)

r3 = [i*j for i in t for j in t2]

print(r3)

r4 = [ i for i in r3 if i%2==0]

print(r4)

r5 = [i for i in r3 if i%2!=0]

print(r5)

#신기하네...