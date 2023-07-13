from random import randint, choice
print('='*50)
print('Bem-vindo ao gerador de dados. Caso queira finalizar o programa, digite "parar".')
dados = [{'nomes': ['Daniel', 'Rafael', 'Ryuk', 'Valda', 'Sidney']},
         {'e-mails': ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']},
         {'telefones': [int(str(9) + str(randint(00000000, 99999999)))]},
         # transformando em str para concatenar com o 9, e fazer com que sempre inicie com esse valor.
         # Porém, transformo pra int de novo, para que não permaneça como str.
         {'cidades': ['Rio de Janeiro', 'Angra dos Reis', 'Macaé', 'Maricá', 'Petrópolis']},
         {'estados': ['Rio de Janeiro', 'São Paulo', 'Rio Grande do Sul', 'Bahia', 'Acre']}]

while True:
    print('-'*50)
    print('Qual dado você quer que seja gerado aleatoriamente? ')
    escolha_usuario = str(input('[1] - Nomes\n'
                                '[2] - E-mails\n'
                                '[3] - Telefones\n'
                                '[4] - Cidade\n'
                                '[5] - Estado\n'
                                'Sua escolha: ')).lower()
    valor_incorreto = False
    if escolha_usuario == 'parar':
        break
    if escolha_usuario.isnumeric() and len(escolha_usuario) > 1:
        valor_incorreto = True
    elif ',' in escolha_usuario:
        qtd_virgulas = escolha_usuario.count(',')
        escolha_usuario = escolha_usuario.replace(',', '')
        qtd_numeros = len(escolha_usuario)
        if qtd_numeros - qtd_virgulas != 1:
            valor_incorreto = True
    if escolha_usuario.isnumeric() and valor_incorreto is False:
        # print(escolha_usuario.split(), len(escolha_usuario))
        escolha_gravacao = str(input('Digite "s" caso deseje salvar os dados em arquivo de texto')).lower()
        if escolha_gravacao == 's':
            arquivo = open('dados.txt', 'a')
        for c in escolha_usuario:
            escolha_usuario = c
            if escolha_usuario == '1' or '2' or '3' or '4' or '5':
                try:
                    posicao_na_lista = int(escolha_usuario) - 1
                    valores = dados[posicao_na_lista]
                    for k in valores.keys():
                        item_escolhido = choice(valores[k])
                        if escolha_usuario == '2':
                            # concatenando um nome aleatorio (em minúsculo) com a parte de trás do e-mail também aleatório.
                            item_escolhido = choice(dados[0]['nomes']).lower() + item_escolhido
                        if escolha_gravacao == 's':
                            arquivo.write(str(item_escolhido) + '\n')
                        print(item_escolhido)
                except (TypeError, ValueError):
                    print('Erro no tipo ou valor.')
                except Exception as causa:
                    print(f'Algo deu errado. Talvez o valor passado não seja uma das opções.')
        if escolha_gravacao == 's':
            print('Dados gravados com sucesso!')
            arquivo.close()
        else:
            print('Os dados não foram gravados.')
    else:
        print('Valor inválido.')