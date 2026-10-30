# REPEATABLE PATTERN 3
# REFERENCE: https://tr.pinterest.com/pin/714665034665556673/
import numpy as np
import cv2
WIDTH = 840
HEIGHT = 840
SIZE = 20
BLACK = (0, 0, 0)

def draw_top_shape(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 3, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y), (x + SIZE * 5, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y), (x + SIZE * 6, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 6, y + SIZE), (x + SIZE * 8, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 2), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 5, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 2), (x + SIZE * 7, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 7, y + SIZE * 2), (x + SIZE * 8, y + SIZE), BLACK, 2)

def draw_left_shape(x, y):
    cv2.line(img, (x + SIZE, y), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 5), (x + SIZE, y + SIZE * 6), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 6), (x + SIZE, y + SIZE * 8), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 4), (x + SIZE, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x + SIZE, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 4), (x + SIZE * 2, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 5), (x + SIZE * 2, y + SIZE * 7), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 7), (x + SIZE, y + SIZE * 8), BLACK, 2)

def draw_right_shape(x, y):
    cv2.line(img, (x + SIZE, y), (x, y + SIZE), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x + SIZE, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 4), (x, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 5), (x, y + SIZE * 7), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 7), (x + SIZE, y + SIZE * 8), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x + SIZE * 2, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 5), (x + SIZE, y + SIZE * 6), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 6), (x + SIZE, y + SIZE * 8), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 4), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)

def draw_bottom_shape(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE, y), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE * 3, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 5, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y), (x + SIZE * 7, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 7, y), (x + SIZE * 8, y + SIZE), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 2), (x + SIZE * 5, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 2), (x + SIZE * 6, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 6, y + SIZE), (x + SIZE * 8, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)

def draw_middle_shape(x, y):
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 2), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 2), (x + SIZE * 5, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 2), (x + SIZE * 4, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 3), (x + SIZE * 5, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 4), (x + SIZE * 4, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 4), (x + SIZE * 4, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 5), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 4), (x + SIZE * 2, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 5), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 4), (x + SIZE, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 4), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x + SIZE, y + SIZE * 2), BLACK, 2)

def draw_vertical_short(x, y):
    cv2.line(img, (x, y), (x, y + SIZE), BLACK, 2)

def draw_horizontal_short(x, y):
    cv2.line(img, (x, y), (x + SIZE, y), BLACK, 2)

def draw_vertical_long(x, y):
    cv2.line(img, (x, y), (x, y + SIZE * 3), BLACK, 2)

def draw_horizontal_long(x, y):
    cv2.line(img, (x, y), (x + SIZE * 3, y), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH-SIZE, 200):
    for j in range(20, HEIGHT-SIZE, 200):
        draw_top_shape(i+20, j)
        draw_left_shape(i, j+20)
        draw_right_shape(i+160, j+20)
        draw_bottom_shape(i+20, j+160)
        draw_middle_shape(i+40, j+40)

for i in range(60, WIDTH, 200):
    for j in range(60, HEIGHT, 200):
        draw_vertical_short(i+60, j)
        draw_vertical_short(i+60, j+100)
        draw_horizontal_short(i, j+60)
        draw_horizontal_short(i+100, j+60)

for i in range(20, WIDTH, 200):
    for j in range(20, HEIGHT-SIZE, 200):
        draw_vertical_long(i, j)
        draw_vertical_long(i, j+140)

for i in range(20, WIDTH-SIZE, 200):
    for j in range(20, HEIGHT, 200):
        draw_horizontal_long(i, j)
        draw_horizontal_long(i+140, j)

cv2.imshow('Repetable Pattern 3', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern3_output.jpg', img)
cv2.destroyAllWindows()