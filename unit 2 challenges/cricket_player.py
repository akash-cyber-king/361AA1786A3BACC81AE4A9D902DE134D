class player:
        def play(self):
                print("playe is playing circket")
class batsman(player):
        def play(self):
                print("the batsman is batting")
class blower(player):
        def play(self):
                print ("the bowler is bowling")

Batsman = batsman()
Bowler= blower()


Batsman.play()
Bowler.play()
