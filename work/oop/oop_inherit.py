import utils


class SportTeam:

    GAME_CAN_BE_TIE = False
    fine_amount = 50_000
    team_cnt = 0

    def __init__(self, team_name, wins, losses, draws=0):
        self.team = team_name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0
        if self.__class__.GAME_CAN_BE_TIE:
            self.draws = draws

        # if self.__class__.__name__ == 'BasketBallTeam':
        #     BasketBallTeam.team_cnt += 1
        # elif self.__class__.__name__ == 'FootBallTeam':
        #     FootBallTeam.team_cnt += 1
        # elif self.__class__.__name__ == 'BaseBallTeam':
        #     BaseBallTeam.team_cnt += 1

        # if isinstance(self, BasketBallTeam):
        #     BasketBallTeam.team_cnt += 1
        # elif isinstance(self, FootBallTeam):
        #     FootBallTeam.team_cnt += 1
        # elif isinstance(self, BaseBallTeam):
        #     BaseBallTeam.team_cnt += 1

        self.__class__.team_cnt += 1

        SportTeam.team_cnt += 1

    def get_fined(self):
        self.total_fines += self.fine_amount  # BasketBallTeam.fine_amount
        # return self.total_fines

    def stat(self):
        sport_type = self.__class__.__name__.replace('Team', '').upper()
        if self.__class__.GAME_CAN_BE_TIE:
            return f"[{sport_type}] STATS: {self.team} has {utils.pluralize(self.wins, 'victory', 'victories')}, {utils.pluralize(self.losses, 'defeat')} and {utils.pluralize(self.draws, 'draw')}"
        return f"[{sport_type}] STATS: {self.team} has {utils.pluralize(self.wins, 'victory', 'victories')} and {utils.pluralize(self.losses, 'defeat')}"

    @classmethod
    def set_fines(cls, amount):
        cls.fine_amount = amount

    @classmethod
    def from_string(cls, stats_as_str):

        return cls(*stats_as_str.strip().split("-"))

    @classmethod
    def from_file(cls, link):
        basket_objects = []
        with open(link, 'r', encoding='utf-8') as f:
            for line in f:
                basket_objects.append(cls(*line.strip().split("-")))
        return basket_objects


class BasketBallTeam(SportTeam):
    GAME_CAN_BE_TIE = False
    team_cnt = 0
    fine_amount = 100_000

    # def stat(self):
    #     return f"[Basketball stats]: {super().stat()}"


class FootBallTeam(SportTeam):
    GAME_CAN_BE_TIE = True
    team_cnt = 0
    fine_amount = 20_000

    # def __init__(self, team_name, wins, losses, draws):
    #     super().__init__(team_name, wins, losses)
    #     self.draws = draws

    # def stat(self):
    #     return f"[Foottball stats]: {super().stat()} {utils.pluralize(self.draws, 'draw')}"


class BaseBallTeam(SportTeam):
    GAME_CAN_BE_TIE = False
    team_cnt = 0

    # def stat(self):
    #     return f"[Baseball stats]: {super().stat()} " + utils.pluralize(self.draws, 'draw')


class VolleyBallTeam(SportTeam):
    pass


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


# print(basket_team_4[1].total_fines)
# basket_team_4[1].get_fined()
# print(f"{basket_team_4[1].team} has a total fines of ${basket_team_4[1].total_fines}")

print("==*==" * 15)

foot_team_1 = FootBallTeam.from_file('nfl.txt')
for team in foot_team_1:
    print(team.stat())


print("==*==" * 15)

baseball_team_1 = BaseBallTeam.from_file('baseball.txt')
for team in baseball_team_1:
    print(team.stat())

# print(baseball_team_1[-1].total_fines)
# baseball_team_1[-1].get_fined()
# print(f"{baseball_team_1[-1].team} has a total fines of ${baseball_team_1[-1].total_fines}")


# basket_team_4 = BasketBallTeam.from_file('nba.txt')
# basket_team_4[0].get_fined()
# team_name = basket_team_4[0].team
# team_wins = basket_team_4[0].wins
# team_losses = basket_team_4[0].losses

# print(team_name, team_wins, team_losses)

# team_fines = basket_team_4[0].total_fines
# print(team_fines)
# print(vars(basket_team_4[0]))
# print(basket_team_4[0].fine_amount)
# print(help(basket_team_4[0]))

# print(f"number of sport teams: {SportTeam.team_cnt}")
# print(f"number of basket teams: {BasketBallTeam.team_cnt}")
# print(f"number of foot teams: {FootBallTeam.team_cnt}")
# print(f"number of base teams: {BaseBallTeam.team_cnt}")

print("==*==" * 15)

volley_team1 = VolleyBallTeam("Brazil", 25, 3)
print(volley_team1.stat())
