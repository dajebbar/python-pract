class BasketBallTeam:

    fine_amount = 50_000
    team_cnt = 0

    def __init__(self, team_name, wins, losses):
        self.team = team_name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0
        BasketBallTeam.team_cnt += 1

    def get_fined(self):
        self.total_fines += self.fine_amount  # BasketBallTeam.fine_amount
        # return self.total_fines

    @classmethod
    def set_fines(cls, amount):
        cls.fine_amount = amount

    @classmethod
    def from_string(cls, stats_as_str):
        team, win, loss = stats_as_str.strip().split("-")
        return cls(team, int(win), int(loss))
    
    @classmethod
    def from_file(cls, link):
        with open(link, 'r', encoding='utf-8') as f:
            for line in f:
                stat = BasketBallTeam.from_string(line)
                print(stat.stat())

    def stat(self):
        return f"[BASKETBALL] STATS: {self.team}: {self.pluralize(self.wins, 'victory', 'victories')} - {self.pluralize(self.losses, 'defeat')}"

    @staticmethod
    def pluralize(total, singular, plural=None):
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

# print(team_1.stat())
# print("=*=" * 20)
# print(team_2.stat())

# team_1.get_fined()
# team_1.get_fined()
# print(team_1.total_fines)

# print(vars(BasketBallTeam))
# print()
# print("=*=" * 30)
# print()
# print(vars(team_1))

# BasketBallTeam.fine_amount = 30_000
# print(team_2.fine_amount)
# team_1.fine_amount = 18_000
# print(BasketBallTeam.fine_amount)
# print(team_1.fine_amount)
# print(team_2.fine_amount)

# print(vars(team_1))
# print(vars(team_2))

# print(BasketBallTeam.team_cnt)

# BasketBallTeam.set_fines(95_000)
# print(team_1.fine_amount)
# print(team_2.fine_amount)
# team_1.set_fines(61_000)
# print(team_1.fine_amount)
# print(team_2.fine_amount)
# print(BasketBallTeam.fine_amount)
# print(vars(team_2))
# print(vars(BasketBallTeam))

utah_stats = "Utah Jazz-34-7"
# team, win, loss = utah_stats.split("-")
# team_3 = BasketBallTeam(team, int(win), int(loss))
team_3 = BasketBallTeam.from_string(utah_stats)
print(team_3.stat())


# with open('nba.txt', 'r', encoding='utf-8') as f:

#     for line in f:
#         stat = BasketBallTeam.from_string(line)
#         print(stat.stat())

team_4 = BasketBallTeam.from_file('nba.txt')
print(team_1.stat())
print(team_2.stat())
