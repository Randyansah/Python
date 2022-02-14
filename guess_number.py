import random


def guess_a_number():

    number = random.randint(1, 25)
    num_of_guess = 0
    while num_of_guess < 5:

        num_of_guess = num_of_guess+1
        string = """
        WELCOME TO THE GUESSING GAME
        DO YOU HAVE THE GUESSING POWER
        CAN YOU GUESS THE RIGHT NUMBER
        LETS SEE HOW YOU CAN GUESS A NUMBER BETWEEN 1 AND 25
        YOU WILL BE GIVEN 5 CHANCES
        
        """
        print(string)
        guess = int(input("ENTER YOUR GUESS: "))
        if guess > number:
            print("THE NUMBER YOU ENTERED IS BIGGER (:")
        if guess < number:
            print("THE NUMBER YOU ENTERED IS  SMALLER (:")
        if guess == number:
            break
    if guess == number:
        print("YOU GUESSED IT RIGHT")
    else:
        print("YOUR GUESSED THE WRONG NUMBER.THE NUMBER IS {}".format(number))


guess_a_number()
