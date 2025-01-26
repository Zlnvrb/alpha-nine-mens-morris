import logging

import coloredlogs

from Coach import Coach
from ninemensmorris.NineMensMorrisGame import  NineMensMorrisGame
from ninemensmorris.pytorch.NNet import NNetWrapper
from utils import *


log = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

args_predef = dotdict({
    'numIters': 30,  # default 1000 -> takes too long
    'numEps': 100,  # Number of complete self-play games to simulate during a new iteration. default 100
    'tempThreshold': 10,  # default 15
    'updateThreshold': 0.6,
    # During arena playoff, new neural net will be accepted if threshold or more of games are won. default 0.6
    'maxlenOfQueue': 30000,  # Number of game examples to train the neural networks. default 200000
    'numMCTSSims': 30,  # Number of games moves for MCTS to simulate. default 25
    'arenaCompare': 20,
    # Number of games to play during arena play to determine if new net will be accepted. default 40
    'cpuct': 1.2,  # default 1

    'checkpoint': './models13/',
    'load_model': True,
    'load_folder_file': ('./models12/', 'best.pth.tar'),
    'numItersForTrainExamplesHistory': 10,

})


def main(args=None):
    if args is None:
        args = args_predef
    # print(args)
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
