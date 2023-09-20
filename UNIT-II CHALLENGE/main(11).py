class player:
    def play(self):
      print(" THE PLAYER IS PLAYING CRICKET .")
class Batsman(player):
    def play(self):
        print(" THE BATS MAN IS BATTING. ")
class Bowler(player):
    def play(self):
        print(" THE BOWLER IS BOWLING. ")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
      
        