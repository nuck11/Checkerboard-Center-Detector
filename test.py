from detect import *

im = cv.imread("im2.jpg")
im = cv.cvtColor(im, cv.COLOR_BGR2GRAY) #se usar, apagar
im = cv.threshold(im, 127, 255, cv.THRESH_BINARY)[1] #se usar, apagar

find_centers(im, 3, 4)