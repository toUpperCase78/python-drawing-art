# DOG IMAGE 1
# REFERENCE: https://tr.pinterest.com/pin/714665034665446214/
import numpy as np
import cv2
WIDTH = 500
HEIGHT = 550
SIZE = 25
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_back_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s * 2), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_one_by_two(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s * 2, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def draw_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def draw_small_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + s, y + s), (0, 0, 0), 2)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

# HEAD OUTER
line_back_diagonal(25, 125, 3)
line_vertical(25, 75, 2)
line_forward_diagonal_two_by_one(25, 75)
line_horizontal(50, 25, 12)
line_back_diagonal_two_by_one(350, 25)
line_vertical(375, 75, 2)
line_forward_diagonal(300, 200, 3)

# HEAD INNER
line_forward_diagonal(100, 50)
line_vertical(100, 50, 7)
line_back_diagonal(100, 225)
line_horizontal(125, 250, 2)
line_forward_diagonal(175, 250)
line_vertical(200, 200)
line_back_diagonal(175, 175)
line_horizontal(175, 175, 2)
line_forward_diagonal(200, 200)
line_back_diagonal(200, 225)
line_horizontal(225, 250, 2)
line_forward_diagonal(275, 250)
line_vertical(300, 50, 7)
line_back_diagonal(275, 25)
line_horizontal(125, 75, 2)
draw_square(125, 100, 2)
line_horizontal(125, 120, 2)
draw_small_square(150, 130, 10)
line_horizontal(225, 75, 2)
draw_square(225, 100, 2)
line_horizontal(225, 120, 2)
draw_small_square(240, 130, 10)

# BONE
line_horizontal(75, 225)
line_back_diagonal(50, 200)
line_forward_diagonal(25, 225)
line_back_diagonal(25, 225)
line_forward_diagonal(25, 275)
line_back_diagonal(25, 275)
line_forward_diagonal(50, 300)
line_horizontal(75, 275, 10)
line_back_diagonal(325, 275)
line_forward_diagonal(350, 300)
line_back_diagonal(350, 250)
line_forward_diagonal(350, 250)
line_back_diagonal(350, 200)
line_forward_diagonal(325, 225)
line_horizontal(300, 225)

# LEGS
line_forward_diagonal_two_by_one(75, 375, 2)
line_vertical(75, 375, 3)
line_forward_diagonal(50, 475)
line_vertical(50, 475)
line_horizontal(50, 500)
line_forward_diagonal(75, 500)
line_vertical(100, 325, 6)
line_vertical(75, 475, 2)
line_horizontal(75, 525, 4)
line_vertical(175, 350, 7)
line_vertical(110, 500)
line_vertical(140, 500)
line_horizontal(175, 500, 2)
line_vertical(225, 350, 7)
line_horizontal(225, 525, 4)
line_vertical(260, 500)
line_vertical(290, 500)
line_back_diagonal_two_by_one(275, 275, 2)
line_vertical(325, 375, 3)
line_back_diagonal(325, 450)
line_vertical(350, 475)
line_horizontal(325, 500)
line_back_diagonal(300, 475)
line_vertical(300, 325, 6)
line_vertical(325, 475, 2)

# TAIL
line_horizontal(325, 400)
line_forward_diagonal_one_by_two(350, 400)
line_forward_diagonal_two_by_one(400, 375)
line_vertical(425, 275, 2)
line_back_diagonal_two_by_one(425, 275)
line_vertical(450, 325, 2)
line_forward_diagonal_two_by_one(425, 425)
line_forward_diagonal_one_by_two(375, 450)
line_horizontal(325, 450, 2)

cv2.imshow('Dog Image 1', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('dog_image1_output.jpg', img)
cv2.destroyAllWindows()