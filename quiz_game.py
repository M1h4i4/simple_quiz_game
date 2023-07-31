# define questions
# define all answers and correct answers
# show question by question and ask for input 
# calculate the percentage of correct answers and display it to the user

questions = ('What is the name of 4 time Formula One World Champion from Germany?: ',
             'What is the name of the sixth planet in our Solar system?: ',
             'How many elements are in the periodic table of elements?: ',
             'What is the name of the capital city of Croatia?: ',
             'Which football team has won Champions League the most times?: ')

answers = (('A. Lewis Hamilton', 'B. Niki Lauda', 'C. Sebastian Vettel', 'D. Max Verstappen'),
           ('A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'),
           ('A. 97', 'B. 118', 'C. 125', 'D. 113'),
           ('A. Zagreb', 'B. Ljubljana', 'C. Beograd', 'D. Sarajevo'),
           ('A. Liverpool', 'B. Inter Milan', 'C. Barcelona', 'D. Real Madrid'))


correct_answers = ('C', 'D', 'B', 'A', 'D')
guesses = []
score = 0
question_num = 0


for question in questions:  
    print('-' * 65)
    print(question)
    for answer in answers[question_num]:
        print()
        print(answer)

    guess = input('\nPlease enter A, B, C or D: ').upper()
    guesses.append(guess)
    if guess == correct_answers[question_num]:
        score += 1
        print(f'Correct! The answer is {guess}')
    else:
        print(f'Unfortunately, the correct answer is {correct_answers[question_num]}')
    question_num += 1

print('\t\t', '-' * 35)
print('\t\t', '     RESULTS OF THE QUIZ      ')
print('\t\t', '-' * 35)

print('Your guesses were:')
for guess in guesses:
    print(guess, end=' ')
print()
print('Correct answers were: ')
for answer in correct_answers:
    print(answer, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score} %')
print()
if score < 50:
    print('Better luck next time!')
else:
    print('Good job!')

