def main():

    s = 'woeiawawefaweiufhaweffiulwaefwaefpawef'
    d={}

    #for c in s:
    #    d[c]+=1

    print(d)

    for c in s:
        if c not in d:
            d[c] =0
        d[c] +=1

    print(sorted(d,key=d.get,reverse=True))


    from collections import defaultdict

    g ={}
    g =defaultdict(int)

    for w in s:
        g[w]+=1

    print(sorted(g))

    from termcolor import colored

    print('test')
    print(colored('test','red'))
    print (colored('leeyonghoon','yellow'))
    print(__name__)

if __name__ == '__main__':  # 지렸다... 넘 재밋다.
    main()
