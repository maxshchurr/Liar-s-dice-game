from game_config import quantity_of_bots, quantity_of_dices
from player.player import Player, HumanPlayer


class Game:
    def __init__(self, quantity_of_bots: int, dices: int):
        self._players = []
        self._quantity_of_bots = quantity_of_bots
        self._quantity_of_dices = dices

    def create_human_player(self, name):
        name = 'Human Player'
        human = HumanPlayer(name=name, dices=self._quantity_of_dices)
        self._players.append(human)

    def create_bot_players(self):
        for i in range(self._quantity_of_bots):
            new_bot = Player(dices=self._quantity_of_dices)
            self._players.append(new_bot)

    def get_players(self):
        return [player for player in self._players]

    def get_players_names(self):
        return [player.get_player_name() for player in self._players]

    # maybe store the result in a class variable?
    def count_face_values_on_dices_for_all_players(self) -> dict:
        face_values_on_dices_for_all_players = {face_value: 0 for face_value in range(1, 7)}

        for player in self._players:
            players_hand = player.get_current_hand()
            for k in players_hand.keys():
                face_values_on_dices_for_all_players[k] += players_hand[k]

        return face_values_on_dices_for_all_players


if __name__ == "__main__":
    game = Game(quantity_of_bots, quantity_of_dices)

    game.create_bot_players()
    game.create_human_player('Max')
    players = game.get_players()

    for player in players:
        player.throw_dices()
        print(player.get_player_name(), player.get_current_hand())

    print(game.count_face_values_on_dices_for_all_players())
