from faker import Faker
import random


class Player:
    is_human = False

    def __init__(self, **kwargs):
        fake = Faker()
        self._name = kwargs.get('name', fake.name())
        self._dices = kwargs.get('dices', 5)
        self._current_hand = {}

    def throw_dices(self):
        dices = [random.randint(1, 6) for dice in range(self._dices)]

        for face_value in range(1, 7):
            if face_value not in dices:
                self._current_hand[face_value] = 0
            else:
                self._current_hand[face_value] = dices.count(face_value)

    def get_current_hand(self) -> dict:
        return self._current_hand

    def get_player_name(self):
        return self._name


class HumanPlayer(Player):

    def __init__(self, name: str, dices: int):
        super().__init__(name=name, dices=dices)
        self.is_human = True
