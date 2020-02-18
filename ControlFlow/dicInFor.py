w = [ 'mon','tue','wed']
f = ['coffee','milk','water']

d={}

for x,y in zip(w,f):
    d[x] = y

print(d)

d2 = {x:y for x,y in zip(f,w)}

print(d2)

#wow....