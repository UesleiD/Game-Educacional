import pygame

pygame.init()


largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()

#CORES Início
preto = (0, 0, 0,)
branco = (255, 255, 255)
#CORES Fim



while True:
    # Inicio do bloco de código que verifica a interação do usuário
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:    
            pygame.quit()
            quit()    
    
    # Fim do bloco de código que verifica a interação do usuário
    display.fill(branco) #Função que muda a cor de fundo da tela
    
    
    pygame.display.update()

    fps.tick(60)