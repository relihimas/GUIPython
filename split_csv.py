import pandas as pd

arqcsv = "CAMINHO DO ARQUIVO"


def opencsv(file):
  arquivo = pd.read_csv(file)
  arquivo['index'] = arquivo.index
  linha = arquivo.iloc[-1::]
  return list(linha['index'])

arquivo = pd.read_csv(arqcsv)
arquivo['index'] = arquivo.index

primeira_linha = arquivo.iloc[0:1]
prima_linha = int(primeira_linha['index'])

linha = arquivo.iloc[-1::]
ult_linha = int(linha['index'])

print(prima_linha)
print(ult_linha)

divisao = int(round(ult_linha / 98000,0))
print(divisao)

qtd_max = 98000
lin_inicio = prima_linha
nome = "TESTE"

for i in range(1, divisao+1):
  max_linha = (i * qtd_max)
  sobra_linha = ult_linha - (i * qtd_max)
  
  #print(f"{i} | {lin_inicio} - {max_linha} | {qtd_max * (i-1) + 1} - {max_linha} | {sobra_linha}")

  if i == 1:
    arch = arquivo.iloc[lin_inicio:max_linha+1]
  else:
    arch = arquivo.iloc[(qtd_max * (i-1) + 1):max_linha+1]

  arch.to_csv(f'{nome}_{i}.csv')

  lin_inicio += 1

print("fim")

#with open(f'{nome}_{i}.csv', mode='a', newline='') as csvfile:
#writer = csv.writer(csvfile)
#for r in row:
#writer.writerow(arch)
