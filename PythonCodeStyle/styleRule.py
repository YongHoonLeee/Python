"""
    Python Coding Style ...
"""
# import 는 맨 첫줄에 ! 그리고 import 하고나서 2줄 띄우기
import os


def main():
    # TODO(YongHoon) 이런식으로 내가 만들었다고 확인할 사항을 메모한다.
    """이런식으로 함수를 설명한다.
    """
    good = os.path.isfile('test.txt')
    print(good)
# 함수와 함수사이엔 2줄을 띄운다.


if __name__ == '__main__':
    main()

# 일단 잘 모르겠고 밑에 에러뜬대로 고치다 보면 나아질듯. 넘 많다.
