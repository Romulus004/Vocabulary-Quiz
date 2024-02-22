#The first elements are for questioning.
#The last elements in the lists are right answers. 
A = ['commotion', 'turmoil', 'diplomacy', 'poor imitation',  'inspiration', 'turmoil']
B = ['giggle', 'laugh nervously', 'laugh loudly', 'complain quietly',  'make a half smile', 'laugh nervously']
C = ['murmur', 'run a fast', 'walk slowly', 'whisper',  'yell', 'whisper']
D = ['stereotype', 'unfair belief', 'vague impression', 'definite fact',  'original approach', 'unfair belief']
E = ['aisle', 'settlement', 'cliff', 'pond',  'passage', 'passage']
F = ['merit', 'attempt', 'deserve', 'spend', 'believe',  'deserve']
# putting all the questions in one set for easier looping.
universal_set = [A, B, C, D, E, F]

def ask_question(X):
    print(f'The synonym for \'{X[0].capitalize()}\' is: \n* {X[1].capitalize()} \n* {X[2].capitalize()} \n* {X[3].capitalize()} \n* {X[4].capitalize()}')
    user_input = input('Input your answer: ')

    if user_input.capitalize() == X[-1].capitalize():    
        print(f"Your answer is correct!\n")
        return 1 #To add one when the user is correct.
    else:
        print(f"Wrong, the right answer is '{X[-1].capitalize()}'.\n")
        return 0
        
score = 0
for i in range(len(universal_set)):
    score += ask_question(universal_set[i-1])

#grading and giving feedback.
if score <= len(universal_set)/2:
    print(f'You got {score} out of {len(universal_set)}. \nNeed more practice :(')
elif score < len(universal_set):
    print(f'You got {score} out of {len(universal_set)}. \nGood ;)')
else:
    print(f'You got {score} out of {len(universal_set)}. \nGreat! All your answers are correct <3')