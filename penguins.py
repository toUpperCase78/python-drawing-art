# PENGUINS
# REFERENCE: https://tr.pinterest.com/pin/714665034665952027/
import numpy as np
import cv2
WIDTH = 720
HEIGHT = 740
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

def draw_small_circle(x, y):
    cv2.circle(img, (x, y), 4, BLACK, -1)

def draw_penguin(x, y):
    line_forward_diagonal(x, y + SIZE * 2, 2)
    line_horizontal(x, y + SIZE * 2)
    line_vertical(x + SIZE, y + SIZE)
    line_horizontal(x + SIZE * 2, y)
    line_back_diagonal(x + SIZE * 3, y)
    line_vertical(x + SIZE * 4, y + SIZE, 7)
    line_horizontal(x + SIZE, y + SIZE * 8, 3)
    line_forward_diagonal(x + SIZE, y + SIZE * 8)
    line_back_diagonal(x + SIZE, y + SIZE * 6)
    line_vertical(x + SIZE, y + SIZE * 4, 2)
    line_forward_diagonal(x + SIZE, y + SIZE * 4)
    line_back_diagonal(x + SIZE, y + SIZE * 2)

    line_back_diagonal(x + SIZE * 2, y)
    line_vertical(x + SIZE * 3, y + SIZE, 2)
    line_forward_diagonal(x + SIZE * 2, y + SIZE * 4)
    line_vertical(x + SIZE * 2, y + SIZE * 4)
    line_back_diagonal(x + SIZE * 2, y + SIZE * 5, 2)
    line_vertical(x + SIZE * 3, y + SIZE * 4, 2)
    line_horizontal(x + SIZE * 2, y + SIZE * 7, 2)
    line_forward_diagonal(x + SIZE * 2, y + SIZE * 8)
    draw_small_circle(x + SIZE * 2, y + SIZE)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 120):
    for j in range(20, HEIGHT, 180):
        draw_penguin(i, j)

cv2.imshow('Penguins', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('penguins_output.jpg', img)
cv2.destroyAllWindows()