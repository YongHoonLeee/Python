def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    answer.sort()

    if len(answer) == 0:
        answer.append(-1)

    return answer

###
# 이게 진짜 혁명적 ; 근데 가독성이 별로
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

###
#리스트 내부에서 반복문 처리하는거 좋다.
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]

