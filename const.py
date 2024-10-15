BOUND = 10
A1 = 1 # the space between 2 bricks (don't mind it)
COLS, ROWS = 100, 20
MAX_WIDTH = 1000
MAX_HEIGHT = 600
A = (MAX_HEIGHT / ROWS) if (MAX_WIDTH / COLS) > (MAX_HEIGHT / ROWS) else (MAX_WIDTH / COLS)  # edge length of node
RES = WIDTH, HEIGHT = 2*BOUND + (COLS-1)*A1 + COLS * A, 2*BOUND + (ROWS-1)*A1 + ROWS * A

GREY = (100, 100, 100)
WHITE = (255, 255, 255) # path
RED = (200, 0, 0)  # discovered node
BLUE = (30, 144, 255)  # completed node (item of closed set)
PURPLE = (138, 43, 226) # goal
ORANGE = (255,165,0) # start
BLACK = (0, 0, 0) # brick