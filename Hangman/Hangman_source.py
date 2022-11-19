import random as rand 
import  csv 
# TODO : Faire une liste de mots random a selectionner pour le 
class Word:
    def __init__(self):
        spamReader = csv.reader(open('Hangman_wordbank.csv', 'r'))
        data = sum([i for i in spamReader],[])
        self.chosenWord = (rand.choice(data)).strip()        
class Hangman:
    
    def __init__(self, lives:int, word):
    
        self.lives = lives
        self.word = word.upper()
        self.spots = len(word)*['_']
        self.guess = None
        self.matching = None
    
        self.playing = True
    # get the guessed letter
    def greet(self):
        print(">>> Hello this is a Hangman game, I will generate a random word and you'll have 8 lives to find it out "
              "by guessing its letters.")
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
            print(self.word)
            self.playing = False

    def check_win(self):
        if '_' not in self.spots:
            print('you won!')
            self.playing =  False
            
    def display_state(self):
        print(self.spots)

w = Word()
g = Hangman(8,w.chosenWord) 
