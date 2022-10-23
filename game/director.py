# filename: director.py
# Team 7am
import random
import turtle
from game.art import Draw_shapes, Wires, mistakes_count, reset
from game.jumper import Jumper

class Director:
    """ A person who directs the game.

    The director is responsible for controlling the sequence of play.

    Attributes:
        
        guess(string): a lettler in the puzzle guessed by the player.
        is_playing(boolean): A value of True or False, defining whether the player is still playing.
        mistakes(int): An integer representing the number of failed guesses the player has.
        jumper(class): An instance of the Jumper class.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guess = ""
        self.is_playing = True
        self.jumper = Jumper()
        self.reset = reset()
        self.mistakes = self.jumper.mistakes_count

    def start_game(self):
        """Starts the game.

        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return
            
        rules = input("Welcome to Jumper!\nWould you like to see the rules? \n(yes or no) >")
        if rules.lower() == "yes":
            print("\nYou will be given a random word to guess one letter at a time.")
            print("You will be able to guess until you discover the entire word or you run out of trys.")
            print("Have fun!\n")
        
        while self.is_playing:
            self.print_values()
            self.prompt_player()
            if self.mistakes == 6:
                self.continue_game()
            if self.jumper.game_win:
                self.continue_game()

    def prompt_player(self):
        """Prompts the player for inputs.

        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return
        if not self.jumper.game_win:
                if(len(self.jumper.getChosenList())>=1):
                    print(self.jumper.strChosenList())
                self.guess = input("Guess a letter [a-z]: ").lower()
                self.jumper.addChosenList(self.guess)


    def print_values(self):
        """Displays the puzzle graphics.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        jumper = self.jumper
        hidden_word = jumper.update_blank_string(self.guess)
        print(" ".join(str(x) for x in hidden_word))
        print()
        reset.resets("self")
        self.mistakes = self.jumper.mistakes_count
        mistakes_count(self.mistakes)

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
    
