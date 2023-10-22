from faker import Faker


class Player:
    is_human = False

    def __init__(self, **kwargs):
        fake = Faker()
        self.name = kwargs.get('name', fake.name())
        self.dices = kwargs.get('dices', 5)


class HumanPlayer(Player):

    def __init__(self, name: str, dices: int):
        super().__init__(name=name, dices=dices)
        self.is_human = True
