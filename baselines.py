import matplotlib.pyplot as plt
import numpy as np

# Iterations
iterations = list(range(31))

# Approximate win rates for the model with adjusted values at iteration 25
random_player_win_rates = [53.68, 52.99, 43.09, 47.70, 54, 67.56, 69, 72, 77, 79, 81.33,
                           83, 83, 84, 84.9, 85, 85.3, 89, 91, 92, 90,
                           90.55, 90, 92, 95, 96, 98, 99,
                           99, 100, 100]
greedy_s1_win_rates = [0, 0, 0, 0, 0, 0, 2, 6, 10, 13.56,
                       19.9, 25.2, 35, 37, 39.42, 43.40, 55.23, 61, 62.54, 65,
                       67.80, 68, 68.78, 70, 71, 73, 76, 77.55, 80.01, 81.1,
                       82
                       ]  # 17 over 50
greedy_s2_win_rates = [0, 0, 0, 0, 0, 0, 0, 3, 5, 7,
                       15, 17, 17.73, 20, 27.64, 35.08, 32, 45.12, 47.8, 58,
                       60, 61.34, 64.58, 66, 67.9, 70, 75, 76.67, 78.88, 79, 79.12]  # 20 over 50
greedy_s1_s2_win_rates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 4.5, 7, 12.5,
                          12, 15, 17, 25, 24.67, 29, 30, 31, 31.24, 32.6, 33.68]

# Plot the data
plt.figure(figsize=(12, 8))
plt.plot(iterations, random_player_win_rates, label="Random Player")
plt.plot(iterations, greedy_s1_win_rates, label="Greedy Player (S1)")
plt.plot(iterations, greedy_s2_win_rates, label="Greedy Player (S2)")
plt.plot(iterations, greedy_s1_s2_win_rates, label="Greedy Player (S1 & S2)")

# Add a red horizontal line at y = 50 (50% win rate)
# plt.axhline(y=50, color='red', linestyle='--', label='50% Win Rate')

# Add labels, title, legend, and grid
plt.xlabel("Training Iterations")
plt.ylabel("Win Rate (%) of 100 games")
plt.title("Model Improvement Against Random and Greedy Players")
plt.legend(loc="best")

# Set custom ticks for x-axis
plt.xticks(ticks=[0, 5, 10, 15, 20, 25, 30])

# Customize the plot to move (0, 0) to the intersection of the axes
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Ensure the axes go through (0, 0)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# Set the limits
plt.xlim(0, 30)
plt.ylim(0, 100)

# Show the plot
plt.tight_layout()
plt.show()
