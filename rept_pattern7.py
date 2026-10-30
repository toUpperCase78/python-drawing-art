# REPEATABLE PATTERN 7
# REFERENCE: https://tr.pinterest.com/pin/714665034665920394/
import numpy as np
import cv2
WIDTH = 820
HEIGHT = 820
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

def draw_polygon1(x, y):
    line_horizontal(x + SIZE, y)
    line_back_diagonal(x + SIZE * 2, y)
    line_vertical(x + SIZE * 3, y + SIZE, 2)
    line_horizontal(x + SIZE, y + SIZE * 3, 2)
    line_back_diagonal(x, y + SIZE * 2)
    line_vertical(x, y + SIZE)
    line_horizontal(x, y + SIZE)
    line_vertical(x + SIZE, y)

def draw_polygon2(x, y):
    line_forward_diagonal(x, y + SIZE)
    line_horizontal(x + SIZE, y)
    line_vertical(x + SIZE * 2, y)
    line_horizontal(x + SIZE * 2, y + SIZE)
    line_vertical(x + SIZE * 3, y + SIZE)
    line_forward_diagonal(x + SIZE * 2, y + SIZE * 3)
    line_horizontal(x, y + SIZE * 3, 2)
    line_vertical(x, y + SIZE, 2)

def draw_polygon3(x, y):
    line_forward_diagonal(x, y + SIZE)
    line_horizontal(x + SIZE, y, 2)
    line_vertical(x + SIZE * 3, y, 2)
    line_forward_diagonal(x + SIZE * 2, y + SIZE * 3)
    line_horizontal(x + SIZE * 1, y + SIZE * 3)
    line_vertical(x + SIZE, y + SIZE * 2)
    line_horizontal(x, y + SIZE * 2)
    line_vertical(x, y + SIZE)

def draw_polygon4(x, y):
    line_horizontal(x, y, 2)
    line_back_diagonal(x + SIZE * 2, y)
    line_vertical(x + SIZE * 3, y + SIZE)
    line_horizontal(x + SIZE * 2, y + SIZE * 2)
    line_vertical(x + SIZE * 2, y + SIZE * 2)
    line_horizontal(x + SIZE, y + SIZE * 3)
    line_back_diagonal(x, y + SIZE * 2)
    line_vertical(x, y, 2)

def draw_cross(x, y):
    line_back_diagonal(x, y, 3)
    line_forward_diagonal(x, y + SIZE * 3, 3)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 160):
    for j in range(20, HEIGHT, 160):
        draw_polygon1(i, j)
        draw_polygon2(i + SIZE * 4, j)
        draw_polygon3(i, j + SIZE * 4)
        draw_polygon4(i + SIZE * 4, j + SIZE * 4)
        draw_cross(i + SIZE * 2, j + SIZE * 2)

for i in range(160, WIDTH-SIZE, 160):
    for j in range(80, HEIGHT-SIZE, 160):
        draw_square(i, j)

for i in range(80, WIDTH-SIZE, 80):
    for j in range(160, HEIGHT-SIZE, 160):
        draw_square(i, j)

cv2.imshow('Repeatable Pattern 7', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern7_output.jpg', img)
cv2.destroyAllWindows()