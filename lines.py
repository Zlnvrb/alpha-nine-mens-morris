input = """
0. 7/3/0
1. 8/2/0
2. 9/1/0
3. 8/2/0
4. 10/0/0
5. 10/0/0
6. 9/1/0
7. 6/4/0
8. 8/2/0
9. 7/3/0
"""


def parse_input(input_string):
    # Initialize an empty list to store the parsed elements
    parsed_data = []

    # Split the input string into lines
    lines = input_string.strip().split("\n")

    for line in lines:
        # Split the line on the '.' character to isolate the data after the index
        _, data = line.split('.')
        # Split the data on '/' and convert to integers
        a, b, c = map(int, data.strip().split('/'))
        # Append the tuple (a, b, c) to the list
        parsed_data.append((a, b, c))

    return parsed_data


results = parse_input(input)
# Calculate total wins, losses, and games excluding draws
total_wins = sum(r[0] for r in results)
total_losses = sum(r[1] for r in results)
total_games = total_wins + total_losses

# Calculate win percentage for the model
win_percentage = (total_wins / total_games) * 100
print(win_percentage)
