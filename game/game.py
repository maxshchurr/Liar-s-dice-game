from game_config import quantity_of_bots, quantity_of_dices
from player.player import Player, HumanPlayer


def create_human_player():
    name = 'Human Player'
    human = HumanPlayer(name=name, dices=quantity_of_dices)
    return human


def create_bot_players(quantity_of_bots):
    created_bots = []
    for i in range(quantity_of_bots):
        new_bot = Player(dices=quantity_of_dices)
        created_bots.append(new_bot)

    return created_bots


if __name__ == "__main__":
    player = create_human_player()
    bots = create_bot_players(quantity_of_bots)
