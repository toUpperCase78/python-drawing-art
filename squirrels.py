# SQUIRRELS
# REFERENCE: https://tr.pinterest.com/pin/497718196318987495/
import numpy as np
import cv2
WIDTH = 800
HEIGHT = 720
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

def line_back_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 2), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_three_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 3), BLACK, 2)

def draw_small_circle(x, y):
    cv2.circle(img, (x, y), 4, BLACK, -1)

def draw_squirrel(x, y):
    line_forward_diagonal(x + SIZE, y + SIZE)
    line_forward_diagonal_three_by_one(x, y + SIZE * 4)
    line_back_diagonal_two_by_one(x, y + SIZE * 4)
    line_back_diagonal_one_by_two(x + SIZE, y + SIZE * 6)
    line_horizontal(x + SIZE * 3, y + SIZE * 7)
    line_back_diagonal(x + SIZE * 3, y + SIZE * 6)
    line_horizontal(x + SIZE * 2, y + SIZE * 6)
    line_back_diagonal(x + SIZE, y + SIZE * 5)
    line_vertical(x + SIZE, y + SIZE * 4)
    line_forward_diagonal(x + SIZE, y + SIZE * 4)
    line_forward_diagonal_one_by_two(x + SIZE * 2, y + SIZE * 3)
    line_vertical(x + SIZE * 4, y + SIZE)
    line_back_diagonal(x + SIZE * 3, y)
    line_horizontal(x + SIZE * 2, y)

    line_vertical(x + SIZE * 3, y + SIZE * 5)
    line_forward_diagonal(x + SIZE * 3, y + SIZE * 5, 2)
    line_vertical(x + SIZE * 5, y, 3)
    line_back_diagonal(x + SIZE * 5, y)
    line_vertical(x + SIZE * 6, y)
    line_back_diagonal(x + SIZE * 6, y, 2)
    line_forward_diagonal(x + SIZE * 7, y + SIZE * 3)
    line_vertical(x + SIZE * 7, y + SIZE * 3)
    line_back_diagonal(x + SIZE * 7, y + SIZE * 4)
    line_horizontal(x + SIZE * 6, y + SIZE * 5, 2)
    line_vertical(x + SIZE * 7, y + SIZE * 5)
    line_back_diagonal(x + SIZE * 7, y + SIZE * 6)
    line_horizontal(x + SIZE * 4, y + SIZE * 7, 4)
    draw_small_circle(x + SIZE * 7, y + SIZE * 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 200):
    for j in range(20, HEIGHT, 180):
        draw_squirrel(i, j)

cv2.imshow('Squirrels', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('squirrels_output.jpg', img)
cv2.destroyAllWindows()