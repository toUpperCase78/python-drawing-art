# HEDGEHOGS
# REFERENCE: https://tr.pinterest.com/pin/302515299969871903/
import numpy as np
import cv2
WIDTH = 820
HEIGHT = 620
SIZE = 20
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_horizontal_small(x, y):
    cv2.line(img, (x, y), (x + int(SIZE / 2), y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_back_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 2), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def draw_small_circle(x, y):
    cv2.circle(img, (x, y), 4, BLACK, -1)

def draw_hedgehog(x, y):
    line_back_diagonal(x, y)
    line_vertical(x + SIZE, y)
    line_back_diagonal(x + SIZE, y)
    line_vertical(x + SIZE * 2, y)
    line_back_diagonal(x + SIZE * 2, y)
    line_vertical(x + SIZE * 3, y)
    line_back_diagonal(x + SIZE * 3, y)
    line_vertical(x + SIZE * 4, y)
    line_back_diagonal(x + SIZE * 4, y, 3)
    line_horizontal(x + SIZE, y + SIZE * 3, 6)
    line_back_diagonal(x, y + SIZE * 2)
    line_horizontal(x, y + SIZE * 2)
    line_back_diagonal_two_by_one(x, y)

    line_forward_diagonal_two_by_one(x + SIZE * 4, y + SIZE * 3)
    draw_small_circle(x + SIZE * 5, y + SIZE * 2)
    line_vertical(x + SIZE, y + SIZE * 3)
    line_horizontal_small(x + SIZE, y + SIZE * 4)
    line_vertical(x + SIZE * 2, y + SIZE * 3)
    line_horizontal_small(x + SIZE * 2, y + SIZE * 4)
    line_vertical(x + SIZE * 3, y + SIZE * 3)
    line_horizontal_small(x + SIZE * 3, y + SIZE * 4)
    line_vertical(x + SIZE * 4, y + SIZE * 3)
    line_horizontal_small(x + SIZE * 4, y + SIZE * 4)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 160):
    for j in range(20, HEIGHT, 100):
        draw_hedgehog(i, j)

cv2.imshow('Hedgehogs', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('hedgehogs_output.jpg', img)
cv2.destroyAllWindows()