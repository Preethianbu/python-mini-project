import random

class Hangman:
    def __init__(self):
        name=input("What is your name?")
        print("Welcome to 'Hangman' " +name, "are you ready to play?")
        print("(1) Yes, for I am ready to die!\n(2) No, get me outta here!")
        user_choice_1 = input("-> ")

        if user_choice_1 == 'yes':
            print("Loading hangman...")
            self.start_game()
        elif user_choice_1 == 'no':
            print("Bye bye now...")
            exit()
        else:
            print("I'm sorry, I didn't understand that.")
            self.__init__()

    def start_game(self):
        print("A crowd begins to gather, they can't wait to see some real justice.")
        print("There's just one thing, you aren't a real criminal.")
        
        print("No, no. You're the wrong time, wrong place type. You may think")
        print("you're doomed, but it's not like that at all.")
        
        print("Yes, yes. You've got a chance to live. All you've gotta do")
        print("is guess the right word and you can live to see another day.")
        
        print("But don't get too happy yet. If you make 6 wrong guesses,")
        
        print("YOU'RE TOAST! VAMANOS!")
        
        print("What is the data type in Python? ")
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        words = ['integer', 'dictionary', 'boolean', 'string', 'float', 'tuple']
        the_word = random.choice(words)
        progress = ["?"] * len(the_word)

        while guesses < 6:
            guess = input("Guess a letter -> ")

            if guess in letters_used:
                print("You've already guessed that letter. Try again!")
                continue

            if guess in the_word:
                print("As it turns out, your guess was RIGHT!")
                letters_used += guess
                self.hangman_graphic(guesses)
                progress = self.progress_updater(guess, the_word, progress)
                print("Progress: " + "".join(progress))
                print("Letters used: " + letters_used)
                if "".join(progress) == the_word:
                    print("Congratulations, you won! You've guessed the word correctly.")
                    self.play_again()
                    return
            else:
                guesses += 1
                print("Things aren't looking so good, that guess was WRONG!")
                print("Oh man, that crowd is getting happy, I thought you")
                print("wanted to make them mad?")
                letters_used += guess
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letters used: " + letters_used)

        print("GAME OVER! The word was:", the_word)
        self.play_again()

    def hangman_graphic(self, guesses):
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |
            """,
            """
               --------
               |      |
               |      O
               |
               |
               |
            """,
            """
               --------
               |      |
               |
               |
               |
               |
            """
        ]
        print(stages[guesses])

    def progress_updater(self, guess, the_word, progress):
        for i, char in enumerate(the_word):
            if guess == char:
                progress[i] = guess
        return progress

    def play_again(self):
        choice = input("Would you like to play again? (yes/no): ").lower()
        if choice == 'yes':
            self.__init__()
        else:
            print("Goodbye!")


game = Hangman()
