import random
#implementa geradores de números aleatórios

palavras = ['abacate','chocolate','paralelepipedo','goiaba']
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def insira():
    while True:
        w = input('insira a palavra/letra: ')
        palavras.append(w)
        if w == '':
            break
    
def principal():
    #define a(s) função(oẽs)
    """
    Função Princial do programa
    """
    print('F O R C A')
    insira()
    #imprime na tela

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:
        #à medida que for verdade
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            #caso
            print('Voce Perdeu!!!')
            break
        #quebra
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG
    #algo ou aquilo indefinido
    if len(letrasErradas) == len(FORCAIMG):
        #para medir um número de elementos de uma lista ou string
        return True
    #voltar para True
    else:
        #Senão
        return False
    #voltar para false
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        #para tal letra  #neste
        if letra not in letrasCertas:
            #não estar
            ganhou = False
            #falso
    return ganhou
    #retornar para
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    #colocar algo no texto
    palpite = palpite.upper()
    #deixa tudo maiusculo
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        #else + if              #ou
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        #oposto a elif
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            #para a variavel
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()

