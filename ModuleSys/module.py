from lesson_package import utiles

r= utiles.say_hello('yonghoon')

print (r)

#import lesson_package.utiles 도 되고
#from lesoon_package import utiles 로 모듈만 도 되고
#from lesson_package.utiles import say_hello
#처럼 함수만 불러와도 되는데

# 어느 모듈에서 왔는지 모르니까 알아 볼 수 있도록
#두번째를 잘 쓰자. 그리고 너무 길어지면 'as' 를
# 써서 별칭을 쓰자.

from lesson_package import utiles as u
g= u.say_hello('잠온다')

print(g)
# 파이썬은 절때 경로를 쓰자.
# 상대경로 예시만.
# from . 은 현재 디렉토리
# from .. 은 한단계 윗 . 늘어날수록 위로.

from lesson_package.talk import human

human.cry()
human.sing()