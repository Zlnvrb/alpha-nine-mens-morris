import numpy as np

from Arena import Arena
from MCTS import MCTS
from ninemensmorris.NineMensMorrisGame import NineMensMorrisGame
from ninemensmorris.NineMensMorrisPlayers import RandomPlayer, GreedyNineMensMorrisPlayer, HumanNineMensMorrisPlayer, \
    GreedyS1NineMensMorrisPlayer, GreedyS2NineMensMorrisPlayer
from ninemensmorris.pytorch.NNet import NNetWrapper
from utils import dotdict

games_to_play = 10

g = NineMensMorrisGame()

# all players
rp = RandomPlayer(g).play
gp = GreedyNineMensMorrisPlayer(g).play
gps1 = GreedyS1NineMensMorrisPlayer(g).play
gps2 = GreedyS2NineMensMorrisPlayer(g).play


def get_model(folder):
    n1 = NNetWrapper(g)
    n1.load_checkpoint(folder,
                       'best.pth.tar')
    args1 = dotdict({'numMCTSSims': 30, 'cpuct': 1.0})
    mcts1 = MCTS(g, n1, args1)
    n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=7))
    return n1p


# nnet player last iter
m1 = get_model('./models10_3_2/')
m2 = get_model('./models10_3_1/')
m3 = get_model('./models10_3/')
m4 = get_model('./models10/')
m5 = get_model('./models/')

models = ["m4", "m5"]
models_dict = {
    "m1": m1,
    "m2": m2,
    "m3": m3,
    "m4": m4,
    "m5": m5
}

fileRandom = "modelVsRandom"
fileGreedyS1 = "modelVsGreedyS1"
fileGreedyS2 = "modelVsGreedyS2"
fileGreedy = "modelVsGreedy"

players = ["gp"]

players_dict = {
    "rp": rp,
    "gps1": gps1,
    "gps2": gps2,
    "gp": gp
}

files_dict = {
    "rp": fileRandom,
    "gps1": fileGreedyS1,
    "gps2": fileGreedyS2,
    "gp": fileGreedy
}

for p in players:
    # for each kind of player play 10 rounds of 10 games with each model and save the result to a designated file
    player = players_dict[p]
    for m in models:
        file_name = files_dict[p] + "_" + m
        model = models_dict[m]

        for i in range(10):
            arena = Arena(model, player, g, display=NineMensMorrisGame.display)
            w, l, d = arena.playGames(games_to_play, verbose=False)
            with open(file_name, "a") as file:
                file.write('%d. %d/%d/%d\n' % (i, w, l, d))
