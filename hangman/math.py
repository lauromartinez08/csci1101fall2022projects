import re
import random

pool_file = open(".com.google.Chrome.JLV29a")


pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)
    
    pool_answer_line = pool_file.readline()

pool_file.close()



answer = random.choice(pool_answers)
answer = answer.upper()

#game setup
num_of_incorrect_guesses = 5

answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$",current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

current_incorrect_guesses = 0

letters_guessed = []

while current_incorrect_guesses < num_of_incorrect_guesses or False not in answer_guessed:
    print(f"Number of incorrect guesses left: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Guessed letters: ", end="")

    for current_guessed_letter in letters_guessed:
        print(current_guessed_letter, end=" ")

    print()

    #display puzzle board
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")

    print()
    #let user guess a letter
    letter = input("Enter a letter: ")

    letter = letter.upper()

    print()

    #check if user entered a valid letter
    if re.search("^[A-Z]$",letter) and len(letter) == 1 and letter not in letters_guessed:
        current_letter_index = 0


        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break
            current_letter_index += 1

        letters_guessed.insert(current_letter_index, letter)

        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorrect_guesses += 1

#post game summary
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("Congratulations, you won!")
else:
    print(f"Sorry you lost :( the answer was {answer}")
