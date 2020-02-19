# w mode file create ok 
with open('mode.txt','w')as f:
    f.write('wite mode')


# w+ mode file overwrite ok
with open('mode.txt','w+') as g:
    g.write('w+ mode')

print("#####")

# r mode no file error
with open('mode.txt','r') as f:
    # location .tell
    print(f.tell())
    line =f.readline()
    print(line)
    f.seek(1)
    print(f.read())

print("#####")

# r+ mode overwrite
with open ('mode.txt','r+') as f:
    f.write('r+')

with open( 'mode.txt','a') as f:
    f.write('\nappend mode')





