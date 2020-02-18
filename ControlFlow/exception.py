l = [1,2,3]
i = 5

#l[i]

#이러면 IndexError 남.

try:
    l[2]
except:
    print("wow Error~~ ;)") #에러 났을땡

else :
    print("Done ~ ") #에러 안났을때

finally :
    print("죽어도 출력하겠어.") #이건 에러나도 출력ㅋ
    #핵간지..

