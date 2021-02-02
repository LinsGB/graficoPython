import csv
#primeira linha a partir do index 1 são as datas
#index 0 a partir da linha 1 são as categorias
#o resto são os gastos, separados por categorias
with open('Gastos Família.csv') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')
    numberoLinha = 0
    numeroColuna = 0
    datas = []
    gastosPorCategoria = {}
    ultimaCategoriaAdicionada = ''
    for linha in csvReader:
        for valor in linha:
            if (numberoLinha == 0 and numeroColuna > 0 and valor != '' ):
                datas.append(valor)
            else:
                if (numberoLinha > 0 and numeroColuna == 0 and valor != ''):
                    gastosPorCategoria[valor] = []
                    ultimaCategoriaAdicionada = valor
                elif (numberoLinha > 0 and numeroColuna > 0 and valor != ''):
                    print('valor: ', gastosPorCategoria)
                    gastosPorCategoria[ultimaCategoriaAdicionada].append(valor)
            numeroColuna = numeroColuna + 1
        numberoLinha = numberoLinha + 1
        numeroColuna = 0
    print("Gastos = ", gastosPorCategoria)
    