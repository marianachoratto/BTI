

# Teste de lógica para o estágio na BTI

Segue uma breve explicação sobre a resolução dos exercícios. Também existem comentários no código.

Escolhi a linguagem python por ter mais afinidade. E utilizei o Dbeaver, que é o programa que estou acostumada fazer planilhas SQL.

## Exercício 1

Para o exercício 1, inicialmente foi utilizada uma API para obter a cotação do dólar. A biblioteca requests foi escolhida devido à sua simplicidade na implementação do código.

Em seguida, foram desenvolvidas duas funções: `valor_da_compra()` e `conversão_dólar()`. A primeira exibe o valor do troco, enquanto a segunda realiza a conversão para dólares, utilizando a cotação previamente obtida.

Por fim, temos a função `notas_para_troco()`, dividida em duas partes. Na primeira parte, é feita a comparação entre o valor das notas da lista e o troco convertido. Sempre que o valor da nota for menor ou igual ao troco convertido, esse valor é adicionado a uma lista chamada `lista_notas`. Ao final, `lista_notas` conterá várias sub-listas, onde o índice [0] representa o valor da nota/moeda e o índice [1] representa a quantidade de notas necessárias para o troco.

Na segunda parte, o objetivo é exibir o troco no terminal. O primeiro loop determina a quantidade de notas (item[1]) e o valor da nota (item[0]). Se o valor do índice [1] for diferente de zero, a mensagem de troco será exibida. Além disso, foi adicionada a função `nota_ou_moeda` para imprimir "nota" ou "moeda" no terminal conforme apropriado. Foi colocado de lado no código para facilitar o entendimento.

## Exercício 2

Foi criado o banco de dados com os campos, id, nomeUsuario e data. O usuário tem desconto na passagem se tiver comprado 10 ou mais passagens de ônibus durante o mês. Assim, quando o usuário compra a passagem o algoritmo automaticamente verifica quantas passagens o usuário já comprou no período. Para facilitar a verificação, o algoritmo automaticamente pega o ano e o mês através da função datetime. Com isso, ele procura no banco de dados o nome do usuário e quantas passagens ele já comprou, através da função `get_passagens_mes()`, e faz o desconto, através da função `funcao_desconto()`. Ao final do código, o algoritmo automaticamente adiciona a passagem comprada no momento do uso da máquina com a função `adicionar_passagem_atual()`. Por fim, fecha-se a conexão com o banco de dados para se evitar bugs no futuro.

A função `iniciar()` foi quebrada em funções menores para facilitar a leitura do código.

**Recomenda-se utilizar no terminal o nome Pedro Dias e Maria Santos para verificar o desconto nas passagens, pois já foram compradas várias passagens em seus nomes.**


 
