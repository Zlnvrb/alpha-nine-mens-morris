# Alpha Zero applied to nine men's morris

## Testing
To try a game go to ```pit.py```.
Set ```testing = True``` for the game board to be shown in the terminal, otherwise it is written to a file.

Set one of the following to True. This chooses the opponent for the model. 

```human_vs_cpu``` 

```random_play ```

```greedy_play ```

To play against it yourself set ```human_vs_cpu = True```.
If you set all to False, the model will play against itself.

Note:  You can have any combination of players when defining ```arena```.

```games_to_play``` controls how many games to play - this has to be an even number, as arena compare is done by having both players start as player 1 an equal amount of games.

## Training
To train the model set the parameters in ```main.py``` and run this.