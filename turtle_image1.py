# TURTLE IMAGE 1
# REFERENCE: https://tr.pinterest.com/pin/714665034665953135/
import numpy as np
import cv2
WIDTH = 375
HEIGHT = 300
SIZE = 25
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def draw_small_square_filled(x, y):
    cv2.rectangle(img, (x, y), (x + int(SIZE / 2), y + int(SIZE / 2)), BLACK, -1)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

line_horizontal(75, 175, 2)
line_back_diagonal(50, 150)
line_vertical(50, 125)
line_horizontal(25, 125)
line_vertical(25, 50, 3)
line_horizontal(25, 50, 3)
line_vertical(100, 50, 3)
line_horizontal(100, 125)

line_vertical(125, 100, 3)
line_forward_diagonal(125, 100, 2)
line_horizontal(175, 50, 3)
line_back_diagonal(250, 50, 2)
line_vertical(300, 100, 3)
line_horizontal(275, 175)
line_forward_diagonal(250, 200)
line_horizontal(175, 200, 3)
line_back_diagonal(150, 175)
line_horizontal(125, 175)

line_back_diagonal(150, 75)
line_horizontal(175, 100, 3)
line_forward_diagonal(250, 100)
line_forward_diagonal(150, 125)
line_vertical(150, 125)
line_horizontal(125, 150, 2)
line_forward_diagonal(175, 150)
line_vertical(200, 100)
line_back_diagonal(175, 150)
line_back_diagonal(200, 125)
line_forward_diagonal(200, 175)
line_vertical(200, 175)
line_horizontal(225, 150)
line_back_diagonal(250, 100)
line_forward_diagonal(250, 150)
line_back_diagonal(250, 150)
line_horizontal(275, 125)

line_forward_diagonal(100, 200)
line_vertical(100, 200, 2)
line_horizontal(100, 250, 2)
line_vertical(150, 200, 2)
line_horizontal(150, 200)
line_vertical(250, 200, 2)
line_horizontal(250, 250, 2)
line_vertical(300, 200, 2)
line_horizontal(300, 175)
line_horizontal(300, 200)
line_forward_diagonal(325, 175)
line_forward_diagonal_two_by_one(325, 200)

draw_small_square_filled(50, 75)

cv2.imshow('Turtle Image 1', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('turtle_image1_output.jpg', img)
cv2.destroyAllWindows()