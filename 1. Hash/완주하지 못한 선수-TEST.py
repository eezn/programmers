def check_sort(participant, completion):
    participant.sort()
    completion.sort()

    print()
    print(participant)
    print(completion)
    print("participant[-1]:", participant[-1])

def check_zip(participant, completion):
    print()
    for k, v in zip(participant, completion):
        print(k, v)
    

participant_1 = ['leo', 'kiki', 'eden']
completion_1 = ['eden', 'kiki']

participant_2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion_2 = ['josipa', 'filipa', 'marina', 'nikola']

participant_3 = ['mislav', 'stanko', 'mislav', 'ana']
completion_3 = ['stanko', 'ana', 'mislav']


check_sort(participant_1, completion_1)
check_sort(participant_2, completion_2)
check_sort(participant_3, completion_3)   

check_zip(participant_1, completion_1)
check_zip(participant_2, completion_2)
check_zip(participant_3, completion_3)