# REPEATABLE PATTERN 5
# REFERENCE: https://tr.pinterest.com/pin/714665034665836022/
import numpy as np
import cv2
WIDTH = 720
HEIGHT = 720
SIZE = 20
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(0, HEIGHT, SIZE * 3):
    cv2.line(img, (0, i), (WIDTH, i), BLACK, 2)
for i in range(0, WIDTH, SIZE * 3):
    cv2.line(img, (i, 0), (i, HEIGHT), BLACK, 2)

for i in range(0, WIDTH, SIZE * 3):
    for j in range(0, HEIGHT, SIZE * 3):
        line_horizontal(i, j + SIZE, 2)
        line_vertical(i + SIZE * 2, j, 2)
        line_horizontal(i + SIZE, j + SIZE * 2, 2)
        line_vertical(i + SIZE, j + SIZE, 2)

cv2.imshow('Repetable Pattern 5', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('rept_pattern5_output.jpg', img)
cv2.destroyAllWindows()