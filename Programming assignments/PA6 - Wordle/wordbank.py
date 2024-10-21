
class WordBank:
    def __init__(self):
        """Initializes a WordBank instance by loading word lists from files.

        The files are expected to be named 'words_5.txt', 'words_6.txt', and 'words_7.txt',
        containing words of lengths 5, 6, and 7 respectively.
        """
        self.words_5 = open_file("words_5.txt")
        self.words_6 = open_file("words_6.txt")
        self.words_7 = open_file("words_7.txt")
    
    def add_word(self, word):
        """Adds a word to the appropriate word list file.

        Args:
            word (str): The word to add.

        Raises:
            ValueError: If the word length is not between 5 and 7.
        """
        length = len(word)
        if length < 5 or length > 7:
            print("Word length should be between 5 and 7.")
            return
        filename = f"words_{length}.txt"
        with open(filename, 'a') as file:
            file.write(word + '\n')
        print("Word added successfully.")
        self.update_word_list(length)

    def update_word_list(self, length):
        """Updates the word list attribute corresponding to the given length.

        Args:
            length (int): The length of the word.
        """
        if length == 5:
            self.words_5 = open_file("words_5.txt")
        elif length == 6:
            self.words_6 = open_file("words_6.txt")
        elif length == 7:
            self.words_7 = open_file("words_7.txt")
    
def open_file(filename):
    """Opens a file and returns its contents as a list of words.

    Args:
        filename (str): The name of the file to open.

    Returns:
        list: A list of words read from the file.
    """
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words
