import itertools
import logging

import torch

from main import main
from utils import dotdict

log = logging.getLogger(__name__)
FILE_NAME = "grid_search.txt"
# Define fixed parameters
params_predef = dotdict({
    'numIters': 5,
    'numEps': 100,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 30000,
    'numMCTSSims': 30,
    'arenaCompare': 20,
    'numItersForTrainExamplesHistory': 10,
    'load_model': False,
})

# Define grid search values for specified parameters
grid_values = {
    'tempThreshold': [10],
    'cpuct': [1.0]
}

# Generate all combinations of grid values
param_combinations = list(itertools.product(
    grid_values['tempThreshold'],
    grid_values['cpuct']
))


# Function to train and evaluate a model with given parameters
def get_params(tempThreshold, cpuct, fixed_params, i):
    # Update the parameters dictionary with current grid values

    params = dotdict({
        'numIters': 5,
        'numEps': 100,
        'updateThreshold': 0.6,
        'maxlenOfQueue': 30000,
        'numMCTSSims': 30,
        'arenaCompare': 20,
        'numItersForTrainExamplesHistory': 10,
        'load_model': False,
        'tempThreshold' : tempThreshold,
        'cpuct': cpuct,
        'checkpoint': './grid_search_models' + '_' + str(i) + '/'
    })

    return params


def main_train():
    i = 0
    for tempThreshold, cpuct in param_combinations:
        params = get_params(tempThreshold, cpuct, params_predef, 7)
        with open(FILE_NAME, "a") as file:
            file.write('-------- PARAMETERS (tt, cpuct) : %d, %f\n' % (tempThreshold, cpuct))

        # log.info(params)

        # train on these params
        main(params) 
        with open(FILE_NAME, "a") as file:
            file.write('\n')

        i += 1


if __name__ == "__main__":
    main_train()
