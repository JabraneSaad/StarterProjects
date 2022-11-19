import random as rand
# guess the computers number 

class Computer:
    
    def __init__(self):
        
        self.playing = True
        self.low = None
        self.high = None
        self.answer = None
        self.guess = None
        self.gs_state = None
        self.num_tries = 0
        self.guessing = True 
    
    def greet():
        mode = None
        while mode!= "Guesser" and mode != "Riddler":
            mode = input('>>>\n Hello! This is a small game named GuessOrMakeMeGuess, choose the mode you want to play: <Riddler> if you want to guess a random number, <Guesser> if you want to make me guess a number! :').strip()
        return mode.lower()
        

class Riddler(Computer):
    def __init__(self):
        super().__init__()
        print("You chose the Riddler Mode.")
        
        self.low = rand.randint(0,20)
        self.high = rand.randint(self.low+1,50)
        self.answer = rand.randint(self.low,self.high)

        
    def get_guessNumber(self):
        self.guess = int(input(f"guess a numbfer between {self.low} and {self.high}: "))
        self.num_tries +=1
    
    def assert_gess(self):
        if self.guess > self.answer : 
            self.gs_state =  'lower'
            print(f'your guess needs to be {self.gs_state}')
        elif self.guess < self.answer : 
            self.gs_state =  'higher'
            print(f'your guess needs to be {self.gs_state}')

        elif self.guess == self.answer : self.gs_state =  True
        
    
    def check_win(self):
        if self.gs_state == True :
            print(f'Haha you won after {self.num_tries}')
            self.playing = False
            
class Guesser(Computer):
    def __init__(self):
        super().__init__()
        print("You chose the Guesser Mode.")
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
    
    
        
        
mode = Computer.greet()

match mode:
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

  


