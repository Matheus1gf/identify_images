import cv2
import argparse

# Recebe a imagem
# TADEU: assim que se recebe parâmetro por terminal em python
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
img_file = vars(ap.parse_args())
img = cv2.imread(img_file["image"])

# copia a imagem proginal
res = img.copy()
# seta uma a cor
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Excluindo textos e contando áreas que estavam em branco
# PROBLEMA: As linhas dos retângulos só são contadas caso estejam em branco, se este for estiver dentro da próxima
# execução, ele conta as linas, os caracteres e as colunas
for i in contours:
    cnt = cv2.contourArea(i)
    if cnt < 500:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(res,(x-1,y-1),(x+w+1,y+h+1),(255,255,255),-1)

# Imprimindo resultado e o destruindo
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# O tratamento do próximo processamento é feito a partir de count
count = res.copy()
gray = cv2.cvtColor(count, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

check = []
for i in contours:
    # IDEIA: na inclusão das coordenadas, é possível que elas venham aqui
    cnt = cv2.contourArea(i)
    if 10000 > cnt > 10:
        cv2.drawContours(count, [i], 0, (255,255,0), 2)
        M = cv2.moments(i)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        check.append([cx, cy])
# sort é usado para ordenação de lists e lambda é uma função anônima (definição de lambda:https://pythonhelp.wordpress.com/tag/lambda/)
# A ordenação pode ser feita decrescente utilizando resverse=True
check.sort(key=lambda xy: xy[1])
columns = 1

for i in range(0, len(check)-1):
    if check[i+1][1] + 5 >= check[i][1] >= check[i+1][1] - 5:
        columns += 1
    else:
        break

print('Colunas: ', columns)

cv2.imshow('res', count)
cv2.waitKey(0)
cv2.destroyAllWindows()
