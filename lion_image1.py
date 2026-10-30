# LION IMAGE 1
# REFERENCE: https://tr.pinterest.com/pin/714665034665446271/
import numpy as np
import cv2
WIDTH = 525
HEIGHT = 625
SIZE = 25
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_back_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y + SIZE * s), BLACK, 2)

def line_back_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 2), BLACK, 2)

def line_back_diagonal_three_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 3), BLACK, 2)

def line_back_diagonal_four_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 4), BLACK, 2)

def line_back_diagonal_five_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 5), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def line_forward_diagonal_three_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 3), BLACK, 2)

def line_forward_diagonal_three_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y - SIZE * s * 3), BLACK, 2)

def line_forward_diagonal_four_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 4), BLACK, 2)

def line_forward_diagonal_five_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 5), BLACK, 2)

def draw_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

# HEAD OUTER
line_horizontal(100, 25, 4)
line_back_diagonal(100, 25)
line_forward_diagonal_one_by_two(75, 75)
line_forward_diagonal(50, 100)
line_horizontal(50, 100)
line_forward_diagonal_two_by_one(50, 150)
line_vertical(50, 150)
line_forward_diagonal(50, 175)
line_forward_diagonal_three_by_one(50, 225)
line_forward_diagonal(50, 225)
line_vertical(75, 200, 3)
line_forward_diagonal(75, 275)
line_vertical(100, 250)
line_back_diagonal_two_by_one(100, 275)
line_vertical(125, 275, 2)
line_back_diagonal(125, 275, 2)
line_vertical(175, 300)
line_back_diagonal(175, 300, 2)
line_forward_diagonal(225, 350, 2)
line_vertical(275, 300)
line_forward_diagonal(275, 325, 2)
line_vertical(325, 275, 2)
line_forward_diagonal_two_by_one(325, 325)
line_vertical(350, 250)
line_back_diagonal(350, 250)
line_vertical(375, 200, 3)
line_back_diagonal(375, 200)
line_back_diagonal_three_by_one(375, 150)
line_back_diagonal(375, 150)
line_vertical(400, 150)
line_back_diagonal_two_by_one(375, 100)
line_horizontal(375, 100)
line_back_diagonal(375, 75)
line_back_diagonal_one_by_two(325, 50)
line_forward_diagonal(325, 50)
line_horizontal(250, 25, 4)
line_forward_diagonal(225, 50)
line_back_diagonal(200, 25)

# HEAD INNER
line_vertical(150, 50)
line_horizontal(150, 50)
line_back_diagonal(175, 50)
line_forward_diagonal(250, 75)
line_horizontal(275, 50)
line_vertical(300, 50)

line_forward_diagonal_one_by_two(125, 125)
line_horizontal(175, 100, 4)
line_back_diagonal_one_by_two(275, 100)
line_vertical(325, 125, 4)
line_forward_diagonal_one_by_two(275, 250)
line_horizontal(175, 250, 4)
line_back_diagonal_one_by_two(125, 225)
line_vertical(125, 125, 4)

draw_square(175, 125)
draw_square(250, 125)
line_horizontal(200, 175, 2)
line_back_diagonal(200, 175)
line_forward_diagonal(225, 200)
line_vertical(225, 200)
line_horizontal(200, 225, 2)
line_back_diagonal(175, 200)
line_forward_diagonal(250, 225)

# CHEST & LEGS
line_forward_diagonal(75, 300)
line_forward_diagonal_two_by_one(50, 350)
line_vertical(50, 350, 4)
line_back_diagonal_four_by_one(50, 450)
line_forward_diagonal(50, 575)
line_vertical(50, 575)
line_horizontal(50, 600, 5)
line_vertical(75, 575)
line_vertical(100, 575)
line_forward_diagonal(125, 600)
line_back_diagonal_five_by_one(125, 450)
line_forward_diagonal_two_by_one(125, 450)
line_back_diagonal_one_by_two(125, 450)
line_vertical(175, 475)
line_back_diagonal_two_by_one(175, 500)
line_vertical(200, 550)
line_forward_diagonal(175, 600)
line_horizontal(175, 475, 4)
line_forward_diagonal_one_by_two(275, 475)
line_vertical(275, 475)
line_forward_diagonal_two_by_one(250, 550)
line_vertical(250, 550)
line_back_diagonal(250, 575)
line_forward_diagonal_five_by_one(300, 575)
line_back_diagonal(300, 575)
line_back_diagonal_two_by_one(300, 400)
line_horizontal(275, 600, 5)
line_vertical(350, 575)
line_vertical(375, 575)
line_vertical(400, 575)
line_back_diagonal(375, 550)
line_forward_diagonal_four_by_one(375, 550)
line_vertical(400, 350, 4)
line_back_diagonal_two_by_one(375, 300)
line_back_diagonal(350, 275)

# TAIL
line_forward_diagonal(400, 350)
line_vertical(425, 125, 8)
line_forward_diagonal(425, 125)
line_back_diagonal(450, 100)
line_vertical(475, 125)
line_forward_diagonal_two_by_one(450, 200)
line_back_diagonal(425, 175)
line_vertical(450, 200, 5)
line_forward_diagonal_three_by_two(400, 400)

cv2.imshow('Lion Image 1', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('lion_image1_output.jpg', img)
cv2.destroyAllWindows()