from human import Human

from ai import AI

from player import player 

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.player_point = 0 
        self.gesture == None
        self.winner_of_the_round = None
        self.winner_of_the_game = None
        super().__init__()

    def run_game(self):
        self.welcome_message()
        self.rules_explanied()
        self.game_mode()
        self.player_picks()
        self.rule_one()
        self.rule_two()
    # The Introduction Phase
    def welcome_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    # Welcome message
    def rules_explained(self):
        print("Rock, Paper, Scissors, Lizard, Spock is the game of rock, paper, scissor! Choose wether you would like to play with another player or against the AI.")
        print("Best 2 out of 3 wins!")
        print("Here are the instructions in order to win the game: Rock of course crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock.")
        print("Now that we covered that, Let the games bagin!")
    #Rules Explained

    #Choose game type - Assign a type to Player 2
    def game_mode(self):
        player_response = int(input("Enter Start to play against another person, or type begin to play against an AI.: "))
        if int(player_response) == 1:
            player_response = self.player_two = Human()
            print(f"You choose to play against another player!")
        elif int(player_response) == 2:
            player_response = self.player_two = AI()
            print(f"You choose to go against the AI")
        else:
            print("Now pick 1 or 2 to continue.")
    
    #Game round phase - Loop
    def player_picks(self):

        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

    #Determine winner of the round
    def rule_one(self):
        while self.player_point <=2:
            if self.player_one.choose_gesture == 0 and self.player_two.choose_gesture == 1: 
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 1 and self.player_two.choose_gesture == 2:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 2 and self.player_two.choose_gesture == 0:
                print("Player one wins")
                return(self.player_point + 1)
            elif self.player_one.choose_gesture == 0 and self.player_two.choose_gesture == 3:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 3 and self.player_two.choose_gesture == 4:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 4 and self.player_two.choose_gesture == 1:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 1 and self.player_two.choose_gesture == 3:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 3 and self.player_two.choose_gesture == 2:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 2 and self.player_two.choose_gesture == 4:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == 4 and self.player_two.choose_gesture == 0:
                print("Player one wins")
                return(self.player_point +1)
            elif self.player_one.choose_gesture == self.player_two.choose_gesture:
                print("It's a Tie! Let's start again!")
                return(self.player_point ==0)
            else:
                print("Player two wins.")
                return(self.player_point +1)
    #Determine winner of the game    
    def rule_two(self):
        player_point = 0
        self.winner_of_the_gmae = 2
        if self.player_one == player_point == 2:
            self.player_one = self.winner_of_the_game
        else:
            self.player_two = self.winner_of_the_game

    #Endgame