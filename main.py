from py_compile import main
import random
if __name__ == "__main__": #runs everything in this block when we run the file
    def generate_random_number(): # being run multiple times, generating new number 
        random_number = random.randint(1, 100)
        return random_number
    random_number = generate_random_number()
    user_guess = 0 # initialize variable to store user's guess, set to 0 so it doesn't equal random number
    attempts = 0 
    max_attempts = 0
    difficulty = input('Choose a difficulty level (easy, medium, hard): ')
    if difficulty == 'easy':
        max_attempts = 15
    elif difficulty == 'medium':
        max_attempts = 10
    elif difficulty == 'hard':
        max_attempts = 5
    else:
        print('Invalid difficulty level. Please choose easy, medium, or hard.')
        exit() # exit the program if user enters invalid difficulty level
    while user_guess != random_number and attempts < max_attempts: 
        try:
            user_guess = int(input('Guess a number between 1 and 100: ')) 
        except (TypeError, ValueError): # if user enters something that can't be converted to an int, catch the error and prompt them to enter a valid number
            print('Invalid input. Please enter a number between 1 and 100.')
            continue # go back to the beginning of the loop
        # string -> int, to compare with the random number
        attempts += 1
        if user_guess == random_number:
            print('correct, you guessed the right number!')
            break # exit the loop, end the game
        elif user_guess < random_number:
            if user_guess + 10 == random_number:
                print('guess within 10 units of correct answer')
            elif user_guess + 5 == random_number:
                print('very close, guess withing 5 units of correct answer')
            else:
                print('too low. try again!')
            continue # go back to the beginning of the loop
        else: # only other option is guess higher than random number
            if user_guess - 10 == random_number:
                print('guess within 10 units of correct answer')
            elif user_guess - 5 == random_number:
                print('very close, guess withing 5 units of correct answer')
            else:
                print('too high. try again!')
            continue # go back to the beginning of the loop
    if attempts == max_attempts and user_guess != random_number:
            print(f'you have used all {max_attempts} attempts. The correct number was {random_number}.')
    else:
            print(f'you guessed the number in {attempts} attempts!')
    redo = input('Do you want to play again? (yes/no): ')
    if redo.lower() == 'yes':
        main()
    elif redo.lower() == 'no':
        print('Thanks for playing! Goodbye!')
    else:
        print('Invalid input. Exiting the game.')
