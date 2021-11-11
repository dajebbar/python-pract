import utils


class SportTeam:

    fine_amount = 50_000
    team_cnt = 0

    def __init__(self, team_name, wins, losses):
        self.team = team_name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0

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
        return f"{self.team} has {utils.pluralize(self.wins, 'victory', 'victories')} and {utils.pluralize(self.losses, 'defeat')}"

    @classmethod
    def set_fines(cls, amount):
        cls.fine_amount = amount

    @classmethod
    def from_string(cls, stats_as_str, draws=0):
        if draws:
            team, win, loss, draws = stats_as_str.strip().split("-")
            return cls(team, int(win), int(loss), int(draws))

        else:
            team, win, loss = stats_as_str.strip().split("-")
            return cls(team, int(win), int(loss))

    @classmethod
    def from_file(cls, link, draws=0):
        basket_objects = []
        with open(link, 'r', encoding='utf-8') as f:
            for line in f:
                if draws:
                    team, win, loss, draws = line.strip().split("-")
                    basket_objects.append(
                        cls(team, int(win), int(loss), int(draws)))
                else:
                    team, win, loss = line.strip().split("-")
                    basket_objects.append(cls(team, int(win), int(loss)))
        return basket_objects


class BasketBallTeam(SportTeam):
    # def __init__(self, team_name, wins, losses):
    #     super().__init__(team_name, wins, losses)
    team_cnt = 0
    fine_amount = 100_000

    def stat(self):
        return f"[Basketball stats]: {super().stat()}"


class FootBallTeam(SportTeam):
    team_cnt = 0
    fine_amount = 20_000

    def __init__(self, team_name, wins, losses, draws):
        super().__init__(team_name, wins, losses)
        self.draws = draws

    def stat(self):
        return f"[Foottball stats]: {super().stat()} {utils.pluralize(self.draws, 'draw')}"


class BaseBallTeam(SportTeam):
    team_cnt = 0

    def stat(self):
        return f"[Baseball stats]: {super().stat()}"

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

foot_team_1 = FootBallTeam.from_file('nfl.txt', draws='yes')
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
