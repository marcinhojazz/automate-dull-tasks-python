        # PARTE I
        
# CAPÍTULO 1: Básico sobre o Python.


# (...) Você se lembrará muito mais das tarefas que fizer do que dos textos que forem apenas lidos.


# Fornecendo expressões no shell interativo.

# No CMD digita: python. 
# Faça um teste, digite: >>> 2 + 2 e veja o resultado.
# >>> 4

------------------------------------------------------
Operador    Operação        Exemplo     Avaliado como
------------------------------------------------------
**          exponencial     2**3        8
%           módulo/resto    22%8        6
//          div. inteira    22//8       2
/           divisão         22/8        2.75
*           multiplicação   3*5         15
-           subtração       5-2         3
+           adição          2+2         4

### TIPOS DE DADO INTEIRO, DE PONTO FLUTUANTE E STRING.
------------------------------------------------------
Tipo de dado            Exemplos
------------------------------------------------------
Inteiros                -2, -1, 0, 1, 2, 4, 5
Núm. ponto flutuante    -1.25, -1.0, -0.5, 0.0, 0.5, 1.0
Strings                 'a', 'aa', 'aaa', 'Hello', '11 cats'


## CONCATENAÇÃO E REPETIÇÃO DE STRINGS
O significado de um operador pode mudar de acordo com os tipos de dados dos valores próximos a ele. Por exemplo, + é o operador de adição quando atua sobre dois valores inteiros ou de ponto flutuante. Entretando, quando + é usado com dois valores do tipo string, ele une as strings, constituindo o operador da concatenação de strings. Digite o seguinte no shell interativo:

EXEMPLOS:

>>> 'ALICE'+'BOB'
'ALICEBOB'

A expressão é avaliada como um único valor novo do tipo string que combina o texto das duas strings. Entretanto, se você tentar usar o operador + em uma string e um valor inteiro, o Python não saberá como lidar com isso e exibirá uma mensagem de erro.

EXEMPLOS QUE NÃO DÃO CERTO:

>>> 'Alice' + 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects


A mensagem de erro quer dizer que o Python achou que você estava tentando concatenar um inteiro à string 'Alice'. Seu código deverá converter explicitamente o inteiro em uma string, pois o Python não pode fazer isso automaticamente. (A conversão de tipos de dados será explicada na seção "DISSECANDO SEU PROGRAMA", em que as funções str(), int() e float() serão discutidas).

OPERADOR * é usado para multiplicação quando atua sobre dois valores inteiros ou de ponto flutuante. Porém, quando for usado em um valor do tipo String e um valor inteiro, o operador * corresponderá ao operador de 'repetição de string'. Forneça uma string multiplicada por um número no shell interativo para ver esse operador em açã:

EXEMPLO: 

>>> 'alice' * 5
'alicealicealicealicealice'


A expressão é avaliada como um único valor do tipo string que repete o valor original um número de vezes igual ao valor inteiro. A repetição de string é um truque útil, porém não é usada com tanta frequência quanto a concatenação de strings.
O operador * pode ser usado apenas com dois valores numéricos ou com um valor do tipo string e um valor inteiro (para repetição de string). Caso contrário, o Python simplesmente exibirá uma mensagem de erro.

EXEMPLO:

>>> 'ALICE' * 'BOB'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'

>>> 'ALICE' * 5.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'



## ARMAZENANDO VALORES EM VARIÁVEIS