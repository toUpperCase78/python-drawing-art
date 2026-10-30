# SNAILS
# REFERENCE: https://tr.pinterest.com/pin/521010250653172821/
import numpy as np
import cv2
WIDTH = 660
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

def draw_snail(x, y):
    line_forward_diagonal(x + SIZE, y + SIZE * 2)
    line_horizontal(x + SIZE * 2, y + SIZE, 2)
    line_back_diagonal(x + SIZE * 4, y + SIZE)
    line_vertical(x + SIZE * 5, y + SIZE * 2, 2)
    line_horizontal(x + SIZE * 4, y + SIZE * 4)
    line_vertical(x + SIZE * 4, y + SIZE * 4)
    line_horizontal(x + SIZE * 2, y + SIZE * 5, 2)
    line_back_diagonal(x + SIZE, y + SIZE * 4)
    line_vertical(x + SIZE, y + SIZE * 2, 2)

    line_forward_diagonal(x + SIZE * 2, y + SIZE * 3)
    line_back_diagonal(x + SIZE * 3, y + SIZE * 2)
    line_forward_diagonal(x + SIZE * 3, y + SIZE * 4)
    line_back_diagonal(x + SIZE * 2, y + SIZE * 3)

    line_forward_diagonal(x, y + SIZE * 5)
    line_horizontal(x, y + SIZE * 5, 6)
    line_vertical(x + SIZE * 6, y + SIZE * 2, 3)
    line_horizontal(x + SIZE * 6, y + SIZE * 2)
    line_back_diagonal(x + SIZE * 6, y + SIZE)
    line_forward_diagonal(x + SIZE * 5, y + SIZE * 2)
    line_vertical(x + SIZE * 6, y)
    line_forward_diagonal(x + SIZE * 6, y + SIZE)
    draw_small_circle(x + SIZE * 6, y)
    draw_small_circle(x + SIZE * 7, y)
    draw_small_circle(x + SIZE * 6, y + int(SIZE * 3 / 2))

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 160):
    for j in range(20, HEIGHT, 120):
        draw_snail(i, j)

cv2.imshow('Snails', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('snails_output.jpg', img)
cv2.destroyAllWindows()