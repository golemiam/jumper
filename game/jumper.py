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
    def __init__(self, word_length) -> None:
        """Constructs a new Jumper.

        Args:
            self (Jumper): an instance of Jumper.
            word_length(int): the length of the word as an integer.
        """
        self._word = Word.create_word
        self._letters = list(self._word)
        self._word_length = word_length
        self._blank_string = self.create_blank_string(self, self._word_length)
        pass

    def create_blank_string(self, word_length):
        """Constructs a blank string.

        Args:
            self (Jumper): an instance of Jumper.
            word_length: an integer equal to the number of letters in the word.
        """
        blank = " _"
        blank_string = []
        self._word_length = word_length
        for _ in word_length:
            blank_string.append(blank)
        return blank_string

    
    def update_blank_string(self, player_guess):
        """Updates the blanks in a string with letters from successful guesses.

        Args:
            self (Jumper): an instance of Jumper.
            blank_string(string): a string comprised of blanks and successfully guessed letters.
            player_guess(string): a letter that the player guessed.
        """
        letters = list(self._word)
        blank_string = self._blank_string
        for blank in blank_string:
            for letter in letters:
                if player_guess == letter:
                    blank_string[blank] =+ player_guess
                else:
                    blank_string[blank] =+ "_ "

        self._blank_string = blank_string