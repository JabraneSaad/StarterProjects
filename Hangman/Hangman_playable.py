from Hangman_source import *


while g.playing:
    g.greet()
    g.getGuess()
    g.checkGuess()
    g.liveOrDie()
    g.check_win()
    g.check_loss()

