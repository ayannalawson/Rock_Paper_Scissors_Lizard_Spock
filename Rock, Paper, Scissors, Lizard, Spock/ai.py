from player import Player
import random


class AI (Player):
    def __init__(self, name):
        super().__init__()
        self.name = "Aerith FFVII"
        
        
        def set_name(self):
            self.name = name
            
        def choose_gesture(self):
            selected_gesture = random.chioce(self.geture_list)
            self.gesture_selected = selected_gesture
            print(f"{self.gesture_selected}")
        
        
    def choose_gesture(self):
        self.ai_turn = random.choice(["Rock", "Paper" , "Scissors", "Lizard", "Spock"])

        print(f"The AI chose {self.ai_turn}")
        
        # As a developer, I want to find a way to properly incoporate inheritance into my game.