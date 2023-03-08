import json

# Load config file
with open("config.json") as f:
    configs = json.load(f)

resolution = (configs["window_size"][0], configs["window_size"][1])  # Alternate resolutions not working at the moment

block_size = configs["block_size"]

# Centers the board based on window resolution and block size
board_x = resolution[0] / 2 - 5 * block_size
board_y = resolution[1] / 2 + 10 * block_size

score_pos = (board_x - 3 * block_size, board_y)

rotations = configs["rotations"]

kick_table = configs["kick_table"]

scoring_table = configs["scoring_table"]

grid = 1  # Width of board grid (Change later)

showHints = False
