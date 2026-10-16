
import os

valor: int = 0
dir: str = ''
arq: str = ''


def main():
    global valor, dir, arq

    dir = '/tmp/exercicios'
    arq = 'ex34.txt'

    if not os.path.exists(dir):
        os.makedirs(dir)

    if os.path.isdir(dir):
        os.chmod(dir, 0o744)

    valor = int(input('Digite um valor entre 1 e 10: '))

    contador = 0
    result = 0

    while contador < 10:
        result = mult(valor, contador + 1)
        grava(contador, result)
        contador = contador + 1


def mult(vlr, tab):
    res = vlr * tab
    return res


def grava(c, rslt):
    global dir, arq

    file = ''
    tipo = ''
    enc = ''
    linha = ''

    linha = str(rslt) + '\n'
    enc = 'utf-8'
    tipo = 'w'

    if os.path.exists(dir) and os.path.isdir(dir):
        caminho = os.path.join(dir, arq)

        if os.path.exists(caminho) and c > 0:
            tipo = 'a'

        file = open(caminho, tipo, encoding=enc)
        file.write(linha)
        file.close()

main()
    
