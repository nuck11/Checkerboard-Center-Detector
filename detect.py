import cv2 as cv
import os

def clear():
    os.system('cls')

#       colunhas
#limhas 0 0 0 0 0 0 0 0 [linhas][colunas]
#       1 1 0 0 1 1 0 1

#esta é a função que atribui a um pixel a sua pontuaçãode correspondência
#com um centro perfeito

win = 25
def eval(l, c): #a função funciona bem, conta todos os 2500 pixeis numa janela
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
    #3º QUADRANTE
    for y in range(l + 1, l + win + 1):
        for x in range(c + 1, c + win + 1):
            if im[y][x] == 0:
                points = points + 1

    return points

im = cv.imread("im1.jpg")
im = cv.cvtColor(im, cv.COLOR_BGR2GRAY) #se usar, apagar

vsize = im.shape[0]
hsize = im.shape[1]

#guarda as coordenadas do pixel mais provavel de ser centro e da sua pontuação
#[x,y,pontos]
best = [0,0,0]

count = 0
percent = 0
#Começar o varrimento na segunda metade da imagem
#o varrimento é feito pixel
for l in range(int(vsize/2), vsize - win - 1):
    for c in range(win, hsize - win - 1):
        count = count + 1

        percent2 = int((count/((vsize/2 - win)*(hsize - 2*win))) * 100)
        if (percent2 > percent):
                percent = percent2
                clear()
                print(str(percent)+"%")

        points = eval(l,c)
        if (points > best[2]):
            best = [l, c, points]

im[best[0], best[1]] = 100
print(best)