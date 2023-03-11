from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        
    def choose_gesture(self):
        self.chosen_gesture = input("Which gesture would like to start with?")
        
    def round_won(self):
        self.current_score +=1