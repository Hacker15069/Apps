import random

class Game:
    def __init__(self, rounds, playersGuess):
        self.rounds = rounds
        self.playersGuess = playersGuess
        self.response = 'Comming soon'
        self.choices = ['Rock','Scissors','Paper']
        self.playersPoints = 0
        self.computersPoints = 0
        
    def Game(self):
        computersGuess = random.choice(self.choices)
        playersChoiceConditions = [self.playersGuess == 'Rock', self.playersGuess == 'Paper', self.playersGuess == 'Scissors']
        computersChoiceConditions = [computersGuess == 'Rock',computersGuess == 'Paper', computersGuess == 'Scissors']

        #if player chooses rock
        if playersChoiceConditions[0]:

            def Rock():
                #if computer chooses Rock
                if computersChoiceConditions[0]:
                    self.response = 'We both picked rock so no points in given'
                
                #if computer chooses Scissors
                elif computersChoiceConditions[1]:
                    self.playersPoints+=1
                    self.response = 'You picked rock and I picked scissors so 1 point for you'

                #if computer chooses Paper
                elif computersChoiceConditions[2]:
                    self.computersPoints+=1
                    self.response = 'I picked paper and you picked rock for 1 point for me'

                #if an error was raised
                else:
                    pass
            Rock()
            
        #if player chooses scissors
        elif playersChoiceConditions[1]:

            def Scissors():
                #if computer chooses Rock
                if computersChoiceConditions[0]:
                    self.computersPoints+=1
                    self.response = 'You picked rock and I picked scissors so 1 point for me'

                #if computer chooses Scissors
                elif computersChoiceConditions[1]:
                     self.response = 'We both picked scissors so no points is given'

                #if Paper
                elif computersChoiceConditions[2]:
                    self.response  = 'I picked paper and you picked scissors for 1 point for you'
                    self.playersPoints+=1

                #if None
                else:
                    pass   
            Scissors()
            
        #if player chooses paper  
        elif playersChoiceConditions[2]:
            
            def Paper():
                #if rock
                if computersChoiceConditions[0]:
                    self.response = 'You picked paper and I picked rock so one point for you'
                    self.playersPoints+=1

                #if Scissors
                elif computersChoiceConditions[1]:
                    self.response = 'I picked scissors so 1 point for me'
                    self.computersPoints+=1

                #if Paper
                elif computersChoiceConditions[2]:
                    self.response = 'We both picked paper so no points is given'

                #if None
                else:
                    pass
            Paper()
            
        #if an error was raised
        else:
            pass
