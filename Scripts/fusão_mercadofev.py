path_json = 'Raw_Data/dados_empresaA.json'
path_csv = 'Raw_Data/dados_empresaB.csv'

from processament_dados import Dados

#Extract

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)


print(dados_empresaA.qtd_linhas)
print(dados_empresaB.qtd_linhas)


#Transform

key_mapping = {'Nome do Item' : 'Nome do Produto',
               'Classificação do Produto' : 'Categoria do Produto',
               'Valor em Reais (R$)' : 'Preço do Produto (R$)',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial', 
               'Data da Venda' : 'Data da Venda'} 


dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join_dados(dados_empresaA, dados_empresaB)
print(dados_fusao)
print(dados_fusao.qtd_linhas)


#Load

path_dados_combinados = 'Processed_Data/dados_combinados_tabela.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)










