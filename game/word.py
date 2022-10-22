import random

class Word:
    """A word for the game

    Word is responsible for generating the word.

    Attributes:
        words(list): a list containing the words for the game.
        word(string): a string containing the secret word for the game.
        guess(string): a string containing the player's guessed letter.
    """
    def __init__(self):
        self._words = []
        self._word = ""
        self._guess = ""
        
    def create_word(self):
        """Creates an instance of the word for the game.
        
        Args:
            self (Word): an instance of Word.
        """
        self._words = ["cheese", "monkey", "brigham", "young", "university", 
            "incredible", "fancy", "palisade", "xylem", "phloem"]
        self._word = random.choice(self._words)
        
        return self._word
