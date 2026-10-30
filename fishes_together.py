# FISHES TOGETHER
# REFERENCE: https://tr.pinterest.com/pin/515943701082988334/
import numpy as np
import cv2
WIDTH = 800
HEIGHT = 675
SIZE = 25
BLACK = (0, 0, 0)

def draw_fish_t1(x, y):
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE), (x + SIZE * 5, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y), (x + SIZE * 5, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 2), (x + SIZE * 5, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 3), (x + SIZE * 5, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 4), (x + SIZE * 4, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 3), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.circle(img, (x + int(SIZE * 3/2), y + int(SIZE * 3/2)), 8, BLACK, -1)

def draw_fish_t2(x, y):
    cv2.line(img, (x, y), (x + SIZE, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE), (x + SIZE * 3, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y), (x + SIZE * 5, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 2), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 4), (x + SIZE, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 3), (x, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 4), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE , y + SIZE * 2), (x, y + SIZE), BLACK, 2)
    cv2.line(img, (x, y + SIZE), (x, y), BLACK, 2)
    cv2.circle(img, (x + int(SIZE * 7/2), y + int(SIZE * 3/2)), 8, BLACK, -1)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(25, WIDTH-100, 100):
    for j in range(25, HEIGHT-100, 150):
        draw_fish_t1(i, j)

for i in range(50, WIDTH-100, 100):
    for j in range(100, HEIGHT-100, 150):
        draw_fish_t2(i, j)

cv2.imshow('Fishes Together', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('fishes_together_output.jpg', img)
cv2.destroyAllWindows()