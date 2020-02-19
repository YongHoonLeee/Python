def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]

participant=['lee','yong','hoon']
completion = ['yong','hoon']

print(solution(participant,completion))

# 효율성 0점임 시간복잡도 고려해서 다시풀기.