# INTRUDOÇÃO

# Automatizar tarefas simples como:
#     - mover e renomear milhares de arquivos e organizá-los em pastas;
#     - preencher formulários online sem que seja necessário digitar;
#     - fazer download de arquivos ou copiar textos de um site sempre que ele for atualizado;
#     - fazer seu computador enviar notificações personalizadas a você;
#     - atualizar ou formatar planilhas Excel;
#     - verificar seus emails e enviar respostas previamente redigitas.

# CONVENÇÕES

# (...)

'''u'''passwordFile = open('SecretPasswordFile.txt')
'''v'''secretPassword = passwordFile.read()
'''w'''print('Enter your password: ')
''' '''typedPassword = input ()
'''x'''if typedPassword == secretPassword:
'''y'''    print('acess granted')
'''z'''    if typedPassword == '12345'
'''{'''        print('That password is one that an idiot puts on their luggage')
''' '''else:
'''|'''    print('Acess denied')

"""Inicialmente o arquivo SecretPasswordFile.txt é aberto 'u' e a senha secreta contida nele é lida 'v'. Em seguida, o usuário é solicitado a fornecer uma senha (por meio do teclado) 'w'. Essas duas senhas são comparadas 'x' e, se forem iguais, o programa exibe 'Acess granted' na tela 'y'. A seguir o programa verifica se a senha é 12345 'z' e oferece uma dica informando que essa opção pode não ser a melhor para uma senha '{'. Se as senhas não forem iguais, o programa exibirá 'Acess denied' na tela '|'. """


- Programadores não precisam saber muita matemática
A ansiedade mais comum que ouço falar sobre aprender a programar está relacionada ao fato de as pessoas acharem que isso exige bastante matemática. Na verdade, a maior parte do que é feito em programação exige apenas conhecimentos de aritimética básica(...) Ser bom em programação não é tão diferente de ser bom em solucionar SUDOKUS.


- Programação é uma atividade CRIATIVA
É algo como construir um castelo de LEGO. Começamos com uma idéia básica de como queremos nosso castelo, avaliamos os blocos disponíveis, e então começamos a construir. Após a construção do castelo, podemos trabalhar para deixa-lo mais elegante.



<<<<<<<SOBRE ESTE LIVRO>>>>>>>>

A primeira parte inclui os conceitos básicos de programação Python; a segunda aborda diversas tarefas que você poderá fazer para o seu computador se automatizar. Cada capítulo da segunda parte contém programas de projetos para você estudar. Eis um breve resumo do que você encontrará em cada capítulo:

>>> PARTE I: Básico da programação Python

    - CAPÍTULO 1: Básico sobre o Python inclui expressões, que são o tipo mais básico da instrução em Python, e como usar o software de shell interativo do Pythonpara testar o código.
    - CAPÍTULO 2: Controle de fluxo explica como fazer os programas decidirem quais intruções devem ser executadas para que seu código possa responder de modo inteligente a diferentes condições.
    - CAPÍTULO 3: Funções ensina como definir suas próprias funções para que você possa organizar seu código em partes mais administráveis.
    - CAPÍTULO 4: Listas apresenta o tipo de dado lista e explica como organizar dados.
    - CAPÍTULO 5: Dicionários e estruturação de dados apresenta otipo de dado dicionário e mostra maneiras mais eficientes de organizar dados.
    - CAPÍTULO 6: Manipulação de strings aborda o trabalho com dados do tipo texto (chamado de strings em Python)



>>> PARTE II: AUTOMATIZANDO TAREFAS

    - CAPÍTULO 7: Correspondência de padrões com expressões regulares discute como o Python pode manipular strings e procurar padrões textuais usando expressões regulares.
    - CAPÍTULO 8: LENDO e escrevendo em arquivos explica como seus programas podem ler o conteúdo de arquivo do tipo texto e slavar informações em arquivos em seu disco rígido.
    - CAPÍTULO 9: Organizando arquivos mostra como o Python pode copiar, mover, renomear e apagar uma quantidade grande de arquivos de forma muito mais rápida do que um usuário humano poderia fazer. Também explica a compactação e a descompactação de arquivos.
    - CAPÍTULO 10:  Debugging mostra como usar as diversas ferramentas do Python para identificação e correção de bugs.
    - CAPÍTULO 11: Web scraping mostra como criar programas que possam fazer download automaticamente de páginas web e fazer parse dessas páginas em busca de informações. Esse processo se chama WEB SCRAPING.
    - CAPÍTULO 12: Trabalhando com planilhas excel discute a manipulação de planilhas Exceli por meio de programação para que não seja necessário lê-las. Será conveniente quando o número de documentos a ser analisado estiver na casa das centenas ou dos milhares.
    - CAPÍTULO 13: Trabalhando com documentos PDF e Word discute como ler documentos WORD E PDF usando programação.
    - CAPÍTULO 14: Trabalhando com arquivos CSV e dados JSON Continua explicando como manipular documentos contendo arquivos CSV e JSON usando programação.
    - CAPÍTULO 15: Monitorando tempo, agendando tarefas e iniciando programas explica como datas e horas são tratadas pelos programas Python e como agendar seu computador para que realize tarefas em determinados horários. Este capítulo também mostra como seus programas Python podem iniciar programas que não tenham sido criados nessa linguagem.
    - CAPÍTULO 16: Enviando emails e mensagens de texto explica como criar programas que possam enviar emails e mensagens de texto em seu nome.
    - CAPÍTULO 17: Manipulando imagens explica como manipular imagens como arquivos JPEG e PNG usando programação.
    - CAPÍTULO 18: Controlando o teclado e o mouse com automação de GUI explica como controlar o mouse e o teclado para automatizar cliques e pressionamento de teclas usando programação.
