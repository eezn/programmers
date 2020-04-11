# Hash lv1 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    element_count = {}
    # participant.sort()
    # completion.sort()

    if len(list(set(participant))) == len(participant): 
        answer = list(set.difference(set(participant), set(completion))).pop()
    else: 
        for person in participant: 
            try: element_count[person] += 1
            except: element_count[person] = 1
            if element_count[person] == 2:
                answer = person

    return answer