from Hangman_source import *

g = Hangman(8,'Orange') 

while g.playing:
    g.getGuess()
    g.checkGuess()
    g.liveOrDie()
    g.display_state()
    g.check_win()
    g.check_loss()
