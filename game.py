from roll_dice import risk_dice_roll_modified as roll


def attack(attacker, attacker_troops, defender, defender_troops):
    if defender_troops > attacker_troops:
        defender_troops = attacker_troops

    a_loss, d_loss = roll(attacker_troops, attacker.attack_modifications,
                          defender_troops, defender.defence_modifications)
    attacker.troops -= a_loss
    defender.troops -= d_loss
