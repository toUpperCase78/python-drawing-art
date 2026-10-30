# REPEATABLE PATTERN 9
# REFERENCE: https://tr.pinterest.com/pin/714665034665920388/
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

def draw_northwest_arrow(x, y):
    line_horizontal(x, y, 2)
    line_vertical(x, y, 2)
    line_back_diagonal(x, y, 2)

def draw_northeast_arrow(x, y):
    line_horizontal(x, y, 2)
    line_vertical(x + SIZE * 2, y, 2)
    line_forward_diagonal(x, y + SIZE * 2, 2)

def draw_southwest_arrow(x, y):
    line_vertical(x, y, 2)
    line_horizontal(x, y + SIZE * 2, 2)
    line_forward_diagonal(x, y + SIZE * 2, 2)

def draw_southeast_arrow(x, y):
    line_vertical(x + SIZE * 2, y, 2)
    line_horizontal(x, y + SIZE * 2, 2)
    line_back_diagonal(x, y, 2)

def draw_all_squares(x, y):
    draw_square(x + SIZE * 4, y)
    draw_square(x + SIZE * 5, y)
    draw_square(x + SIZE * 2, y + SIZE * 2)
    draw_square(x + SIZE * 7, y + SIZE * 2)
    draw_square(x, y + SIZE * 4)
    draw_square(x + SIZE * 9, y + SIZE * 4)
    draw_square(x, y + SIZE * 5)
    draw_square(x + SIZE * 9, y + SIZE * 5)
    draw_square(x + SIZE * 2, y + SIZE * 7)
    draw_square(x + SIZE * 7, y + SIZE * 7)
    draw_square(x + SIZE * 4, y + SIZE * 9)
    draw_square(x + SIZE * 5, y + SIZE * 9)

def draw_intermediate_lines(x, y):
    line_forward_diagonal(x + SIZE, y + SIZE * 4)
    line_forward_diagonal(x + SIZE * 3, y + SIZE * 2)
    line_back_diagonal(x + SIZE * 6, y + SIZE)
    line_back_diagonal(x + SIZE * 8, y + SIZE * 3)
    line_forward_diagonal(x + SIZE * 8, y + SIZE * 7)
    line_forward_diagonal(x + SIZE * 6, y + SIZE * 9)
    line_back_diagonal(x + SIZE * 3, y + SIZE * 8)
    line_back_diagonal(x + SIZE, y + SIZE * 6)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH-SIZE, 200):
    for j in range(20, HEIGHT-SIZE, 200):
        draw_northwest_arrow(i, j)
        draw_northeast_arrow(i+160, j)
        draw_southwest_arrow(i, j+160)
        draw_southeast_arrow(i+160, j+160)
        draw_all_squares(i, j)
        draw_southeast_arrow(i+60, j+60)
        draw_southwest_arrow(i+100, j+60)
        draw_northeast_arrow(i+60, j+100)
        draw_northwest_arrow(i+100, j+100)
        draw_intermediate_lines(i ,j)

cv2.imshow('Repeatable Pattern 9', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern9_output.jpg', img)
cv2.destroyAllWindows()