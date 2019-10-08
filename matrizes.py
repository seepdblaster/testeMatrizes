matrix = [['A','8','5','10'],
          ['G','U','1','T'],
          ['RD','56','N','5'],
          ['54','HG','9','7']]
for line in range(len(matrix)):
    for column in range(len(matrix[line])):
        if matrix[line][column].isdigit():
            print('true' + ' ' +matrix[line][column])
        else:
            print('false' + ' ' +matrix[line][column])