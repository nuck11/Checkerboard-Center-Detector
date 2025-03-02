from detect_centers import *

im = cv.imread("im1.jpg")
im = cv.cvtColor(im, cv.COLOR_BGR2GRAY) #se usar, apagar
im = cv.threshold(im, 127, 255, cv.THRESH_BINARY)[1] #se usar, apagar

#é melhor guardar como .png porque não usa compressao
find_centers(im, 1, 25, "centers.png")