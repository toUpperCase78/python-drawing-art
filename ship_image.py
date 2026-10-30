# SHIP IMAGE
# REFERENCE: https://tr.pinterest.com/pin/714665034666068918/
import numpy as np
import cv2
WIDTH = 525
HEIGHT = 400
SIZE = 25
BLACK = (0, 0, 0)

def line_bold_customized(x, y, w=1, h=1):
    cv2.line(img, (x, y), (x + w, y + h), BLACK, 4)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_vertical_bold(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 4)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_horizontal_bold(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 4)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_back_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 2), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_one_by_three(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 3, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def draw_small_rectangle(x, y):
    cv2.rectangle(img, (x, y), (x + SIZE, y + int(SIZE / 2)), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

line_vertical(50, 125, 4)
line_horizontal(50, 225, 4)
line_back_diagonal(50, 125, 4)
line_vertical_bold(100, 75, 4)
draw_small_rectangle(75, 75)
line_vertical_bold(100, 225, 2)
line_horizontal(25, 250, 4)
line_vertical(75, 250)
line_vertical(125, 250)
line_horizontal(75, 275, 2)

line_back_diagonal_two_by_one(175, 150)
line_vertical(200, 200)
line_forward_diagonal_two_by_one(175, 275)
line_horizontal(175, 275, 4)
line_forward_diagonal_two_by_one(275, 275)
line_vertical(300, 200)
line_back_diagonal_two_by_one(275, 150)
line_horizontal(175, 150, 4)

line_back_diagonal(175, 50)
line_vertical(200, 75)
line_forward_diagonal(175, 125)
line_horizontal(175, 125, 3)
line_forward_diagonal(250, 125)
line_vertical(275, 75)
line_back_diagonal(250, 50)
line_horizontal(175, 50, 3)
line_vertical_bold(225, 25)
draw_small_rectangle(200, 25)
line_vertical_bold(225, 125)
line_vertical_bold(225, 275, 2)
line_horizontal(125, 275, 2)
line_back_diagonal(125, 275)
line_vertical(150, 275)
line_horizontal(150, 300, 2)
line_vertical(175, 275)
line_back_diagonal(200, 300)
line_horizontal(225, 325, 2)

line_back_diagonal(300, 175)
line_vertical(325, 200, 2)
line_forward_diagonal(300, 275)
line_horizontal(300, 275, 3)
line_forward_diagonal(375, 275)
line_vertical(400, 200, 2)
line_back_diagonal(375, 175)
line_horizontal(300, 175, 3)
line_back_diagonal(300, 75)
line_vertical(325, 100)
line_forward_diagonal(300, 150)
line_horizontal(300, 150, 3)
line_forward_diagonal(375, 150)
line_vertical(400, 100)
line_back_diagonal(375, 75)
line_horizontal(300, 75, 3)
line_vertical_bold(350, 50)
draw_small_rectangle(325, 50)
line_vertical_bold(350, 150)
line_vertical_bold(350, 275)
line_forward_diagonal(275, 325)
line_horizontal(300, 300, 4)
line_back_diagonal(400, 300)
line_horizontal(275, 325, 6)
line_vertical(300, 300)
line_vertical(325, 300)

line_forward_diagonal_two_by_one(425, 275)
line_vertical(450, 200)
line_forward_diagonal_one_by_two(450, 200)
line_vertical(500, 175)
line_forward_diagonal_two_by_one(475, 250)
line_forward_diagonal_one_by_two(425, 275)
line_bold_customized(500, 125, -25, 62)
line_bold_customized(425, 325, 25, -62)

line_forward_diagonal_one_by_three(425, 325)
line_forward_diagonal_one_by_two(400, 350, 2)
line_forward_diagonal(375, 375)
line_vertical(25, 250)
line_back_diagonal_two_by_one(25, 275)
line_vertical(50, 325)
line_back_diagonal(50, 350)
line_horizontal_bold(0, 375, 21)

cv2.imshow('Ship Image', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('ship_image_output.jpg', img)
cv2.destroyAllWindows()