# Hash lv1 완주하지 못한 선수 (https://programmers.co.kr/learn/courses/30/lessons/42576)
# Hash : O(1) - O(n)
# Hash Collision

# Dictionary : key-value (associative array)

# 1 <= len(participant) <= 100_000
# len(completion) = lens(participant) - 1
# duplicate element

def solution(participant, completion):
    participant.sort() # nlog(n)
    completion.sort() # nlog(n)
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
