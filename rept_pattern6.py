# REPEATABLE PATTERN 6
# REFERENCE: https://tr.pinterest.com/pin/1050464681819783285/
import numpy as np
import cv2
WIDTH = 620
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

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH-80, 100):
    for j in range(20, HEIGHT-80, 100):
        draw_square(i, j, 4)
        draw_square(i+20, j+20, 2)
        line_back_diagonal(i, j)
        line_forward_diagonal(i+60, j+20)
        line_back_diagonal(i+60, j+60)
        line_forward_diagonal(i, j+80)

cv2.imshow('Repetable Pattern 6', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern6_output.jpg', img)
cv2.destroyAllWindows()