
import os

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''


def main():
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    if not os.path.exists(dir):
        os.makedirs(dir)

    if os.path.isdir(dir):
        os.chmod(dir, 0o744)

    contador = 0

    while contador < 5:
        entrada()
        contador = contador + 1


def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    valor_media = med(nota1, nota2, nota3, nota4)

    print('Média:', valor_media)

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media


def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha = ''
    linha = nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'

    escreveArq(dir, arq, linha)


def escreveArq(caminho, arquivo, linha_cad):
    file = ''
    tipo = ''
    enc = ''

    enc = 'utf-8'

    if os.path.exists(caminho) and os.path.isdir(caminho):
        nome_arquivo = os.path.join(caminho, arquivo)

        if os.path.exists(nome_arquivo):
            tipo = 'a'
        else:
            tipo = 'w'

        file = open(nome_arquivo, tipo, encoding=enc)
        file.write(linha_cad)
        file.close()

main()
