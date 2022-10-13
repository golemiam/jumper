# filename: director.py
# Team 7am

class Director:
    """ A person who directs the game.

    The director is responsible for controlling the sequence of play.

    Attributes:
        
        guess(string): a lettler in the puzzle guessed by the player.
        is_playing(boolean): A value of True or False, defining whether the player is still playing.
        puzzle_word(string): A secret word randomly chosen from a list.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guess = ""
        self.is_playing = True
        self.puzzle_word = ""
        
    def start_game(self):
        """Starts the game.

        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return
        while self.is_playing:
            self.prompt_player()
            self.update_values()
            self.print_values()
        self.continue_game()

    def prompt_player(self):
        """Prompts the player for inputs.

        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return
    
    def update_values(self):
        """Updates the puzzle, guess count, and visible letters.
        
        Args:
            self (Director): an instance of Director.
        """
    
    def print_values(self):
        """Displays the puzzle graphics.
        
        Args:
            self (Director): an instance of Director.
        """

    def continue_game(self):
        """Asks the user if they would like to play again.
        
        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return
        restart_game = str(input("Would you like to play again?\n('yes' or 'no') "))
        if restart_game == "yes":
            self.start_game()
        elif restart_game == "no":
            self.is_playing = False
            return
        else:
            print("Sorry. That input wasn't accepted.")
            self.is_playing = False
            return