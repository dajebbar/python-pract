class BasketBallTeam:
    def __init__(self, team_name, wins, losses):
        self.team = team_name
        self.wins = wins
        self.losses = losses

    def stat(self):
        return f"[BASKETBALL] STATS: {self.team}: {BasketBallTeam.pluralize(self.wins, 'victory', 'victories')} - {BasketBallTeam.pluralize(self.losses, 'defeat')}"

    @classmethod
    def pluralize(cls, total, singular, plural=None):
        assert isinstance(total, int) and total >= 0, "total must be positive"
        if not plural:
            plural = singular + 's'
        string = singular if total <= 1 else plural
        return f"{total} {string}"


team_1 = BasketBallTeam("Los Ageles lakers", 12, 8)
team_2 = BasketBallTeam("Chicago Bulls", 10, 0)

# print(team_1.team)
# print(team_2.team)

# print(team_1.wins, team_1.losses)
# print(team_2.wins, team_2.losses)

print(team_1.stat())
print("=*=" * 20)
print(team_2.stat())
