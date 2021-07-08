import pandas as pd

source = r"CAMINHO"
local = r"CAMINHO DO ARQUIVO"

def splitcsv(file):
    '''abrindo o arquivo'''
    arquivo = pd.read_excel(file)

    '''criando a coluna de índice'''
    arquivo['index'] = arquivo.index

    '''criando uma lista com os nomes das colunas originais para dividir nos arquivos divididos'''
    colunas = list(arquivo.keys())

    '''quantidade de linhas para cada arquivo'''
    qtd_max = 98000

    '''índice da primeira linha do arquivo'''
    primeira_linha = arquivo.iloc[0:1]
    prima_linha = int(primeira_linha['index'])

    '''índice da última linha do arquivo'''
    ultima_linha = arquivo.iloc[-1::]
    ult_linha = int(ultima_linha['index'])

    '''outros dados'''
    lin_inicio = prima_linha
    nome = "TESTE"

    '''quantidade de arquivos a serem divididos'''
    divisao = int(round(ult_linha / 98000, 0))

    '''check divisao'''
    if divisao == 0:
        divisao = 1
    else:
        divisao

    '''loop para criação dos arquivos'''
    for i in range(1, divisao + 1):
        max_linha = (i * qtd_max)

        if i == 1:
            arch = arquivo.iloc[lin_inicio:max_linha + 1]
        else:
            arch = arquivo.iloc[(qtd_max * (i - 1) + 1):max_linha + 1]

        arch.to_excel(f'{source}'+f'\{nome}_{i}.xlsx', encoding='utf-8', columns=colunas, index_label='index')

        lin_inicio += 1

    print("fim")

splitcsv(local)
