import pygame
import random
class Background:
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
    def load_image(self):
        screen.blit(background.image, background.rect)

class Monster:
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.dir = ['n','s','w','e']
    def load_image(self, it):
        ch = 'e'
        '''
        if it % 120 == 0:
            ch = self.dir[random.randint(0,3)]
        if ch == 'n':
            self.rect[1] += 1
        elif ch == 's':
            self.rect[1] -= 1
        elif ch == 'w':
            self.rect[0] -= 1
        else:
            self.rect[0] += 1    
        '''
        if self.rect[0] > 500:
            self.rect[0] = 0
        elif self.rect[0] < 0:
            self.rect[0] = 500
        elif self.rect[1] > 500:
            self.rect[1] = -500
        else:
            self.rect[1] = 500
        
        

class Hero:
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def load_image(self):
        screen.blit(self.image, self.rect)
        self.rect[0] += 5
        if self.rect[0] > 500:
            self.rect[0] = 0



def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    it = 0
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    background = Background('background.png',[0,0])
    monster = Monster('./images/monster.png', [5,5])
    hero = Monster('./images/hero.png', [250,250])
    change_dir_countdown = 120
    clock = pygame.time.Clock()

    # Game initialization
    
    stop_game = False
    while not stop_game:
        
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        #screen.fill(blue_color)
        screen.fill([255, 255, 255])
        
        screen.blit(background.image, background.rect)
        screen.blit(monster.image, monster.rect)
        screen.blit(hero.image, hero.rect)
        
        #Game logic
        monster.load_image(it)
        
        # Game display

        pygame.display.update()
        pygame.time.delay(1)
        it += 1
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
