class Territory:
    '''A risk territory'''

    territory_count = 0

    def __init__(self, name, owner, troops=0, scar=None, pop=1, neighbors=[],
                 attack_modifications=[], defence_modifications=[]):
        self.name = name
        self.owner = owner
        self.troops = troops
        self.scar = scar
        self.pop = pop
        self.neighbors = neighbors
        self.attack_modifications = attack_modifications
        self.defence_modifications = defence_modifications
        Territory.territory_count += 1

    def status(self):
        print "Name: " + self.name + " Owner: " + self.owner
        print "Troops: " + str(self.troops)

    def attack_max(self):
        attackers = self.troops - 1
        if attackers > 3:
            attackers = 3
        return attackers

    def defend_max(self):
        defenders = self.troops
        if defenders > 2:
            defenders = 2
        return defenders
