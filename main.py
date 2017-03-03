from territory import Territory
import game
import modifications as mods
from table import table
import multiprocessing
from timeit import default_timer as timer
import csv
import sys


def pl(list_):
    for i in list_:
        print i


def base_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops)
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def fort_bunker_case(args, return_queue=None):
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


def fort_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.fortification])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def bunker_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.bunker])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def ammo_shortage_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops)
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.ammo_shortage])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def well_armed_ammo_shortage_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops,
                  attack_modifications=[mods.well_armed])
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.ammo_shortage])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def well_armed_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops,
                  attack_modifications=[mods.well_armed])
    b = Territory("B", "Leon", b_troops)
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def fort_bunker_well_armed_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops,
                  attack_modifications=[mods.well_armed])
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.fortification,
                                         mods.bunker])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def fort_well_armed_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops,
                  attack_modifications=[mods.well_armed])
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.fortification])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def bunker_well_armed_case(args, return_queue=None):
    a_troops = args[0]
    b_troops = args[1]
    a = Territory("A", "Leon", a_troops,
                  attack_modifications=[mods.well_armed])
    b = Territory("B", "Leon", b_troops,
                  defence_modifications=[mods.bunker])
    while(a.attack_max() > 0 and b.defend_max() > 0):
        game.attack(a, a.attack_max(), b, b.defend_max())
    if return_queue is None:
        return a.troops, b.troops
    else:
        return_queue.put([a.troops, b.troops])


def gen_table(max_troops, test_case):
    threads = 100
    processes = 100
    pool = multiprocessing.Pool(processes=16)
    results = []
    for d in range(max_troops):
        row = []
        for a in range(max_troops):
            # print "Testing: " + str(a + 1) + " vs " + str(d + 1)
            player_results = []
            table_results = []

            args = [threads,
                    test_case,
                    [a + 1, d + 1]]

            table_results = pool.map(table, [args] * processes)

            for t in table_results:
                for player in t:
                    player_results.append([player[0],
                                           player[1],
                                           player[0] > player[1]])

            attacker_wins = []
            attacker_win_count = 0
            for i in player_results:
                if i[2]:
                    attacker_win_count += 1
                    attacker_wins.append(i)

            if attacker_win_count == 0:
                row.append([0, 0, a + 1, d + 1])
            else:
                win_median = 0
                win_mean = 0
                for i in attacker_wins:
                    win_mean += i[0]
                win_mean = float(win_mean) / float(len(attacker_wins))
                # win_mode = 0
                attacker_wins = sorted(attacker_wins, key=lambda win: win[0])
                win_median = attacker_wins[len(attacker_wins) / 2][0]
                win_percentage = float(attacker_win_count) / \
                    float(len(player_results))
                row.append([win_percentage, win_median, a + 1, d + 1])
        results.append(row)
    return results


def write_csv(table, file_name):
    file_string = ''
    headers = 'Attacker Win Percentage'
    row_strings = []
    for cell in table[0]:
        headers = headers + "," + \
            str(cell[2]) + " Attackers" + "," + "Median Troops Remaining"

    file_string = headers + "\n"

    for row in table:
        row_title = str(row[0][3]) + " Defenders"
        row_string = row_title
        for cell in row:
            row_string = row_string + "," + str(cell[0]) + "," + str(cell[1])
        # print row_cell
        file_string = file_string + row_string + "\n"
        # print file_string

    file_ = open(file_name, 'w')
    file_.write(file_string)
    file_.close()


def main(args=None):
    """The Main function"""
    start = timer()
    # pl(table)
    # write_csv(gen_table(5, fort_bunker_case), "test.csv")
    # write_csv(gen_table(30, fort_bunker_case), "fort_bunker_case.csv")
    # write_csv(gen_table(30, fort_case), "fort_case.csv")
    # write_csv(gen_table(30, bunker_case), "bunker_case.csv")
    # write_csv(gen_table(30, ammo_shortage_case), "ammo_shortage_case.csv")
    # write_csv(gen_table(30, well_armed_ammo_shortage_case),
    #           "well_armed_ammo_shortage_case.csv")
    # print "Starting fort_bunker_well_armed_case"
    # write_csv(gen_table(30, fort_bunker_well_armed_case),
    #           "fort_bunker_well_armed_case.csv")
    # print "Starting fort_well_armed_case"
    # write_csv(gen_table(30, fort_well_armed_case),
    #           "fort_well_armed_case.csv")
    # print "Starting bunker_well_armed_case"
    # write_csv(gen_table(30, bunker_well_armed_case),
    #           "bunker_well_armed_case.csv")
    # print "Starting well_armed_case"
    # write_csv(gen_table(30, well_armed_case),
    #           "well_armed_case.csv")
    print "Starting base_case"
    write_csv(gen_table(30, base_case),
              "base_case.csv")
    end = timer()
    print "Run Time:       ", (end - start)


if __name__ == '__main__':
    main()
