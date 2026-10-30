# REPEATABLE PATTERN 2
# REFERENCE: https://tr.pinterest.com/pin/1131107262696787616/
import numpy as np
import cv2
WIDTH = 800
HEIGHT = 800
SIZE = 20
BLACK = (0, 0, 0)

def draw_hexagon_t1(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE, y), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 2, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x + SIZE, y + SIZE *3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE, y + SIZE *3), BLACK, 2)

def draw_hexagon_t2(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE, y), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 3, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE * 3, y + SIZE), BLACK, 2)

def draw_plus(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE, y + SIZE * 2), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(60, WIDTH, 160):
    for j in range(20, HEIGHT, 160):
        draw_hexagon_t1(i, j)
        draw_hexagon_t1(i, j+60)
        draw_hexagon_t2(i-40, j+40)
        draw_hexagon_t2(i+20, j+40)

for i in range(-20, WIDTH, 160):
    for j in range(-60, HEIGHT, 160):
        draw_hexagon_t1(i, j)
        draw_hexagon_t1(i, j+60)
        draw_hexagon_t2(i-40, j+40)
        draw_hexagon_t2(i+20, j+40)

for i in range(-20, WIDTH, 80):
    for j in range(-20, HEIGHT, 80):
        draw_plus(i, j)

cv2.imshow('Repetable Pattern 2', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern2_output.jpg', img)
cv2.destroyAllWindows()