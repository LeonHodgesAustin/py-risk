import random


def p(msg):
    # print msg
    pass


def risk_dice_roll(attackers, defenders):
    attacker_losses = 0
    defender_losses = 0
    attack_dice = []
    for i in range(attackers):
        attack_dice.append(random.randint(1, 6))
    attack_dice.sort(reverse=True)

    defence_dice = []
    for i in range(defenders):
        defence_dice.append(random.randint(1, 6))
    defence_dice.sort(reverse=True)

    for i in range(defenders):
        if attack_dice[i] <= defence_dice[i]:
            attacker_losses += 1
        else:
            defender_losses += 1

    return attacker_losses, defender_losses


def risk_dice_roll_modified(attackers, attack_modifications,
                            defenders, defence_modifications):
    # print "attackers: " + str(attackers)
    # print "defenders: " + str(defenders)
    attacker_losses = 0
    defender_losses = 0
    attack_dice = []
    for i in range(attackers):
        attack_dice.append(random.randint(1, 6))
    attack_dice.sort(reverse=True)
    for mod in attack_modifications:
        attack_dice = mod(attack_dice)

    p("Attacker: ")
    p(attack_dice)

    defence_dice = []
    for i in range(defenders):
        defence_dice.append(random.randint(1, 6))
    defence_dice.sort(reverse=True)
    for mod in defence_modifications:
        defence_dice = mod(defence_dice)

    p("Defender: ")
    p(defence_dice)

    for i in range(defenders):
        if attack_dice[i] <= defence_dice[i]:
            attacker_losses += 1
        else:
            defender_losses += 1

    p("Result: ")
    p("attacker losses: " + str(attacker_losses))
    p("defender losses: " + str(defender_losses))

    return attacker_losses, defender_losses
