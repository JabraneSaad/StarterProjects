import random as rand

#TODO : change the method of choise of mode (not a match case)
#TODO : implement the levels of dificulty through lives 

class Computer:
    
    def __init__(self, lives = 10):
        
        self.playing = True
        self.low = None
        self.high = None
        self.answer = None
        self.guess = None
        self.gs_state = None
        self.num_tries = 0
        self.guessing = True 
        self.lives = lives
        self.mode = None
        self.level = None
    
    #greet , get game mode , get difficulty level
    def greet(self):

        self.mode = (input('>>>\nHello there! This is a small game named GuessOrMakeMeGuess,\n choose the mode you want to play: <Riddler> if you want to guess a random number, <Guesser> if you want to make me guess a number! :').strip()).lower()
        while self.mode not in ['riddler','guesser']:
            self.mode = (input('>>>\nPlease choose one of the given options (Riddler/Guesser) :').strip()).lower()
        self.level = (input('\nSelect the level of difficulty (easy/normal/hard):').strip()).lower()
        while self.level not in ['easy','normal','hard']:
            self.level = input('\nPlease enter one of the given options (easy/normal/hard): ')
        if self.mode == "riddler":
            print(f"\nYou chose the {(self.mode).title()} {self.level} Mode, you have {self.lives} lives.\n")
        else:
             print(f"\nYou chose the {(self.mode).title()} Mode, I am always up for a challenge .\n")
class Riddler(Computer):
    def __init__(self):
        super().__init__()

        self.low = rand.randint(0,20)
        self.high = rand.randint(self.low+1,50)
        self.answer = rand.randint(self.low,self.high)

    def get_guessNumber(self):
        self.guess = input(f"\nGuess a numbfer between {self.low} and {self.high}: ")
        while not self.guess.isnumeric():
            self.guess = input("\nPlease enter a proper number")
        self.guess = int(self.guess)
        self.num_tries +=1

    def assert_gess(self):
        if self.guess > self.answer : 
            self.gs_state =  'lower'
            print(f'\nYour guess needs to be {self.gs_state}')
            self.lives -=1
            print(f"\nWrong! You now have {self.lives} lives.")

        elif self.guess < self.answer : 
            self.gs_state =  'higher'
            print(f'\nYour guess needs to be {self.gs_state}')
            self.lives -=1
            print(f"\nWrong! You now have {self.lives} lives.")

        elif self.guess == self.answer : self.gs_state =  True



    def check_win(self):
        if self.gs_state == True :
            print(f'Haha you won after {self.num_tries}')
            self.playing = False


            
class Guesser(Computer):
    def __init__(self):
        super().__init__()
        
        self.low = None
        self.high = None 
        self.answer = None
        
    
    def guet_boundaries(self):
        self.low = int(input('choose a range of guessing for the number , ex: for a number between 10 and 25 , low:10 and high:25\n lowest: '))
        self.high = int(input('high: '))
        
    def guessNumber(self):
        self.answer = rand.randint(self.low,self.high)
        self.num_tries +=1
    
    def assert_guess(self):
        self.asserted_guess = input(f"Is {self.answer} right(yes)? If your number is higher(higher), if your number is lower(lower)? (yes/higher/lower):")
        if self.asserted_guess =="yes": self.gs_state = True
        if self.asserted_guess == "lower": self.high = self.answer-1
        if self.asserted_guess == "higher": self.low = self.answer+1
    
    def check_win(self):
        if self.gs_state :
            print(f'Haha I won. Number of attempts: {self.num_tries}')
            self.guessing = False
            self.playing = False
    
    
def are_still_playing():
    temp = (input("would you like to play again?: (yes/no)").lower()).strip()
    return temp == "yes"

still_playing = True
C = Computer()

while still_playing:
    
    C.greet()

    match C.mode:
        case "guesser":
            g = Guesser()

            while g.playing:
                g.guet_boundaries()
                while g.guessing:
                    g.guessNumber()
                    g.assert_guess()
                    g.check_win()

        case "riddler":
            r = Riddler()

            while r.playing:
                r.get_guessNumber()
                r.assert_gess()
                r.check_win()
    still_playing = are_still_playing()   
        
print("thank you! See you next time ")

