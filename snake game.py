import pygame
import time
import random


# Inicializando o pygame
pygame.init()


# Criando a tela
dis_width = 400  # largura
dis_height = 400  # altura
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 210)



# Tamanho do bloco que representa a cobra e velocidade do jogo/cobra
snake_block = 10
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])


def you_lost():
    mesg = font_style.render('You Lost', True, red)
    dis.blit(mesg, [dis_width / 3, dis_height / 3 + 20])
    mesg = font_style.render('Q-Quit or C-Continue', True, red)
    dis.blit(mesg, [dis_width/3, dis_height/3 + 50])


def gameLoop():  # creating a function
    game_over = False
    game_close = False

    # Posicionamento Inicial Centralizado
    x1 = dis_width / 2
    y1 = dis_height / 2
    # Mudança
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Localização da comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    # Evita que o jogador inverta o movimento totalmente
    last_key = 0

    while not game_over:
        # Jogador Perdeu
        while game_close:
            dis.fill(white)
            you_lost()
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != pygame.K_RIGHT:
                    x1_change = -snake_block
                    y1_change = 0
                    last_key = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and last_key != pygame.K_LEFT:
                    x1_change = snake_block
                    y1_change = 0
                    last_key = pygame.K_RIGHT
                elif event.key == pygame.K_UP and last_key != pygame.K_DOWN:
                    y1_change = -snake_block
                    x1_change = 0
                    last_key = pygame.K_UP
                elif event.key == pygame.K_DOWN and last_key != pygame.K_UP:
                    y1_change = snake_block
                    x1_change = 0
                    last_key = pygame.K_DOWN

        # Teste se a cobra foi além da "parede"
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        # Inserindo a comida
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Se a cobra bater no próprio corpo, game over
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

