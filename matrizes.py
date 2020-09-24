#Criando a matriz
matrix = [['A','8','5','10'],
          ['G','U','1','T'],
          ['RD','56','N','5'],
          ['54','HG','9','7']]
#Loop percorrendo a matriz por inteiro
for line in range(len(matrix)):
    for column in range(len(matrix[line])):
          #verifica se a casa tem um numero
        if matrix[line][column].isdigit():
          #eh numero printa o numero e fala true
            print('true' + ' ' +matrix[line][column])
        else:
          #nao eh numero printa a letra e fala false
            print('false' + ' ' +matrix[line][column])
