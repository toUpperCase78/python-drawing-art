# REPEATABLE PATTERN 8
# REFERENCE: https://tr.pinterest.com/pin/845480530032400630/
import numpy as np
import cv2
WIDTH = 840
HEIGHT = 840
SIZE = 20
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def draw_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def draw_cross(x, y):
    line_back_diagonal(x, y, 4)
    line_forward_diagonal(x, y + SIZE * 4, 4)

def draw_diamond(x, y):
    line_forward_diagonal(x, y + SIZE)
    line_back_diagonal(x + SIZE, y)
    line_forward_diagonal(x + SIZE, y + SIZE * 2)
    line_back_diagonal(x, y + SIZE)

def draw_outer_shape(x, y):
    line_horizontal(x, y, 4)
    line_back_diagonal(x + SIZE * 4, y)
    line_forward_diagonal(x + SIZE * 5, y + SIZE)
    line_vertical(x + SIZE * 5, y + SIZE)
    line_horizontal(x + SIZE * 6, y, 4)
    line_vertical(x + SIZE * 10, y, 4)
    line_forward_diagonal(x + SIZE * 9, y + SIZE * 5)
    line_back_diagonal(x + SIZE * 9, y + SIZE * 5)
    line_horizontal(x + SIZE * 8, y + SIZE * 5)
    line_vertical(x + SIZE * 10, y + SIZE * 6, 4)
    line_horizontal(x + SIZE * 6, y + SIZE * 10, 4)
    line_back_diagonal(x + SIZE * 5, y + SIZE * 9)
    line_forward_diagonal(x + SIZE * 4, y + SIZE * 10)
    line_vertical(x + SIZE * 5, y + SIZE * 8)
    line_horizontal(x, y + SIZE * 10, 4)
    line_vertical(x, y + SIZE * 6, 4)
    line_forward_diagonal(x, y + SIZE * 6)
    line_back_diagonal(x, y + SIZE * 4)
    line_horizontal(x + SIZE, y + SIZE * 5)
    line_vertical(x, y, 4)

def draw_inner_shape(x, y):
    line_horizontal(x + SIZE, y + SIZE * 3)
    line_back_diagonal(x, y + SIZE * 2)
    line_vertical(x, y, 2)
    line_horizontal(x, y, 2)
    line_back_diagonal(x + SIZE * 2, y)
    line_vertical(x + SIZE * 3, y + SIZE)
    line_vertical(x + SIZE * 5, y + SIZE)
    line_forward_diagonal(x + SIZE * 5, y + SIZE)
    line_horizontal(x + SIZE * 6, y, 2)
    line_vertical(x + SIZE * 8, y, 2)
    line_forward_diagonal(x + SIZE * 7, y + SIZE * 3)
    line_horizontal(x + SIZE * 6, y + SIZE * 3)
    line_horizontal(x + SIZE * 6, y + SIZE * 5)
    line_back_diagonal(x + SIZE * 7, y + SIZE * 5)
    line_vertical(x + SIZE * 8, y + SIZE * 6, 2)
    line_horizontal(x + SIZE * 6, y + SIZE * 8, 2)
    line_back_diagonal(x + SIZE * 5, y + SIZE * 7)
    line_vertical(x + SIZE * 5, y + SIZE * 6)
    line_vertical(x + SIZE * 3, y + SIZE * 6)
    line_forward_diagonal(x + SIZE * 2, y + SIZE * 8)
    line_horizontal(x, y + SIZE * 8, 2)
    line_vertical(x, y + SIZE * 6, 2)
    line_forward_diagonal(x, y + SIZE * 6)
    line_horizontal(x + SIZE, y + SIZE * 5)

def draw_whole_shape(x, y):
    draw_outer_shape(x, y)
    draw_inner_shape(x + SIZE, y + SIZE)
    draw_square(x + SIZE * 2, y + SIZE * 2)
    draw_square(x + SIZE * 7, y + SIZE * 2)
    draw_square(x + SIZE * 2, y + SIZE * 7)
    draw_square(x + SIZE * 7, y + SIZE * 7)
    draw_cross(x + SIZE * 3, y + SIZE * 3)
    draw_diamond(x + SIZE * 4, y + SIZE * 2)
    draw_diamond(x + SIZE * 6, y + SIZE * 4)
    draw_diamond(x + SIZE * 4, y + SIZE * 6)
    draw_diamond(x + SIZE * 2, y + SIZE * 4)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH-SIZE, 200):
    for j in range(20, HEIGHT-SIZE, 200):
        draw_whole_shape(i, j)

cv2.imshow('Repeatable Pattern 8', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern8_output.jpg', img)
cv2.destroyAllWindows()