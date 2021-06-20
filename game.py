import pygame

pygame.init()


largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/paisagem.png") #IMAGEMFUNDO

personagem = pygame.image.load("assets/lixeira.png") #PERSONAGEMLIXEIRA
escalaPersonagem = pygame.transform.scale(personagem,(180,150)) #formata para o tamanho certo

sacolixo = pygame.image.load("assets/sacolixo.png") #SACODELIXO
sacolixo.set_colorkey((255,255,255)) #tira a cor de fundo da png
escalaSacolixo = pygame.transform.scale(sacolixo,(110,110)) #formata para o tamanho certo

#CORES Início
preto = (0, 0, 0,)
branco = (255, 255, 255)
#CORES Fim

lixeiraX = largura* 0.40
lixeiraY = altura* 0.75
movimentoX = 0
sacolixoX = largura* 0.40
sacolixoY = -80
sacolixolargura = 130
sacolixoaltura = 110
velocidadesacolixo = 4 



while True:
    # Inicio do bloco de código que verifica a interação do usuário
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:    
            pygame.quit()
            quit()    
        if evento.type == pygame.KEYDOWN:#funções para interação de teclas
            if evento.key == pygame.K_LEFT:
                movimentoX = -5
            elif evento.key == pygame.K_RIGHT:
                movimentoX = 5
        if evento.type == pygame.KEYUP:
            movimentoX = 0
    
    
    
    
    
    
    # Fim do bloco de código que verifica a interação do usuário
    display.fill(branco) #Função que muda a cor de fundo da tela
    display.blit(fundo, (0, 0)) #Função que muda imagem de fundo da tela
    
    lixeiraX = lixeiraX + movimentoX #controla a lixeira dentro do display do game
    if lixeiraX < 0:
        lixeiraX = 0 
    elif lixeiraX > 610:
        lixeiraX = 610

    display.blit(escalaPersonagem, (lixeiraX, lixeiraY))
    
    display.blit(escalaSacolixo, (sacolixoX,sacolixoY))
    sacolixoY = sacolixoY + velocidadesacolixo
    if sacolixoY > altura:
        sacolixoY = -80
        velocidadesacolixo += 1
    
    
    pygame.display.update()
    fps.tick(60)