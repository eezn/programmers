def check_sort(participant, completion):
    participant.sort()
    completion.sort()

    print()
    print(participant)
    print(completion)
    print("participant[-1]:", participant[-1])
    

participant_1 = ['leo', 'kiki', 'eden']
completion_1 = ['eden', 'kiki']

participant_2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion_2 = ['marina', 'josipa', 'nikola', 'filipa']

participant_3 = ['mislav', 'stanko', 'mislav', 'ana']
completion_3 = ['stanko', 'ana', 'mislav']


if __name__ == "__main__":
    check_sort(participant_1, completion_1)
    check_sort(participant_2, completion_2)
    check_sort(participant_3, completion_3)