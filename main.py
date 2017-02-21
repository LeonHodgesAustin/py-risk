from territory import Territory
import game
import modifications as mods
from table import table
import multiprocessing
from timeit import default_timer as timer


def pl(list_):
    for i in list_:
        print i


def test_conquer_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.fortification,
                                         mods.bunker])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def main(args=None):
    """The Main function"""
    test_cases = 100
    # results = []
    # a.status()
    # b.status()
    # for i in range(test_cases):
    #     a = Territory("A", "Leon", 10)
    #     b = Territory("B", "Leon", 4, attack_modifications=[mods.nuke],
    #                   defence_modifications=[mods.fortification,
    #                                          mods.bunker])
    #     r_a, r_b = test_conquer_case(a, b)
    #     results.append([r_a, r_b, r_a > r_b])
    #
    # attacker_wins = 0
    # for i in results:
    #     if i[2]:
    #         attacker_wins += 1
    # print "Attacker Wins: " + str(attacker_wins)
    # print "out of: " + str(len(results))
    # win_percentage = float(attacker_wins) / float(len(results)) * 100
    # print "or: " + str(win_percentage)
    # pl(results)

    player_results = []
    table_results = []

    args = [test_cases,
            test_conquer_case,
            [12, 4]]

    # test = table(args)
    # print test

    pool = multiprocessing.Pool(processes=20)

    start = timer()
    table_results = pool.map(table, [args]*test_cases)
    end = timer()
    for t in table_results:
        for player in t:
            player_results.append([player[0],
                                   player[1],
                                   player[0] > player[1]])

    # for i in range(10):
    #     print player_results[i]

    print "Runs: " + str(len(player_results))
    attacker_wins = 0
    for i in player_results:
        if i[2]:
            attacker_wins += 1
    print "Attacker Wins: " + str(attacker_wins)
    print "out of: " + str(len(player_results))
    win_percentage = float(attacker_wins) / float(len(player_results)) * 100
    print "or: " + str(win_percentage)

    print "Run Time:       ", (end - start)


if __name__ == '__main__':
    main()
