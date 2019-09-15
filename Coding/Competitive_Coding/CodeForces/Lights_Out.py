# Lenny is playing a game on a 3 × 3 grid of lights. In the beginning of the game all lights are switched on.
# Pressing any of the lights will toggle it and all side-adjacent lights. The goal of the game is to switch all the
# lights off. We consider the toggling as follows: if the light was switched on then it will be switched off,
# if it was switched off then it will be switched on.

# Lenny has spent some time playing with the grid and by now he has pressed each light a certain number of times.
# Given the number of times each light is pressed, you have to print the current state of each light.

# Input
# The input consists of three rows. Each row contains three integers each between 0 to 100 inclusive.
# The j-th number in the i-th row is the number of times the j-th light of the i-th row of the grid is pressed.

# Output
# Print three lines, each containing three characters. The j-th character of the i-th line is "1" if and only
# if the corresponding light is switched on, otherwise it's "0".

# Examples
# input
#   1 0 0
#   0 0 0
#   0 0 1
# output
#   001
#   010
#   100
# input
#   1 0 1
#   8 8 8
#   2 0 3
# output
#   010
#   011
#   100

grid = [[1 for j in range(3)] for i in range(3)]
i_grid = []
for _ in range(3):
    i_grid.append(list(map(int, input().split())))
for i in range(3):
    for j in range(3):
        if i_grid[i][j] != 0:
            if i_grid[i][j] % 2 != 0:  # taking care of only odd no's as even no's produce same result alternatively.
                grid[i][j] = 1 if grid[i][j] == 0 else 0
                if j + 1 < 3:
                    # print("grid[", i, "][", j+1, "]")
                    grid[i][j+1] = 1 if grid[i][j+1] == 0 else 0
                if j - 1 >= 0:
                    # print("grid[", i, "][", j-1, "]")
                    grid[i][j-1] = 1 if grid[i][j-1] == 0 else 0
                if i - 1 >= 0:
                    # print("grid[", i-1, "][", j, "]")
                    grid[i-1][j] = 1 if grid[i-1][j] == 0 else 0
                if i + 1 < 3:
                    # print("grid[", i+1, "][", j, "]")
                    grid[i+1][j] = 1 if grid[i+1][j] == 0 else 0
for i in grid:
    for j in i:
        print(j, end="")
    print()