import cv2 as cv

win = int(50/2)

def eval(im, l, c):
    points = 0
    count = 0
    #1º QUADRANTE
    for y in range(l - win + 1, l + 1):
        for x in range(c - win + 1, c + 1):
            count = count + 1
            if im[y][x] == 0:
                points = points + 1
    #2º QUADRANTE
    for y in range(l - win + 1, l + 1):
        for x in range(c + 1, c + win + 1):
            count = count + 1
            if im[y][x] == 255:
                points = points + 1
    #3º QUADRANTE
    for y in range(l + 1, l + win + 1):
        for x in range(c - win + 1, c + 1):
            count = count + 1
            if im[y][x] == 255:
                points = points + 1
    #4º QUADRANTE
    for y in range(l + 1, l + win + 1):
        for x in range(c + 1, c + win + 1):
            count = count + 1
            if im[y][x] == 0:
                points = points + 1

    return (points, count)

im = cv.imread("im1.jpg")
im = cv.cvtColor(im, cv.COLOR_BGR2GRAY) #se usar, apagar
