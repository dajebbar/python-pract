import utils


class SportTeam:

    fine_amount = 50_000
    team_cnt = 0

    def __init__(self, team_name, wins, losses):
        self.team = team_name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0
        SportTeam.team_cnt += 1

    def get_fined(self):
        self.total_fines += self.fine_amount  # BasketBallTeam.fine_amount
        # return self.total_fines

    def stat(self):
        return f"{self.team}: {utils.pluralize(self.wins, 'victory', 'victories')} - {utils.pluralize(self.losses, 'defeat')}"

    @classmethod
    def set_fines(cls, amount):
        cls.fine_amount = amount

    @classmethod
    def from_string(cls, stats_as_str):
        team, win, loss = stats_as_str.strip().split("-")
        return cls(team, int(win), int(loss))

    @classmethod
    def from_file(cls, link):
        basket_objects = []
        with open(link, 'r', encoding='utf-8') as f:
            for line in f:
                team, win, loss = line.strip().split("-")
                basket_objects.append(cls(team, int(win), int(loss)))
        return basket_objects


class BasketBallTeam(SportTeam):
    def stat(self):
        return "[Basketball stats]: " + super().stat()


class FootBallTeam(SportTeam):
    def stat(self):
        return "[Foottball stats]: " + super().stat()


class BaseBallTeam(SportTeam):
    def stat(self):
        return "[Baseball stats]: " + super().stat()

# basket_team_1 = BasketBallTeam("Los Ageles lakers", 12, 8)
# basket_team_2 = BasketBallTeam("Chicago Bulls", 10, 0)

# print(basket_team_1.stat())
# print(basket_team_2.stat())

# utah_stats = "Utah Jazz-34-7"
# basket_team_3 = BasketBallTeam.from_string(utah_stats)
# print(basket_team_3.stat())


basket_team_4 = BasketBallTeam.from_file('nba.txt')
for team in basket_team_4:
    print(team.stat())


print("==*==" * 10)

foot_team_1 = FootBallTeam.from_file('nfl.txt')
for team in foot_team_1:
    print(team.stat())


print("==*==" * 15)

baseball_team_1 = BaseBallTeam.from_file('baseball.txt')
for team in baseball_team_1:
    print(team.stat())
