import pygame,time,random

pygame.init()
arquivo = open ("dados.txt","a")
nome = input(str( "Qual é o seu Nome? " ))
gmail = input(str( "Qual é o seu E-mail? " )) 
arquivo.write(nome + " "+ gmail + " \n") 
arquivo.close()


certa = pygame.mixer.music.load("assets/certa.wav")
icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("It's Raining Garbage")
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



#CORES {INI}
preto = (0, 0, 0,)
branco = (255, 255, 255)
#CORES {FIM}

def mostrarsacospegos(sacospegados):
    fonte = pygame.font.SysFont(None,25)
    texto = fonte.render("Lixos Coletados:"+str(sacospegados), True, preto)
    display.blit(texto, (0, 0))

def mostrarlixosperdidos(lixosperdidos):
    fonte = pygame.font.SysFont(None,25)
    texto = fonte.render("Lixos perdidos:"+str(lixosperdidos), True, preto)
    display.blit(texto, (650, 0))

def mostraperdeu():
    fonte = pygame.font.SysFont(None,50)
    texto = fonte.render("Você deixou 3 sacos de lixo cair!", True, preto)
    display.blit(texto, (130, 300))   
    pygame.display.update()






def jogo():
    pygame.mixer.music.load("assets/fundomusica.mp3")
    pygame.mixer.music.play(-1) #música fica no loop
    lixeiraX = largura* 0.40
    lixeiraY = altura* 0.75
    movimentoX = 0
    sacolixoX = largura* 0.40
    sacolixoY = -80
    sacolixolargura = 130
    sacolixoaltura = 110
    velocidadesacolixo = 4 

    sacospegados = 0
    lixosperdidos = 0
    while True:
        #bloco de código que verifica a interação do usuário {INI}
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:    
                pygame.quit()
                quit()    
            if evento.type == pygame.KEYDOWN:#funções para interação de teclas
                if evento.key == pygame.K_LEFT:
                    movimentoX = -15
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 15
            if evento.type == pygame.KEYUP:
                movimentoX = 0
         #bloco de código que verifica a interação do usuário {FIM}
        
        
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
        #quando ele atravessa a tela ele cai de outra posição {INI}
        if sacolixoY > altura:
            sacolixoY = -80
            velocidadesacolixo += float(0.3)
            sacolixoX = random.randrange(0, largura -150)
            lixosperdidos +=1
        #quando ele atravessa a tela ele cai de outra posição {FIM}
        
        #Analise de colisão para contagem
        if lixeiraY < sacolixoY + sacolixoaltura:
            
            if lixeiraX < sacolixoX and lixeiraX+100 > sacolixoX or sacolixoX+60 > lixeiraX and sacolixoX+60 < lixeiraX+100:
                sacolixoY = -80
                sacolixoX = random.randrange(0, largura -150)
                
                sacospegados += 1
                
        if lixosperdidos >= 3:
            mostraperdeu() 
            time.sleep(3)
            pygame.quit()
             

       
        
        
        
        mostrarsacospegos(sacospegados)
        mostrarlixosperdidos(lixosperdidos)
        pygame.display.update()
        fps.tick(60)

jogo()