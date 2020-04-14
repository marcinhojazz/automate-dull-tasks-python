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

Uma variável é como uma caixa na memória do computador, em que podemos armazenar um único valor. Se quiser usar posteriormente o resultado de uma expressão avaliada em seu programa, você poderá salvá-la em uma variável.

# Instruções de atribuição

Valores são armazenados em variáveis por meio de uma instruçaõ de atribuição. Uma instrução de atribuição consiste de um nome de variável, um sinal de igualdade (chamado de atribuição) e o valor a ser armazenado. Se a instrução de atribuição 'spam = 42' for especificada, a variável chamada spam conterá o valor inteiro 42.
Pense em uma variável como uma caixa etiquetada em que um valor é inserido.


                  ------------
               /    42     /|
               ------------ |
              |           | |
              |           | |
              |           | /
               ------------/

# Nomes de variáveis

A tabela a seguir apresenta exmeplos de nomes permitidos para variáveis. Você pode dar qualquer nome a uma variável desde que ela obedeça às três regras a seguir:
    1. O nome pode ser constituido somente de uma palavra.
    2. Somente letras, números e o caractere underscore (_) podem ser usados.
    3. O nome não pode começar com um número.
Há distinção entre letras maiúsculas e minúsculas nos nomes de variáveis (são case sensitive); isso quer dizer que spam, SPAM, Spam e sPaM são quatro variáveis diferentes. Iniciar as variáveis com uma letra minúscula é uma convenção do Python.
--------------------------------------------
Nomes válidos de variáveis  nomes inválidos de variáveis
--------------------------------------------------
balance                     current-balance(hífens não são permitidos)
currentBalance              current balance (espaços não são permitidos)
current_balance             4account (não pode começar com um número)
_spam                       42 (não pode começar com um número)
sPaM                        total_$um (caracteres especiais não são permitidos)
account4                    'hello' (caracteres especiais ' não são permitidos')

Este livro utiliza CAMELCASE para os nomes das variáveis no lugar de underscores, ou seja, usa variáveis como lookLikeThis em vez de looking_like_this. Alguns programadores experientes podem enfatizar o estilo oficial da codificação Python, a PEP 8, afirma que underscores devem ser usados. Sem fazer apologia, prefiro usar CAMELCASE e destaco "A Foolish Consistency Is the Hobgoblin of Little Minds" (Uma consistência tola é o demônio das mentes mediócres) na própria PEP 8:
    "A consistência usando o guia de estilos é importante. Porém, acima de tudo, saiba quando ser inconsistente- às vezes, o guia de estilo simplesmente não se aplica. Na dúvida, utilize o bom senso"
Um bom nome de variável descreve os dados que ela contém. Suponha que você tenha se mudado para uma casa nova e tenha etiquetado todas as caixas de mudança como Objetos. Você jamais encontrará nada! Os nomes de variáveis spam, eggs e bacon, são usados como nomes genéricos nos exemplos deste livro e em boa parte da documentação Python (inspirados no esquete "Spam" do Monty Python), porém em seus programas, um nome descritivo ajudará a deixar seu código mais legível.

# SEU PRIMEIRO PROGRAMA

print('Olá mundo!')
print('what is yout name?') #pergunta o nome
myName = input()
print('Nice to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') #pergunta idade
myAge = input()
print('You will be ' + str(int(myAge) + 1)+' in a year.')
===========================================================
        resultado
>>> ================================ RESTART
================================
>>>
Hello world!
What is your name?
Al
It is good to meet you, Al
The length of your name is:
2
What is your age?
4
You will be 5 in a year.
>>>


## DISSECANDO SEU PROGRAMA

# FUNÇÃO print()
A função print() exibe na tela o valor do tipo string que está entre parênteses.
'v'
print('Hello world')
print('What is your name?') #pergunta o nome
A linha print('hello world') quer dizer "exiba o texto que está na string 'hello world'!". Quando o Python executa essa linha, dizemos que ele está chamando a função print() e que o valor do tipo string está sendo passado para a função. Um valor passado para uma função chama-se argumento. Observe que as aspas não são exibidas na tela. Elas marcam os locais em que a string começa e termina e não fazem parte do valor da string.
    nota: Também podemos usar essa função para inserir uma linha em branco na tela; basta chamar print() sem nada entre parênteses.
Ao escrever um nome de função, os parênteses de abertura e de fechamento no final o identificam como o nome de uma função. É por isso que, neste livro, você verá print() em vez de print. O capítulo 2 descreve as funções com mais detalhes.

# FUNÇÃO input()
a FUNÇÃO print() espera o usuário digitar um texto no teclado e pressionar ENTER.
'w'
myName = Input()
Essa chamada de função é avaliada como uma string igual ao texto do usuário, e a linha de código anterior atribui o valor dessa string á variável myName.
Você pode pensar na chamada da função input() como uma expressão avaliada com qualquer string que o usuário digitar. Se o usuário digitar 'Al', a expressão será avaliada como myName = 'Al'.

# Exibindo o nome do usuário
A chamada a seguir a print() contém a expressão 'it is good to meet you, ' + myName entre parênteses.
'x'
print('it is good to meet you, ' + myName)
Lembre-se de que as expressões sempre podem ser avaliada como um único valor. Se 'Al' for o valor armazenado em myName na linha anterior, essa expressão será avaliada como 'it is good to meet you, '. Esse valor único de string então é passado para print(), que o exibirá na tela.

# Função len()
Podemos passar um valor de string à função len() (ou uma variável contendo uma string), e a função será avaliada como o valor inteiro referente à quantidade de caracteres dessa string.
'y'
print('The length of yout name is.')
print(len(myName))
Digite no shell interativo para testar:
>>>len('hello')
5
>>> len('eu não sei quantas letras tem nesta frase')
41
>>> len('')
0

Assim como nesses exemplos, len(myName) é avaliado como u inteiro. Esse valor é então passado para print() para ser exibido na tela. Observe que print() permite que tanto valores inteiros, quanto stings sejam passados a ele. Contudo observe o erro mostrado quando digitamos o seguinte no shell interativo:

print('i am' + 29 + 'years old.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects

Não é a função print() que está causando esse erro, mas a expressão que você tentou passar para ela. Você obterá a mesma mensagem de erro se digitar a expressão sozinha no shell interativo.

O Python mostra um erro porque podemos usar o operador + somente para somar dois inteiros ou concatenar duas strings. Não podemos osmar um inteiro e uma string, pois isso é agramatical em Python. Isso pode ser corrigido usando uma versão em string do inteiro, conforme explicado na próxima seção.


# Funções str(), int() e float()
Se quiser concatenar um inteiro como 29 a uma string e passar o resultado para print(), será necessário obter o valor '29', que é forma em string de 29. A função str() pode receber um valor inteiro e será avaliada como uma versão em string desse valor, da seguinte maneira:

>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.

(...)

As funções str(), int() e float() serão respectivamente avaliadas como as formas em string, inteiro e de ponto flutuante do valor que você passar.
Experimente converter alguns valores no shell interativo usando essas funções e observe o que acontece.

>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> int('42')
42
>>> int('-99')
-99
>>> int(1.25)
1
>>> int(1.99)
1
>>> float('3.14')
3.14
>>> float(10)
10.0

Os exemplos anteriores chamam as funções str(), int() e float() e passam valores de outros tipos de dados para obter a forma em string, inteiro ou de ponto flutuante desses valores.

A função str() será conveniente quando houver um inteiro ou um número de ponto flutuante que você queira concatenar em uma string. A função int() também será útil se houver um número na forma de string que você queira usar em alguma operação matemática. Por exemplo, a função input() sempre retorna uma string, mesmo que o usuário tenha forneceido um número. Digite spam = input() no shell interativo e forneça 101 quando seu texto estiver sendo esperado.

>>> spam = input()
101
>>> spam
'101

O valor armazenado em spam não é o inteiro 101, mas a string '101'. Se quiser realizar alguma operação matemática usando o valor em spam, utiliza a função int() para obter a forma inteira de spam e, em seguida, armazene esse resultado como o novo valor de spam.

>>> spam = int(spam)
>>> spam
101

Agora você poderá tratar a variável spam como um inteiro em vez de tratá-la como string.

>>> spam * 10 / 5
202.0

Observe que, se você passar um valor para int() que não possa ser avaliado como inteiro, o Python exibirá uma mensagem de TypeError

>>> int('99.99')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99.99'

int('twelve')
(...)

A função int() também será útil se você precisar arredondar um número de ponto flutuante para baixo.

>>> int(7.7)
7
>>> int(7.7) + 1
8

Em seu programa, você utilizou as funções int() e str() nas três últimas linhas para obter um valor com o tipo de dado apropriado ao código.
'z'
print('what is yout age?') #pergunta a idade
myAge = input()
print('You will be' + str(int(myAge) + 1) + 'in a year')

A variável myAge contém o valor retornado por input(). Como a função input() sempre retorna uma string (mesmo que o usuário tenha digitado um número), podemos usar o código int(myAge) para retornar o valor inteiro a partir da string em myAge. Esse valor inteiro é então somado a 1 na expressão int(myAge) + 1
O resultado dessa adição é passado para a função str(): str(int(myAge) + 1). O valor em string retornado é concatenado às strings 'You will be' e 'in a year' para ser avaliado como um valor mais extenso de string. Essa string maior é facilmente passada para print() para ser exibida na tela.
Vamos supor que o usuário forneça a string '4' para myAge. Astring '4' é convertida em um inteiro para que você possa somar um a esse valor. O resultado é 5. A fução str() converte o resultado de volta em uma string para que ela possa ser concatenada à segunda string 'in a year' e a mensagem final seja criada. Esses passos de avaliação são semelhantes ao que está sendo mostrado no exemplo abaixo:

# EQUIVALÊNCIA ENTRE TEXTO E NÚMERO
Embora o valor em string de um número seja considerado um valor totalmente diferente da versão inteira ou de ponto flutuante, um inteiro pode ser igual a um número de ponto flutuante.
>>> 42 == '42'
False
>>> 42 == 42.0
True
>>> 42 == 0042.000
True
O Python faz essa distinção porque as strings são texto, enquanto tanto inteiros quanto números de ponto flutuante são números.

(...)

EXERCÍCIOS PRÁTICOS

1. Quais das opções a seguir são operadores e quais são valores?
*
'hello'
-88.8
-
/
+
5

2. Qual das opções a seguir é uma vriável e qual é uma string?
- spam
'spam'

3. Nomeie três tipos de dados.

4. De que é composta uma expressão? O que fazem as expressões?

5. Este capítulo apresentou as instruções de atribuição, por exemplo, spam = 10. Qual é a diferença entre uma expressão e uma instrução?

6. O que a variável bacon conterá após o código a seguir ser executado?

7. Para que valores as duas expressões a seguir serão avaliadas?

8. Por que eggs é um nome válido de variável enquanto 100 é inválido?

9. Quais três funções podem ser usadas para obter uma versão inteira, de ponto flutuante ou em string de um valor?
int(), float() e str().

10. Porque a expressão a seguir causa um erro? Como você pode corrigi-la?
'i have eaten' + 99 'burritos'



