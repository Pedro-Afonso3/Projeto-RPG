class Personagem:
    def __init__(self,vida,mana,defesa,dano):
        self.vida = vida
        self.mana = mana
        self.defesa = defesa
        self.dano = dano
        self.sorte = 0
        self.azar = 0

    def ver_azar(self):
        self.azar = self.azar - (self.azar * 2)
        return self.azar

class Heroi(Personagem):
    pass

class Boss(Personagem):
    pass
