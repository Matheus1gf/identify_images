import hashlib
import os

os.chdir(r'.\images')

fileList = os.listdir()
print('O total de arquivos na pasta é: ', len(fileList))

duplicates = []
duplicateFile = ''
hashKeys = dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
            if filehash not in hashKeys:
                hashKeys[filehash] = index
            else:
                duplicates.append((index, hashKeys[filehash]))
                duplicateFile = duplicateFile+' | '+filename

print('O(s) arquivo(s) duplicado(s) é(são): ', duplicateFile)
print('O total de arquivos duplicados é: ', len(duplicates))

# Se quiser remover as imagens, basta utilizar o código abaixo
#for index in duplicates:
#    os.remove(fileList[index[0]])
