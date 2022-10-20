import random
class Word:
    """ A word for the game

    Word is responsible for generating a word and validating the guess.

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
        self._words = ["Cheese", "Monkey", "Brigham", "Young", "University", 
            "incredible", "Fancy", "Palisade", "Xylem", "Phloem"]
        self._word = random.choice(self._words)
        
    def compare_letters(self, players_choice):
        """Compares the letters of the word.

        Args:
            self (Word): an instance of Word.
            players_choice: a string containing the player's guess.
        """
        len(self._word)
        word_letters = list(self._word)
        players_list = list(self.players_choice)
        for letter in word_letters:
            for letters in players_list:
                if word_letters[letter] == players_list[letters]:


        

                    

    def check_guess(self, player_choice):
        """
        """
        players_choice = self._guess
        if(player_choice in self._word):
            return True
        else:
            mistakes = mistakes + 1
            return False
  
