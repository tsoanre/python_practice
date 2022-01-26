import random

list_participant = []

print("Note:- If participant names completed please press Enter")

secret_santa_participant = input("Enter participant name :-\n").split(' ')

for participant in secret_santa_participant:
    list_participant.append(participant)

list_santa = list_participant.copy()

def secret_santa(list_santa,list_participant):
    random.shuffle(list_participant)

    for participant in range(len(list_participant)):
        for santa in range(len(list_santa)):
            if list_participant[participant] == list_santa[santa]:
                random.shuffle(list_participant)
                random.shuffle(list_santa)

    combine_list = zip(list_participant,list_santa)
    the_secret = list(combine_list)

    return print(the_secret)

print("Your secret santa pairings are (Santa, Gift Receiver): ")

secret_santa(list_santa,list_participant)