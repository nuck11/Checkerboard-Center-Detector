import cv2 as cv
import os

def clear():
    os.system('cls')

#esta é a função que atribui a um pixel a sua pontuação de correspondência
#com um centro perfeito
def eval(im, l, c, win):
    points = 0
    #1º QUADRANTE
    for y in range(l - win + 1, l + 1):
        for x in range(c - win + 1, c + 1):
            if im[y][x] == 0:
                points = points + 1
    #2º QUADRANTE
    for y in range(l - win + 1, l + 1):
        for x in range(c + 1, c + win + 1):
            if im[y][x] == 255:
                points = points + 1
    #3º QUADRANTE
    for y in range(l + 1, l + win + 1):
        for x in range(c - win + 1, c + 1):
            if im[y][x] == 255:
                points = points + 1
    #4º QUADRANTE
    for y in range(l + 1, l + win + 1):
        for x in range(c + 1, c + win + 1):
            if im[y][x] == 0:
                points = points + 1
    return points

#marca a zona proxima a um pixel mais provavel
def mark(im, l, c):
    im[l][c] = 100;im[l][c + 1] = 100
    im[l + 1][c] = 100;im[l + 1][c + 1] = 100

#encontra e marca os centros numa imagem
def find_centers(im, num_centers, win, ui = 1):
    vsize = im.shape[0]
    hsize = im.shape[1]

    centers = []
    best = [0,0,0]
    percent = 0
    count = 0

    for _ in range(num_centers):
        best[2] = 0
        for l in range(int(vsize/2), vsize - win - 1):
            for c in range(win, hsize - win - 1):
                if(im[l][c] != 100): #apenas avalia o pixel se n for já um centro
                    points = eval(im,l,c,win)/((win*2)**2)*100
                if (points > best[2]):
                    best = [l, c, points]
                if (ui):
                    count = count + 1
                    percent2 = int((count/(((vsize/2 - win)*(hsize - 2*win))*num_centers)) * 100)
                    if (percent2 > percent):
                        clear(); print(best,end=' '); print(str(percent + 2)+"%")
                        percent = percent2
        centers.append(best.copy())
        mark(im, best[0], best[1])

    print(centers)
    cv.imwrite("im_centers.jpg", im)
    return centers
