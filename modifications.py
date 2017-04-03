import random


def base(dice):
    return dice


def bunker(dice):
    # print "Bunker"
    dice.sort(reverse=True)
    if dice[0] < 6:
        dice[0] += 1
    dice.sort(reverse=True)
    return dice


def fortification(dice):
    # print "fortification"
    dice.sort(reverse=True)
    if dice[0] < 6:
        dice[0] += 1
    if len(dice) > 1:
        if dice[1] < 6:
            dice[1] += 1
    dice.sort(reverse=True)
    return dice


def ammo_shortage(dice):
    # print "ammo_shortage"
    dice.sort(reverse=True)
    if dice[0] > 1:
        dice[0] -= 1
    dice.sort(reverse=True)
    return dice


def nuke(dice):
    # print "nuke"
    dice.sort()
    dice[0] = 6
    dice.sort(reverse=True)
    return dice


def well_armed(dice):
    # print "well_armed"
    for i in range(len(dice)):
        if dice[i] > 6:
            dice[i] += 1
    dice.sort(reverse=True)
    return dice


def rivalry(dice):
    for i in range(len(dice)):
        if dice[i] == 1:
            dice[i] = random.randint(1, 5) + 1
    dice.sort(reverse=True)
    return dice
