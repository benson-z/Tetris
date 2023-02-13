import json

with open("config.json") as f:
    configs = json.load(f)

resolution = (configs["window_size"][0], configs["window_size"][1])

block_size = configs["block_size"]

# Centers the board based on window resolution and block size
board_x = resolution[0] / 2 - 5 * block_size
board_y = resolution[1] / 2 + 10 * block_size

rotations = configs["rotations"]

grid = 1  # Width of board grid (Change later)
