class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        if self.race.lower() == "human":
            self.stats = [100, 100, 50, 40, 50]
        elif self.race.lower() == "orc":
            self.stats = [200, 20, 100, 80, 10]
        elif self.race.lower() == "kahjiit":
            self.stats = [50, 50, 20, 30, 100]
        
    def __str__(self, stat_condition):
      if stat_condition == "health":
        return f"{self.stats[0]}"
