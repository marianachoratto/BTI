'''1. Existem os algoritmos de cálculo de cédulas para troco, por exemplo:
Gastei 37 reais, paguei com uma nota de 50, quais notas devem ser entregues para troco

    Despesa 37
    Pagamento 50
    Troco 13 reais.    
    Resultado algoritmo: (1 nota de 10, 1 nota de 2, 1 moeda de 1).


Crie um algoritmo de troco para um freeshop. Onde o valor recebido é em reais e o troco dado em dólares.'''

#API para a cotação do dólar
#Utilizou-se a biblioteca requests, pois é mais simples e não é necessário passar tantas linhas de código.
import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

response = requests.get(url)

cotacao = float(response.json()['USDBRL']['bid'])


valorTotal = float(input('Digite o valor total da compra: '))
dinheiroRecebido = float(input('Digite o valor do dinheiro recebido: '))

def valor_da_compra(valorTotal, dinheiroRecebido ):
    resultado = dinheiroRecebido - valorTotal
    return resultado

troco = valor_da_compra(valorTotal, dinheiroRecebido)
print(f'O troco da compra é de R${troco:.2f} reais.'  )

def conversão_dolar(troco, cotacaoDolar):
    resultadoConvertido = troco/cotacaoDolar
    return resultadoConvertido

trocoConvertido = conversão_dolar(troco, cotacao)
print(f'O valor do troco em dólares é de ${trocoConvertido:.2f} dólares.')

def notas_para_troco(trocoConvertido):
    notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

    lista_notas = []
    for item in notas:
        qtd_notas = 0
        while item <= trocoConvertido:
            # print(f'Nota de {item}')
            trocoConvertido -= item
            # print(trocoConvertido)
            qtd_notas += 1
        lista_notas.append([item, qtd_notas])
    
    # print(lista_notas)
    
    #objetivo: escrever o troco no terminal
    lista_notas_filtrada = "O troco é de: "
    for item in lista_notas:
    # determinar a quantidade de notas (item[1]) da lista e o valor da nota (item[0])
        quantidade_notas = item[1]
        valor_da_nota = item[0]
        if quantidade_notas != 0: # checar se a nota ou moeda foi utilizada no troco
            lista_notas_filtrada += f'{quantidade_notas} {nota_ou_moeda(valor_da_nota)} de {valor_da_nota} , '
    lista_notas_filtrada = lista_notas_filtrada[:-2] #removendo a "," do final da frase
    print(lista_notas_filtrada)

def nota_ou_moeda(valor_da_nota):
    if valor_da_nota > 1: # checar se é nota ou moeda 
        return 'nota(s)'
    else: 
        return 'moeda(s)' 

resultado = notas_para_troco(trocoConvertido)
#As vezes vai faltar 1 centavo no troco, pela forma como o python lida com números com casas decimais.