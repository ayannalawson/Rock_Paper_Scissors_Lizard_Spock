class Player:

    def __init__(self):
        self.gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.player_point = 0


        def choose_geture(self):
            while True:
                self.gesture_choice = input("Enter 0 for Rock, 1 for Scissor, 2 for Paper, 3 for Lizard, 4 for Spock: ")
                if self.gesture_choice == "0":
                    print(f"You've Chosen {self.gesture[0]}")
                elif self.gesture_chioce == "1":
                    print(f"You've Chosen {self.gesture[1]}")
                elif self.gesture_choice == "2":
                    print(f"You've Chosen {self.gesture[2]}")
                elif self.gesture_choice == "3":
                    print(f"You've Chosen {self.gesture[3]}")
                elif self.gesture_choice == "4":
                    print(f"You've Chosen {self.gesture[4]}")
                if self.gesture_choice not in ['0','1','2','3','4']:
                    print("Nope. Once Again. Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock: ")
                else:
                    break
                
                # As a developer, I waant to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc). The gesture list is in line 4.
                