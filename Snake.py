import pygame
import random
pygame.init()
pygame.font.init()
window_resolution = (1024,768)
window=pygame.display.set_mode(window_resolution)
pygame.display.set_caption('Snake, now with GUI')
font = pygame.font.Font('freesansbold.ttf', 12)
watermark = font.render("Wilmer Liljenström  2022", 'black','black')

food_color=(255,0,0) #red
snake_size=(30,45) #width, length
body_size=(25,25)
food_size=(40,40)
food_list_x = []
food_list_y = [] 
for i in range(0,15):
    food_list_x.append(window_resolution[0]/16*i+window_resolution[0]/32-food_size[0]/2)  #List of different positions on map
    food_list_y.append(window_resolution[1]/16*i+window_resolution[1]/32-food_size[1]/2)  #with coordinates in checkered

clock = pygame.time.Clock()
player = pygame.image.load("player.png")
player = pygame.transform.scale(player,snake_size)
body = pygame.image.load("body.png")
body = pygame.transform.scale(body, body_size)
food = pygame.image.load("food.png")
food = pygame.transform.scale(food,food_size)
field = pygame.image.load("field.png")
field = pygame.transform.scale(field,(window_resolution[0]+40,window_resolution[1]+20))
field.blit(watermark, (window_resolution[0]/2-40,window_resolution[1]-15))
pygame.display.update()
current_rotation = 0
def draw_snake(snake_length):
    for x in snake_length:
        #pygame.draw.rect(window, 'darkgreen',[x[0]*30*i,x[1],25,25])
        window.blit(body, [x[0], x[1]])
def gameloop():
    global food_list_x
    global food_list_y
    game_over=False
    x1 = window_resolution[0]/2
    y1 = window_resolution[1]/2
    x1_change = 0       
    y1_change = 0
    rand_x = round(random.randrange(1, 15))
    rand_y = round(random.randrange(1, 15))
    food_x = food_list_x[rand_x]
    food_y = food_list_y[rand_y]
    food_pos = (food_x,food_y)
    snake_length = []
    snake_l = 0
    while not game_over:
        global player
        global current_rotation
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if current_rotation == 1:
                        player = pygame.transform.rotate(player,90)
                    elif current_rotation == 2:
                        continue #Don't allow turn into self
                    elif current_rotation == 3:
                        player = pygame.transform.rotate(player,-90)
                    y1_change = -8
                    x1_change = 0
                    current_rotation=0
                elif event.key == pygame.K_RIGHT:
                    if current_rotation == 0:
                        player = pygame.transform.rotate(player,-90)
                    elif current_rotation == 2:
                        player = pygame.transform.rotate(player,90)
                    elif current_rotation == 3:
                        continue 
                    x1_change = 8
                    y1_change = 0
                    current_rotation=1
                elif event.key == pygame.K_DOWN:
                    if current_rotation == 0:
                        continue
                    elif current_rotation == 1:
                        player = pygame.transform.rotate(player,-90)
                    elif current_rotation == 3:
                        player = pygame.transform.rotate(player,90)
                    y1_change = 8
                    x1_change = 0
                    current_rotation=2
                elif event.key == pygame.K_LEFT:
                    if current_rotation == 0:
                        player = pygame.transform.rotate(player,90)
                    elif current_rotation == 1:
                        continue
                    elif current_rotation == 2:
                        player = pygame.transform.rotate(player,-90)
                    x1_change = -8
                    y1_change = 0
                    current_rotation=3
        x1 += x1_change
        y1 += y1_change
        if x1<=-25:
            x1=window_resolution[0]-35
        elif x1>=window_resolution[0]-35:
            x1=0
        elif y1<=-35:
            y1=window_resolution[1]-35
        elif y1>=window_resolution[1]-35:
            y1=0
        if abs(x1-food_pos[0])<=20 and abs(y1-food_pos[1])<=20:
            rand_x = round(random.randrange(1, 15)) #Fetch random intergers for positioning of food
            rand_y = round(random.randrange(1, 15)) #on map
            food_x = food_list_x[rand_x]
            food_y = food_list_y[rand_y]
            food_pos = (food_x,food_y)
            snake_l += 1
        
        window.blit(field,(-20,-14))
        window.blit(player, (x1,y1))
        window.blit(food,food_pos)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_length.append(snake_Head)

        if len(snake_length) > snake_l:
            del snake_length[0]
 
        for x in snake_length[:0]:
            if x == snake_Head:
                game_close = True
 
        draw_snake(snake_length)

        pygame.display.update()
        
        clock.tick(30)

 
    pygame.quit()
    quit()
gameloop()