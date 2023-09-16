#Define base class player
class Player:
  def play(self):
       print("The player is playing cricket")

#Define derived class Batsman
class Batsman(Player):
  def play(self):
       print("The batsman is batting")

#Define derived class Bowler
class Bowler(Player):
  def play(self):
       print("The bowler is bowling")

#Creating objects for batsman and bowler classes
batsman= Batsman() 
bowler= Bowler() 

#call play() method for each object
batsman. play() 
bowler.play() 