# BIRDS
# REFERENCE: https://tr.pinterest.com/pin/714665034666272489/
import numpy as np
import cv2
WIDTH = 740
HEIGHT = 640
SIZE = 20
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_back_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y + SIZE * s), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_four_by_three(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 3, y - SIZE * s * 4), BLACK, 2)

def draw_small_plus(x, y):
    cv2.line(img, (x - int(SIZE / 3), y), (x + int(SIZE / 3), y), BLACK, 2)
    cv2.line(img, (x, y - int(SIZE / 3)), (x, y + int(SIZE / 3)), BLACK, 2)

def draw_small_circle(x, y):
    cv2.circle(img, (x, y), 4, BLACK, -1)

def draw_bird(x, y):
    line_vertical(x, y + SIZE * 3)
    line_horizontal(x, y + SIZE * 4, 2)
    line_back_diagonal_one_by_two(x, y + SIZE * 3)

    line_forward_diagonal_four_by_three(x + SIZE * 2, y + SIZE * 4)
    line_back_diagonal(x + SIZE * 5, y)
    line_vertical(x + SIZE * 6, y + SIZE, 2)
    line_forward_diagonal(x + SIZE * 4, y + SIZE * 5, 2)
    line_horizontal(x + SIZE * 3, y + SIZE * 5)
    line_back_diagonal(x + SIZE * 2, y + SIZE * 4)

    line_horizontal(x + SIZE * 6, y + SIZE * 2, 2)
    line_back_diagonal_one_by_two(x + SIZE * 6, y + SIZE)
    line_forward_diagonal(x + SIZE * 3, y + SIZE * 4)
    line_horizontal(x + SIZE * 3, y + SIZE * 4)
    line_forward_diagonal(x + SIZE * 4, y + SIZE * 4)
    line_back_diagonal(x + SIZE * 3, y + SIZE * 5)
    line_back_diagonal(x + SIZE * 4, y + SIZE * 5)
    draw_small_circle(x + SIZE * 5, y + SIZE)
    draw_small_plus(x + SIZE * 4, y + SIZE * 6)
    draw_small_plus(x + SIZE * 5, y + SIZE * 6)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 180):
    for j in range(20, HEIGHT, 160):
        draw_bird(i, j)

cv2.imshow('Birds', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('birds_output.jpg', img)
cv2.destroyAllWindows()