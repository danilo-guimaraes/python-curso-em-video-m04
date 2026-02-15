import random                                      # Importa a biblioteca para gerar números aleatórios

n1 = int(input('Pensei em um numero de 0 a 5, tente adivinhar: ').strip(' ')) # Lê o palpite do usuário e converte em número inteiro
print('PROCESSANDO...')                            # Exibe uma mensagem de espera para dar efeito ao jogo
if n1 == random.randint (0, 5):                    # SE o número digitado for IGUAL ao sorteado pelo PC entre 0 e 5
    print('voce acertou, parabens')                # Mensagem de vitória caso a comparação seja verdadeira
else:                                              # SENÃO (caso o número digitado seja diferente do sorteado)
    print('voce errou, tente novamente')           # Mensagem de derrota caso a comparação seja falsa


