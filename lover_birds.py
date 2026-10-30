# LOVER BIRDS
# REFERENCE: https://tr.pinterest.com/pin/714665034665446201/
import numpy as np
import cv2
WIDTH = 450
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

def line_back_diagonal_two_by_half(x, y, s=1):
    cv2.line(img, (x, y), (x + int(SIZE * s / 2), y + SIZE * s * 2), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def line_forward_diagonal_two_by_one(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s * 2), BLACK, 2)

def line_forward_diagonal_two_by_half(x, y, s=1):
    cv2.line(img, (x, y), (x + int(SIZE * s / 2), y - SIZE * s * 2), BLACK, 2)

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

# LEFT BIRD
line_vertical(75, 150, 3)
line_forward_diagonal(75, 150)
line_horizontal(100, 125, 2)
line_back_diagonal(150, 125)
line_vertical(175, 150, 3)
line_back_diagonal(175, 150)
line_forward_diagonal(175, 200)
line_horizontal(175, 175)
draw_square(125, 150)
draw_small_square(137, 157, 8)

line_forward_diagonal(25, 250)
line_vertical(25, 250, 2)
line_back_diagonal(25, 300, 4)
line_forward_diagonal(125, 400, 4)
line_vertical(225, 250, 2)
line_back_diagonal(200, 225)
line_horizontal(150, 225, 2)
line_forward_diagonal(125, 250)
line_back_diagonal(100, 225)
line_horizontal(50, 225, 2)
line_vertical(50, 275, 2)
line_vertical(75, 300, 2)
line_vertical(100, 325, 2)
line_vertical(125, 350, 2)
line_vertical(150, 325, 2)
line_vertical(175, 300, 2)
line_vertical(200, 275, 2)

line_forward_diagonal_two_by_one(50, 475, 2)
line_back_diagonal(50, 475)
line_forward_diagonal(75, 500)
line_back_diagonal(100, 475)
line_forward_diagonal(125, 500)
line_back_diagonal(150, 475)
line_forward_diagonal(175, 500)
line_back_diagonal_two_by_one(150, 375, 2)
line_back_diagonal_two_by_half(138, 425)
line_forward_diagonal_two_by_half(100, 475)

# RIGHT BIRD
line_vertical(275, 150, 3)
line_forward_diagonal(275, 150)
line_horizontal(300, 125, 2)
line_back_diagonal(350, 125)
line_vertical(375, 150, 3)
line_forward_diagonal(250, 175)
line_back_diagonal(250, 175)
line_horizontal(250, 175)
draw_square(300, 150)
draw_small_square(305, 157, 8)

line_forward_diagonal(225, 250)
line_back_diagonal(225, 300, 4)
line_forward_diagonal(325, 400, 4)
line_vertical(425, 250, 2)
line_back_diagonal(400, 225)
line_horizontal(350, 225, 2)
line_forward_diagonal(325, 250)
line_back_diagonal(300, 225)
line_horizontal(250, 225, 2)
line_vertical(250, 275, 2)
line_vertical(275, 300, 2)
line_vertical(300, 325, 2)
line_vertical(325, 350, 2)
line_vertical(350, 325, 2)
line_vertical(375, 300, 2)
line_vertical(400, 275, 2)

line_forward_diagonal_two_by_one(250, 475, 2)
line_back_diagonal(250, 475)
line_forward_diagonal(275, 500)
line_back_diagonal(300, 475)
line_forward_diagonal(325, 500)
line_back_diagonal(350, 475)
line_forward_diagonal(375, 500)
line_back_diagonal_two_by_one(350, 375, 2)
line_forward_diagonal_two_by_half(300, 475)
line_back_diagonal_two_by_half(338, 425)

# STICK
line_horizontal(25, 350, 2)
line_vertical(25, 350)
line_horizontal(25, 375, 3)
line_horizontal(175, 350, 4)
line_horizontal(150, 375, 6)
line_horizontal(375, 350, 2)
line_vertical(425, 350)
line_horizontal(350, 375, 3)

# MIDDLE HEART
line_forward_diagonal(175, 50)
line_vertical(175, 50)
line_back_diagonal(175, 75, 2)
line_forward_diagonal(225, 125, 2)
line_vertical(275, 50)
line_back_diagonal(250, 25)
line_forward_diagonal(225, 50)
line_back_diagonal(200, 25)

cv2.imshow('Lover Birds', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('lover_birds_output.jpg', img)
cv2.destroyAllWindows()