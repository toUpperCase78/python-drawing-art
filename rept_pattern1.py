# REPEATABLE PATTERN 1
# REFERENCE: https://tr.pinterest.com/pin/564357397072329614/
import numpy as np
import cv2
WIDTH = 820
HEIGHT = 820
SIZE = 20
BLACK = (0, 0, 0)

def draw_polygon_t1(x, y):
    cv2.line(img, (x, y + SIZE), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x + SIZE, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE, y), (x + SIZE * 3, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)

def draw_polygon_t2(x, y):
    cv2.line(img, (x, y), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 3, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE), (x + SIZE *3, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 3), (x + SIZE * 3, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x + SIZE, y + SIZE *2), BLACK, 2)
    cv2.line(img, (x, y), (x, y + SIZE * 2), BLACK, 2)

def draw_square(x, y):
    cv2.rectangle(img, (x, y), (x + SIZE, y + SIZE), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 160):
    for j in range(20, HEIGHT, 160):
        draw_polygon_t1(i, j)

for i in range(100, WIDTH, 160):
    for j in range(100, HEIGHT, 160):
        draw_polygon_t1(i, j)

for i in range(100, WIDTH, 160):
    for j in range(20, HEIGHT, 160):
        draw_polygon_t2(i, j)

for i in range(20, WIDTH, 160):
    for j in range(100, HEIGHT, 160):
        draw_polygon_t2(i, j)

for i in range(80, WIDTH, 160):
    for j in range(80, HEIGHT, 160):
        draw_square(i, j)

for i in range(160, WIDTH-60, 160):
    for j in range(160, HEIGHT-60, 160):
        draw_square(i, j)

cv2.imshow('Repetable Pattern 1', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern1_output.jpg', img)
cv2.destroyAllWindows()