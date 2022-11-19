from Hangman_source import *

while still_playing:   
    g.greet()
    while g.playing:
        g.getGuess()
        g.checkGuess()
        g.liveOrDie()
        g.check_win()
        g.check_loss()
    still_playing = are_still_playing()   
           
print("thank you! See you next time ")
