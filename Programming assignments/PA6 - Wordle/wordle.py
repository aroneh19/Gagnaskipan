import random, os
from wordbank import WordBank
from players import Player

class Wordle:
    def __init__(self, words):
        """Initializes a Wordle game instance.

        Args:
            words (list): A list of words to choose from.
        """
        self.word = random.choice(words).upper()
        self.max_guess = len(self.word)
            
    def check_guess(self, guess):
        """Checks the guess against the hidden word.

        Args:
            guess (str): The guessed word.

        Returns:
            str: A string representing correct letters guessed in the correct positions,
                 and incorrect letters guessed in incorrect positions.
        """
        compare = ["-"] * len(self.word)
        keyword = list(self.word)

        for i, letter in enumerate(guess):
            if keyword[i] == guess[i]:
                compare[i] = letter
                keyword[i] = ''

        for i, letter in enumerate(guess):
            if (letter in keyword) and (compare[i] == '-'):
                compare[i] = letter.lower()
        return ''.join(compare)

    def play(self, player):
        """Executes a single game of Wordle.

        Args:
            player (Player): The player participating in the game.

        Returns:
            bool: True if the player wins, False otherwise.
        """
        clear_screen()
        print(f"Username: {player.username}")
        counter = 1
        while counter <= self.max_guess:
            print(f"Guess - {counter}/{self.max_guess}")
            guess = input("Enter word: ").upper()
            if len(guess) == self.max_guess:
                print(self.check_guess(guess))
                counter += 1
                if guess == self.word:
                    return True
            else:
                print("Not enough characters to guess")
            print()
        return False

    def victory(self, player, score):
        """Handles the victory scenario.

        Args:
            player (Player): The player who won.
            score (int): The current score.

        Returns:
            int: The updated score.
        """
        print("\nVictory!")
        player.stats["wins"] += 1
        return score + self.max_guess

    def loss(self, player, score):
        """Handles the loss scenario.

        Args:
            player (Player): The player who lost.
            score (int): The current score.

        Returns:
            int: The updated score.
        """
        print("You lose!")
        print(f"The word was: {self.word}")
        player.stats["losses"] += 1
        player.update_stats(score)
        player.save_profile()
        return 0
    
def gamemode():
    """Allows the player to choose a game mode.

    Returns:
        Wordle: A Wordle game instance.
    """
    while True:
        clear_screen()
        print("Choose a mode:")
        print("1. 5 Letters")
        print("2. 6 Letters")
        print("3. 7 Letters")
        print("4. Add a Word")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3']:
            length = int(choice) + 4
            return Wordle(getattr(wordbank, f"words_{length}"))
        elif choice == '4':
            clear_screen()
            new_word = input("Enter the word to add: ").strip().capitalize()
            if new_word.isalpha():
                wordbank.add_word(new_word)
                input(f"\n'{new_word}' has been added to the word bank.\nPress ENTER to continue")
            else:
                print("Please enter a valid word.")
        else:
            input("Invalid choice.\nPress ENTER to try again")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == "__main__":
    print("Welcome to Wordle!")

    while (username := input("Enter your username: ")) == "":
        print("Username cannot be empty. Please try again.")
    
    player = Player(username)
    player.load_profile()
    wordbank = WordBank()
    
    score = 0
    play_again = True
    while play_again:
        game = gamemode()
        play = game.play(player)
        if play:
            score = game.victory(player, score)
        else:
            score = game.loss(player, score)

        play_again = input("\nPlay Again (j/n): ")
        if play_again.lower() == "n":
            play_again = False

    if score:
        player.update_stats(score)
    player.save_profile()

    display = input("\nDo you want to display your player card (y/n): ")

    if display.lower() != "n":
        clear_screen()
        player.display_player()
        