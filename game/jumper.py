from game.word import Word
class Jumper:
    """The main aspects of the jumper game.
    The purpose of Jumper is to keep track of the blank spaces and other data of the guessing portion of the game.
    
    Attributes:
        _word(string): a string containing the hidden word that the player is trying to guess.
        _blanks(string): a string representing the hidden word with blanks where the letters would be.
        _letters(string): a string containing the letters in a word.
        _word_length(string): the number of letters in the word that the player is trying to guess.
        """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): an instance of Jumper.
        """
        self._word = Word().create_word()
        letters_list = list(self._word)
        self._letters = letters_list
        self.mistakes_count = -1
        self._word_length = len(self._word)
        self._blank_string = self.create_blank_string(self._word_length)
        self.game_win = False
        pass

    def create_blank_string(self, word_length):
        """Constructs a blank string.

        Args:
            self (Jumper): an instance of Jumper.
            word_length: an integer equal to the number of letters in the word.
        """
        blank = "_"
        blank_string = []
        self._word_length = word_length
        x = self._word_length
        while x != 0:
            blank_string.append(blank)
            x -= 1
        return blank_string

    def update_blank_string(self, player_guess):
        """Updates the blanks in a string with letters from successful guesses.

        Args:
            self (Jumper): an instance of Jumper.
            blank_string(string): a string comprised of blanks and successfully guessed letters.
            player_guess(string): a letter that the player guessed.
        """
        letters = self._letters
        new_blank_string = []
        
        for letter in letters:
            if player_guess == letter:
                new_blank_string.append(letter)
            elif letter in self._blank_string:
                new_blank_string.append(letter)
            elif player_guess != letter:
                new_blank_string.append("_")
            else:
                new_blank_string.append("_")
        if new_blank_string == self._blank_string:
            self.mistakes_count += 1
        if new_blank_string == letters:
            self.game_win = True
        self._blank_string = new_blank_string
        return self._blank_string