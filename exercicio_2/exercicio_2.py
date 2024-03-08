'''2. O Governo brasileiro está para lançar um programa para que usuários frequentes de pedágio paguem menos por passagem.

O cenário é:

Um pedágio cobra por passagem 7,90 reais.
Dentro do mesmo mês, após um veículo passar 10 vezes, ele começará a receber um desconto de 5% por passagem.
O valor mínimo que ele pode pagar é de 20% do valor da tarifa cheia.

Demonstre:

1 - A estrutura de banco de dados para suportar esta funcionalidade
2 - Os comandos de banco de dados para operar (selects, inserts e updates)
3 - O algoritmo do processo.
'''
#1) Criar banco de dados. Ele terá a coluna nomeUsuário e numeroDePassagens

import sqlite3

conexao = sqlite3.connect('usuariosPedagio')
cursor = conexao.cursor()


# cursor.execute('CREATE TABLE pedagio (id INTEGER PRIMARY KEY AUTOINCREMENT, nomeUsuario varchar(20), data TEXT )')
# cursor.execute("INSERT INTO pedagio (nomeUsuario, data) VALUES ('maria santos', '03-2024')")
# cursor.execute ("DELETE FROM pedagio WHERE id = 14")

# conexao.close()

#2) fazer função do preço
from datetime import datetime

class Software:
    #a funcao_desconto() é utilizada dentro da função get_passagens_mes()
    def funcao_desconto(self, lista_fetch):
        passagem = 7.9
        numero_de_passagens = lista_fetch

        if numero_de_passagens >= 10 and numero_de_passagens < 20:
            valor_passagem = passagem * 0.95
            return valor_passagem
        elif numero_de_passagens >= 20 and numero_de_passagens < 30:
            valor_passagem = passagem * 0.9
            return valor_passagem
        elif numero_de_passagens >= 30 and numero_de_passagens < 40:
            valor_passagem = passagem * 0.85
            return valor_passagem
        elif numero_de_passagens >= 40:
            valor_passagem = passagem * 0.8
            return valor_passagem
        else:
            return passagem # Sem desconto para menos de 10 passagens
    
    def adicionar_data(self):
        data_atual = datetime.now().strftime('%Y-%m')
        return data_atual
    
    def get_passagens_mes(self, nome_cliente, data_atual):
        data = cursor.execute(f'SELECT * FROM pedagio WHERE nomeUsuario="{nome_cliente}" AND data="{data_atual}" ')
        data_fetch = data.fetchall()
        lista_fetch = len(data_fetch)
        mensagem_preco = (f'Olá {nome_cliente}, vimos que você usou o pedágio {lista_fetch} vezes esse mês, portanto o valor da sua passagem é de R${self.funcao_desconto(lista_fetch):.2f} reais.')
        return mensagem_preco

    def adicionar_passagem_atual(self, nome_cliente, data_atual  ):
        cursor.execute(f"INSERT INTO pedagio (nomeUsuario, data) VALUES ('{nome_cliente}', '{data_atual}')")

    def fechar_conexao(self):
        conexao.commit()
        conexao.close()

    def iniciar(self):
            nome_cliente = input('Olá e seja bem-vindo ao Pedágio! Digite seu nome:    ').lower()

            #pegando a data atual do modulo datetime
            data_atual = self.adicionar_data()

            #fazendo get de quantas vezes o usuário usou o pedágio no mês
            pedagio1 = self.get_passagens_mes(nome_cliente, data_atual)
            print(pedagio1)

            #adicionando uma nova passagem
            self.adicionar_passagem_atual(nome_cliente, data_atual )

            #fechando conexão com o banco de dados
            self.fechar_conexao()


pedagio = Software()
pedagio.iniciar()