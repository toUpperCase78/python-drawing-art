# LEAVES
# REFERENCE: https://tr.pinterest.com/pin/714665034665683935/
import numpy as np
import cv2
WIDTH = 840
HEIGHT = 840
SIZE = 20
BLACK = (0, 0, 0)

def draw_leaf(x, y):
    cv2.line(img, (x + SIZE * 2, y), (x + SIZE * 5, y), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y), (x + SIZE * 5, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 5, y + SIZE * 3), (x + SIZE * 4, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 3), (x + SIZE * 4, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 4, y + SIZE * 4), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 4), (x + SIZE * 3, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 5), (x + SIZE * 2, y + SIZE * 5), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 5), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 4), (x + SIZE, y + SIZE * 4), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 4), (x + SIZE, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 3), (x, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 3), (x, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 2), (x + SIZE, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE * 2), (x + SIZE, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE, y + SIZE), (x + SIZE * 2, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 2, y), BLACK, 2)
    cv2.line(img, (x, y + SIZE * 5), (x + SIZE * 4, y + SIZE), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE), (x + SIZE * 3, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 3, y + SIZE * 2), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 2), (x + SIZE * 2, y + SIZE * 3), BLACK, 2)
    cv2.line(img, (x + SIZE * 2, y + SIZE * 3), (x + SIZE * 3, y + SIZE * 3), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

for i in range(20, WIDTH, 140):
    for j in range(20, HEIGHT, 140):
        draw_leaf(i, j)

cv2.imshow('Leaves', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('leaves_output.jpg', img)
cv2.destroyAllWindows()