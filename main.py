import logging

import coloredlogs

from Coach import Coach
from ninemensmorris.NineMensMorrisGame import  NineMensMorrisGame
from ninemensmorris.pytorch.NNet import NNetWrapper
from utils import *


log = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

args = dotdict({
    'numIters': 5,  # default 1000 -> takes too long
    'numEps': 60,  # Number of complete self-play games to simulate during a new iteration. default 100
    'tempThreshold': 15,  # default 15
    'updateThreshold': 0.1,
    # During arena playoff, new neural net will be accepted if threshold or more of games are won. default 0.6
    'maxlenOfQueue': 512,  # Number of game examples to train the neural networks. default 200000
    'numMCTSSims': 200,  # Number of games moves for MCTS to simulate. default 25
    'arenaCompare': 20,
    # Number of games to play during arena play to determine if new net will be accepted. default 40
    'cpuct': 2.4,  # default 1

    'checkpoint': './models/',
    'load_model': False,
    'load_folder_file': ('./models/', 'best.pth.tar'),
    'numItersForTrainExamplesHistory': 100,

})


def main():
    log.info('Loading %s...', NineMensMorrisGame.__name__)
    g = NineMensMorrisGame()

    log.info('Loading %s...', NNetWrapper.__name__)
    nnet = NNetWrapper(g)
    if args.load_model:
        log.info('Loading checkpoint "%s/%s"...', args.load_folder_file[0], args.load_folder_file[1])
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process 🎉')

    c.learn()

if __name__ == "__main__":
    main()
