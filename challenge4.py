class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
def main():
    batsman = Batsman("Virat Kohli")
    bowler = Bowler("Jasprit Bumrah")

    batsman.play()
    bowler.play()

if __name__ == "__main__":
    main()
  
