# DIAGONAL FACES
# REFERENCE: https://tr.pinterest.com/pin/714665034665155964/
import numpy as np
import cv2
import random
WIDTH = 560
HEIGHT = 820
SIZE = 20
BLACK = (0, 0, 0)

def line_vertical(x, y, s=1):
    cv2.line(img, (x, y), (x, y + SIZE * s), BLACK, 2)

def line_horizontal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y), BLACK, 2)

def line_back_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def line_forward_diagonal(x, y, s=1):
    cv2.line(img, (x, y), (x + SIZE * s, y - SIZE * s), BLACK, 2)

def draw_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, 2)

def draw_filled_square(x, y, s=1):
    cv2.rectangle(img, (x, y), (x + SIZE * s, y + SIZE * s), BLACK, -1)

def draw_eyes_and_mouth(x, y):
    cv2.rectangle(img, (x, y), (x + SIZE * 2, y + SIZE * 2), BLACK, 2)
    cv2.rectangle(img, (x + SIZE * 2, y), (x + SIZE * 4, y + SIZE * 2), BLACK, 2)
    e = random.randint(1, 4)
    if e == 1:
        cv2.rectangle(img, (x, y), (x + SIZE, y + SIZE), BLACK, -1)
        cv2.rectangle(img, (x + SIZE * 2, y), (x + SIZE * 3, y + SIZE), BLACK, -1)
    elif e == 2:
        cv2.rectangle(img, (x + SIZE, y), (x + SIZE * 2, y + SIZE), BLACK, -1)
        cv2.rectangle(img, (x + SIZE * 3, y), (x + SIZE * 4, y + SIZE), BLACK, -1)
    elif e == 3:
        cv2.rectangle(img, (x, y + SIZE), (x + SIZE, y + SIZE * 2), BLACK, -1)
        cv2.rectangle(img, (x + SIZE * 2, y + SIZE), (x + SIZE * 3, y + SIZE * 2), BLACK, -1)
    elif e == 4:
        cv2.rectangle(img, (x + SIZE, y + SIZE), (x + SIZE * 2, y + SIZE * 2), BLACK, -1)
        cv2.rectangle(img, (x + SIZE * 3, y + SIZE), (x + SIZE * 4, y + SIZE * 2), BLACK, -1)
    m = random.randint(1, 4)
    if m == 1:
        cv2.rectangle(img, (x + SIZE, y + SIZE * 3), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    elif m == 2:
        cv2.rectangle(img, (x + SIZE, y + SIZE * 3), (x + SIZE * 2, y + SIZE * 4), BLACK, 2)
    elif m == 3:
        cv2.rectangle(img, (x + SIZE * 2, y + SIZE * 3), (x + SIZE * 3, y + SIZE * 4), BLACK, 2)
    elif m == 4:
        line_horizontal(x + SIZE, y + SIZE * 3, 2)
        line_back_diagonal(x + SIZE, y + SIZE * 3)
        line_forward_diagonal(x + SIZE * 2, y + SIZE * 4)

img = np.uint8(np.zeros((HEIGHT, WIDTH, 3)))
img[:,:,:] = 230

for i in range(0, HEIGHT, SIZE):
    cv2.line(img, (0, i), (WIDTH, i), (200, 200, 200), 1)
for i in range(0, WIDTH, SIZE):
    cv2.line(img, (i, 0), (i, HEIGHT), (200, 200, 200), 1)

# OUTER LINES
for i in range(0, WIDTH-80, SIZE):
    line_vertical(i+80, i)
    line_horizontal(i+80, i+20)

for i in range(0, WIDTH-280, SIZE):
    line_vertical(i+280, i)
    line_horizontal(i+280, i+20)

for i in range(0, WIDTH-480, SIZE):
    line_vertical(i+480, i)
    line_horizontal(i+480, i+20)

for i in range(0, WIDTH, SIZE):
    line_vertical(i, i+120)
    line_horizontal(i, i+140)

for i in range(0, WIDTH, SIZE):
    line_vertical(i, i+320)
    line_horizontal(i, i+340)

for i in range(0, WIDTH, SIZE):
    line_vertical(i, i+520)
    line_horizontal(i, i+540)

for i in range(0, WIDTH, SIZE):
    line_vertical(i, i+720)
    line_horizontal(i, i+740)

for i in range(120, 0, -SIZE):
    line_vertical(i, 120-i)
    line_horizontal(i-20, 120-i+20)

for i in range(320, 0, -SIZE):
    line_vertical(i, 320-i)
    line_horizontal(i-20, 320-i+20)

for i in range(520, 0, -SIZE):
    line_vertical(i, 520-i)
    line_horizontal(i-20, 520-i+20)

for i in range(WIDTH, 0, -SIZE):
    line_vertical(i, WIDTH-i+160)
    line_horizontal(i-20, WIDTH-i+180)

for i in range(WIDTH, 100, -SIZE):
    line_vertical(i, WIDTH-i+360)
    line_horizontal(i-20, WIDTH-i+380)

for i in range(WIDTH, 300, -SIZE):
    line_vertical(i, WIDTH-i+560)
    line_horizontal(i-20, WIDTH-i+580)

for i in range(WIDTH, 500, -SIZE):
    line_vertical(i, WIDTH-i+760)
    line_horizontal(i-20, WIDTH-i+780)

# PREMADE FACES
draw_square(0, 0, 2)
draw_square(0, 60)
draw_filled_square(20, 0)
draw_square(0, 200, 2)
draw_square(0, 260)
draw_filled_square(0, 200)
draw_square(0, 400, 2)
draw_filled_square(20, 420)
line_horizontal(0, 460)
line_forward_diagonal(0, 480)
draw_square(0, 600, 2)
draw_square(0, 660)
draw_filled_square(0, 620)
draw_square(0, 800, 2)
draw_filled_square(20, 800)

# RANDOMIZED FACES
for i in range(0, HEIGHT, 200):
    draw_eyes_and_mouth(160, i)
    draw_eyes_and_mouth(360, i)

for i in range(100, HEIGHT, 200):
    draw_eyes_and_mouth(60, i)
    draw_eyes_and_mouth(260, i)
    draw_eyes_and_mouth(460, i)

cv2.imshow('Diagonal Faces', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('diagonal_faces_output.jpg', img)
cv2.destroyAllWindows()