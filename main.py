import pygame, sys
from pygame.locals import *
import pygame.mixer
import random
from scrore import update, show

size = width, height = (450, 700)
road_w = int(width/1.4)
roadmark_w = int(width/60)

pygame.init()
pygame.mixer.init()
pygame.font.init()

orange = (255, 165, 0)
red = 'red' #(255, 165, 0)
score_font = pygame.font.SysFont('ubuntu', 20)
score_font1 = pygame.font.SysFont('ubuntu', 30)
message_font = pygame.font.SysFont('ubuntu', 30)
message_font_level = pygame.font.SysFont('ubuntu', 20)

running = True

screen = pygame.display.set_mode(size,)
screen.fill((60, 220, 0))
score_area = pygame.Surface((65, 200))

pygame.display.set_caption("Rohit's car game")

crash_sound = pygame.mixer.Sound('crash_sound.wav')
back_sound = pygame.mixer.Sound('background_sound.wav')
engine_sound = pygame.mixer.Sound('engine_sound.wav')

def print_score(sc, sp):
    score_area.fill((60, 220, 0))
    text = score_font.render('score:', True, 'black')
    score_area.blit(text, [0, 0])
    text1 = score_font1.render(str(sc), True, 'red')
    score_area.blit(text1, [10, 20])

    
    game_over_message = score_font.render("speed:", True, 'black')
    score_area.blit(game_over_message, [0, 60])           
    game_over_message1 = score_font.render(f"{str(sp)}m/s", True, 'blue')
    score_area.blit(game_over_message1, [3,90])
    screen.blit(score_area, [0, 0])


def draw_image(screen, car_image, car_loc, car_image1, car_loc1):
    pygame.draw.rect(screen, (50, 50, 50), (width/2 - road_w/2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(car_image, car_loc)
    screen.blit(car_image1, car_loc1)

    
def run_game():
    speed = 1
    game_over = False
    game_close = False


    # highway_image = pygame.image.load('highways.jpg')
    # highway_width, highway_height = 300, 700
    # highway_image = pygame.transform.scale(highway_image, (highway_width, highway_height))

    # highway_loc = highway_image.get_rect()
    # highway_loc.x = width/2 - highway_loc.width/2
    # highway_loc.y = 0

    car_image = pygame.image.load('car1.png')
    car_width, car_height = 80, 160  # Set the desired width and height for the car
    car_image = pygame.transform.scale(car_image, (car_width, car_height))  # Resize the car image

    car_loc = car_image.get_rect()
    car_loc.x = width/3 - car_loc.width/2  # Set the x-coordinate to center the car horizontally
    car_loc.y = height * 0.7  # Set the y-coordinate to position the car vertically

    if random.randint(0, 1) == 0:
        car_image1 = pygame.image.load('car2.png')
        car_width1, car_height1 = 80, 160  # Set the desired width and height for the car
        car_image1 = pygame.transform.scale(car_image1, (car_width1, car_height1))  # Resize the car image

        car_loc1 = car_image1.get_rect()
        car_loc1.x = width/3 - car_loc1.width/2  # Set the x-coordinate to center the car horizontally
        car_loc1.y = height * 0.02  # Set the y-coordinate to position the car vertically

    else:
        car_image1 = pygame.image.load('carq.png')
        car_width1, car_height1 = 100, 160  # Set the desired width and height for the car
        car_image1 = pygame.transform.scale(car_image1, (car_width1, car_height1))  # Resize the car image

        car_loc1 = car_image1.get_rect()
        car_loc1.x = width/3 - car_loc1.width/2  # Set the x-coordinate to center the car horizontally
        car_loc1.y = height * 0.02  # Set the y-coordinate to position the car vertically


    counter = 0 
    car_sc = 0
    car_sp = 0
    while not game_over:
        counter += 1
        
        while game_close:

            game_over_message1 = message_font.render(f"your highest score '{show()}'", True, 'black')
            screen.blit(game_over_message1, [width / 6, height / 9])
            game_over_message1 = message_font.render("crashed!", True, red)
            screen.blit(game_over_message1, [width / 4, height / 5])
            game_over_message = message_font.render("Game Over!", True, orange)
            screen.blit(game_over_message, [width / 4, height / 3])
            game_over_message2 = message_font.render("tap to restart!", True, 'purple')
            screen.blit(game_over_message2, [width / 4, height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_PAGEDOWN:
                        run_game()

                    if event.key == pygame.K_SPACE:
                        run_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_close == True:
                        run_game()
                        #game_over = False
                

                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

            
        right_lane = width/2.1 + car_loc1.width/2
        left_lane = width/3 - car_loc1.width/2
        engine_sound.play()
        if counter == 1024:
            speed += 0.15
            counter = 0
        # highway_loc[1] += 700
        # if highway_loc[1] > height:
        #     highway_loc[1] = -200
        car_loc1[1] += speed
        if car_loc1[1] > height:
            car_loc1[1] = -200
            car_sc = car_sc + 3
            car_sp = car_sp + 1
            update(car_sc)
        
            if random.randint(0,1) == 0:
                car_loc1.x, car_loc1.y = right_lane, -200
                
            else:
                car_loc1.x, car_loc1.y = left_lane, -200

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    if car_loc.x > 223:
                        car_loc = car_loc.move([-int(road_w/2), 0])
                if event.key in [K_d, K_RIGHT]:
                    if car_loc.x < 233 :
                        car_loc = car_loc.move([int(road_w/2), 0])
                
                if event.key in [K_d, K_2]:
                    game_close = True                    
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # print(mouse_x, mouse_y)


                if mouse_x > 223 and car_loc.right < road_w:
                    car_loc = car_loc.move([int(road_w/2), 0])
                
                if mouse_x < 223 and car_loc.left > int(road_w/2):
                    car_loc = car_loc.move([-int(road_w/2), 0])


            # if event.type == pygame.MOUSEBUTTONUP:
            #     print('mouse up')

            # if event.type == pygame.FINGERDOWN:
            #     print("Finger touched the screen")
            # if event.type == pygame.FINGERUP:
            #     print("Finger touched the screen")

        if car_loc.colliderect(car_loc1):
            crash_sound.play()
            game_close = True
                

        draw_image(screen, car_image, car_loc, car_image1, car_loc1)
        # screen.blit(highway_image, highway_loc)

        print_score(car_sc, car_sp)
        back_sound.play()
        pygame.display.update()

    pygame.quit()
    quit()

run_game()
