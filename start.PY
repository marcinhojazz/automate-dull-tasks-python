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

passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password: ')
typedPassword = input ()
if typedPassword == secretPassword:
    print('acess granted')
    if typedPassword == '12345'
        print('That password is one that an idiot puts on their luggage')
else:
    print('Acess denied')
