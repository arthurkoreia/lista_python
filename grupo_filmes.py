lista_filmes = ['Titanic','Bettlejuice','Superman','Senhor dos Aneis']
print(lista_filmes)

filme1 = "Titanic"
ano1 = 1997

filme2 = "Bettlejuice"
ano2 = 1988

filme3 = "Superman"
ano3 = 1978

filme4 = "Senhor dos Aneis"
ano4 = 2001


selecionado = input('Sendo 1 Titanic e 4 Senhor dos Aneis, selecione o filme de 0 a 4 para saber seu ano de lancamento: ')

if selecionado == '1':
    print(filme1)
    print(ano1)
    
if selecionado == '2':
    print(filme2)
    print(ano2)
    
if selecionado == '3':
    print(filme3)
    print(ano3)
    
if selecionado == '4':
    print(filme4)
    print(ano4)
