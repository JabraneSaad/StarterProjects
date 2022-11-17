class Hangman:
    
    def __init__(self, lives:int, word:str):
    
        self.lives = lives
        self.word = word.upper()
        self.spots = len(word)*['_']
        self.guess = None
        self.matching = None
    
        self.playing = True
    # get the guessed letter
    def getGuess(self):
        self.guess =(input("guess a letter:")).upper()
    
    # check the guessed letter if  in word
    def checkGuess(self):
        if self.guess in self.word: 
            self.matching = True 
        else :
            self.matching = False
    
    # change the diplay of the spots/hints 
    # diplay the number of lives left
    def liveOrDie(self):
        temp_index = []
        if self.matching:
            for i in range(len(self.word)):
                if self.word[i]  == self.guess:
                    temp_index.append(i)
            for index in temp_index:
                self.spots[index] = self.guess
        else : 
            self.lives -= 1
            print(f'you have {self.lives} lives left')
    
    # check if still alive and changes playing var to stop the loop
    def check_loss(self):
        if self.lives <= 0:
            print("you are dead, terminate the game")
            self.playing = False
        
    def check_win(self):
        if '_' not in self.spots:
            print('you won!')
            self.playing =  False
            
    def display_state(self):
        print(self.spots)

#TO DO: 
t = Hangman(8,'Orange') 

while t.playing:
    t.getGuess()
    t.checkGuess()
    t.liveOrDie()
    t.display_state()
    t.check_win()
    t.check_loss()

    
    