# DRAGON IMAGE 1
# REFERENCE: https://tr.pinterest.com/pin/714665034666019782/
import numpy as np
import cv2
WIDTH = 375
HEIGHT = 325
SIZE = 25
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_vertical_customized(x, y, l=1):
    cv2.line(img, (x, y), (x, y + l), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def draw_small_square_filled(x, y):
    cv2.rectangle(img, (x, y), (x + int(SIZE / 2), y + int(SIZE / 2)), BLACK, -1)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

line_horizontal(50, 100)
line_vertical_customized(50, 100, 17)
line_horizontal(25, 117)
line_vertical_customized(25, 75, 42)
line_horizontal(25, 75, 2)
line_vertical(75, 50)
line_horizontal(75, 50)
line_forward_diagonal(100, 50)
line_vertical(125, 25)
line_horizontal(125, 50)
line_forward_diagonal(125, 75)
line_back_diagonal(125, 75)
line_vertical(150, 100, 2)
line_horizontal(150, 150)

line_horizontal(50, 125, 2)
line_vertical(100, 125)
line_forward_diagonal(75, 175)
line_vertical(75, 175, 2)
line_back_diagonal(75, 225)
line_vertical(100, 250)
line_horizontal(75, 275)
line_vertical(75, 275)
line_horizontal(75, 300, 2)
line_vertical(125, 200, 4)

line_forward_diagonal(150, 250, 2)
line_back_diagonal(150, 250)
line_horizontal(150, 275)
line_vertical(150, 275)
line_horizontal(150, 300, 3)
line_forward_diagonal(225, 300)
line_back_diagonal(250, 275)
line_horizontal(275, 300, 2)
line_forward_diagonal(325, 300)
line_vertical(350, 200, 3)
line_forward_diagonal(325, 225)
line_vertical(325, 225)
line_forward_diagonal(300, 275)
line_back_diagonal(275, 250)
line_vertical(275, 225)
line_back_diagonal(225, 175, 2)
line_horizontal(175, 175, 2)
line_vertical(175, 150)

line_forward_diagonal(175, 150)
line_vertical(200, 50, 3)
line_horizontal(200, 50, 4)
line_forward_diagonal(275, 75)
line_vertical(275, 75)
line_back_diagonal(275, 100)
line_horizontal(275, 125)
line_forward_diagonal(250, 150)
line_vertical(250, 150)
line_back_diagonal(250, 175)
line_horizontal(250, 200)

draw_small_square_filled(87, 75)

cv2.imshow('Dragon Image 1', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('dragon_image1_output.jpg', img)
cv2.destroyAllWindows()