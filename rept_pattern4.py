# REPEATABLE PATTERN 4
# REFERENCE: https://tr.pinterest.com/pin/714665034665683146/
import numpy as np
import cv2
WIDTH = 800
HEIGHT = 920
SIZE = 20
BLACK = (0, 0, 0)

def draw_polygon_t1(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 4), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x, y + SIZE), BLACK, 2)

def draw_polygon_t2(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x, y + SIZE), BLACK, 2)

def draw_polygon_t3(x, y):
    cv2.line(img, (x, y + SIZE), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 4, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 3), (x, y + SIZE), BLACK, 2)

def draw_polygon_t4(x, y):
    cv2.line(img, (x, y), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 4), (x, y), BLACK, 2)

def draw_polygon_t5(x, y):
    cv2.line(img, (x + SIZE * 4, y), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x + SIZE * 4, y), BLACK, 2)

def draw_polygon_t6(x, y):
    cv2.line(img, (x, y), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x, y), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH-100, 240):
    for j in range(20, HEIGHT-120, 120):
        draw_polygon_t1(i+40, j)
        draw_polygon_t2(i+80, j+20)
        draw_polygon_t3(i+80, j+60)
        draw_polygon_t4(i+80, j+80)
        draw_polygon_t5(i, j+80)
        draw_polygon_t6(i, j+40)

for i in range(140, WIDTH-100, 240):
    for j in range(80, HEIGHT-120, 120):
        draw_polygon_t1(i+40, j)
        draw_polygon_t2(i+80, j+20)
        draw_polygon_t3(i+80, j+60)
        draw_polygon_t4(i+80, j+80)
        draw_polygon_t5(i, j+80)
        draw_polygon_t6(i, j+40)

cv2.imshow('Repetable Pattern 4', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern4_output.jpg', img)
cv2.destroyAllWindows()