from territory import Territory
import game
import modifications as mods
from table import table


def pl(list_):
    for i in list_:
        print i


def test_conquer_case(a_troops, b_troops):
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.fortification,
                                         mods.bunker])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    return a.troops, b.troops


def main(args=None):
    """The Main function"""
    test_cases = 10000
    results = []
    # a.status()
    # b.status()
    for i in range(test_cases):
        a = Territory("A", "Leon", 10)
        b = Territory("B", "Leon", 4, attack_modifications=[mods.nuke],
                      defence_modifications=[mods.fortification,
                                             mods.bunker])
        r_a, r_b = test_conquer_case(a, b)
        results.append([r_a, r_b, r_a > r_b])

    attacker_wins = 0
    for i in results:
        if i[2]:
            attacker_wins += 1
    print "Attaker Wins: " + str(attacker_wins)
    print "out of: " + str(len(results))
    win_percentage = float(attacker_wins) / float(len(results)) * 100
    print "or: " + str(win_percentage)
    # pl(results)

    player_results = []
    table_results = []

    args = [test_cases,
            wager_size,
            wager_count,
            roll_dice,
            players_at_table]

    # test = table(args)
    # print test

    pool = multiprocessing.Pool(processes=13)

    start = timer()
    table_results = pool.map(table, [args]*table_count)
    end = timer()
    for t in table_results:
        for player in t:
            player_results.append(player)




if __name__ == '__main__':
    main()
