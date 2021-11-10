def pluralize(total, singular, plural=None):
    assert isinstance(total, int) and total >= 0, "total must be positive"
    if not plural:
        plural = singular + 's'
    string = singular if total <= 1 else plural
    return f"{total} {string}"


def get_basketball_team_stats(team_name, wins, losses):
    return f"[BASKETBALL] STATS: {team_name}: {pluralize(wins, 'victory', 'victories')} - {pluralize(losses, 'defeat')}"


def get_football_team_stats(team_name, wins, losses):
    return f"[FOOTBALL] STATS: {team_name}: {pluralize(wins, 'victory', 'victories')} - {pluralize(losses, 'defeat')}"


if __name__ == "__main__":

    # Basketball teams

    # print(get_basketball_team_stats("Chicago bulls", 89, 25))
    # print(get_basketball_team_stats("Los Angeles Lakers", 95, 1))

    # chicago_stats = "Chicago bulls-19-5"
    # team, win, loss = chicago_stats.split("-")
    # print(get_basketball_team_stats(team, int(win), int(loss)))

    with open('nba.txt', 'r', encoding='utf-8') as f:
    
        for line in f:
            team, win, loss = line.strip().split("-")
            print(get_basketball_team_stats(team, int(win), int(loss)))

    print("=*=" * 20)
    # Football teams
    with open('nfl.txt', 'r', encoding='utf-8') as f:
    
        for line in f:
            team, win, loss = line.strip().split("-")
            print(get_football_team_stats(team, int(win), int(loss)))