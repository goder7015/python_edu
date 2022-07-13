import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode([800,500])
screen.fill([255,255,255])

pet_images = ['Pet正常.png','Pet睡觉.png','Pet高兴.png','Pet死.png','Pet生病.png','Pet生气.png']
玩_image = ['玩.png']
看病_image = ['看病.png']
食物_image = ['食物.png']
散步_image = ['散步.png']

class PetClass (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pet正常.png')
        self.rect = self.image.get_rect()
        self.rect.center = [400,350]
        self.angle = 0

def animate():
    screen.fill([255,255,255])
    screen.blit(pet.image,pet.rect)
   
    screen.blit(玩.image,玩.rect)
    screen.blit(看病.image,看病.rect)
    screen.blit(食物.image,食物.rect)
    screen.blit(散步.image,散步.rect)
   
    pygame.display.flip()        
    
class Do1Class (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('玩.png')
        self.rect = self.image.get_rect()
        self.rect.center = [270,40]
        self.angle = 0

def animate1():
    screen.blit(玩.image,玩.rect)
    
    pygame.display.flip()
    
class Do2Class (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('看病.png')
        self.rect = self.image.get_rect()
        self.rect.center = [350,40]
        self.angle = 0
        
def animate2():
    screen.blit(看病.image,看病.rect)
    pygame.display.flip()
    
class Do3Class (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('食物.png')
        self.rect = self.image.get_rect()
        self.rect.center = [430,40]
        self.angle = 0
        
def animate3():
    screen.blit(食物.image,食物.rect)
    pygame.display.flip()
    
class Do4Class (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('散步.png')
        self.rect = self.image.get_rect()
        self.rect.center = [510,40]
        self.angle = 0
        
def animate4():
    screen.blit(散步.image,散步.rect)
    pygame.display.flip()
    
pet = PetClass()
玩 = Do1Class()
看病 = Do2Class()
食物 = Do3Class()
散步 = Do4Class()

i = 1
hungry = 1
happy = 10
health = 1
sleep = random.randint(1,1)
time = random.randint(10,20)

running = True
while running:
    
    for event in pygame.event.get():
        if happy >= 100:
            happy = 100

        if happy < 1:
            happy = 1
                
        if hungry >= 10:
            hungry = 10
                
        if hungry < 1:
            hungry = 1
                
        if health >= 10:
            health = 10

        if health < 1:
            health = 1
        if event.type == pygame.QUIT:
            running = False
        
        
        elif event.type == pygame.KEYDOWN:
            if hungry == 1:
                pet.image = pygame.image.load('Pet饿.png')
                animate()
                happy -= 10
                health -= 1
                hungry -= 1
                pygame.time.delay(3000)            
            if event.key == pygame.K_3:
                hungry = hungry + 2
                pet.image = pygame.image.load('Pet吃.png')
                animate()
                pygame.time.delay(1000)
                if hungry >= 10:
                    pet.image = pygame.image.load('Pet饱.png')
                    animate()
                    happy += 10
                    pygame.time.delay(3000)
                    pet.image = pygame.image.load('Pet睡觉.png')
                    animate()
                    pygame.time.delay(sleep * 1000 * time)
                    pet.image = pygame.image.load('Pet睡觉1.png')
                    animate()
                    pygame.time.delay(200)
                    pet.image = pygame.image.load('Pet睡觉2.png')
                    animate()
                    pygame.time.delay(200)
                    pet.image = pygame.image.load('Pet睡觉1.png')
                    animate()
                    pygame.time.delay(200)
                    pet.image = pygame.image.load('Pet睡觉2.png')
                    animate()
                    pygame.time.delay(200)
                    pet.image = pygame.image.load('Pet睡觉1.png')
                    animate()
                    pygame.time.delay(200)
                    pet.image = pygame.image.load('Pet正常.png')
                    animate()
                    health = random.randint(8,10)
                    hungry = random.randint(1,9)
                else:
                    pet.image = pygame.image.load('Pet正常.png')
                    animate()
                    
        
            if health < 6:
                pet.image = pygame.image.load('Pet生病.png')
                animate()
                pygame.time.delay(3000)
                if event.key == pygame.K_2:
                    health = 10
                    pet.image = pygame.image.load('Pet生病.png')
                    animate()
                    pygame.time.delay(1500)
                
                    if health == 10:         
                        pet.image = pygame.image.load('Pet正常.png')
                        animate()
                    elif health <= 6:
                        pet.image = pygame.image.load('Pet生病.png')
                        happy -= 10
                        animate()

            if event.key == pygame.K_4:
                pet.image = pygame.image.load('Pet散步1.png')
                animate()
                pygame.time.delay(3000)
                happy = happy + 5
                hungry = hungry -2
                health = health + 2

            if event.key == pygame.K_1:
                pet.image = pygame.image.load('Pet高兴.png')
                animate()
                pygame.time.delay(200)
                pet.image = pygame.image.load('Pet高兴1.png')
                animate()
                pygame.time.delay(200)
                pet.image = pygame.image.load('Pet高兴2.png')
                animate()
                pygame.time.delay(200)
                pet.image = pygame.image.load('Pet高兴1.png')
                animate()
                pygame.time.delay(200)
                pet.image = pygame.image.load('Pet高兴.png')
                animate()
                pygame.time.delay(500)

                       
                
                happy = happy + 10
                hungry = hungry -1
                
            if happy <= 50 and hungry == 1 and health == 1:
                pet.image = pygame.image.load('Pet死.png')
                animate()
                pygame.quit()
            

        if sleep == 1:
            pet.image = pygame.image.load('Pet睡觉.png')
            animate()
            pygame.time.delay(sleep * 1000 * time)
            pet.image = pygame.image.load('Pet睡觉1.png')
            animate()
            pygame.time.delay(200)
            pet.image = pygame.image.load('Pet睡觉2.png')
            animate()
            pygame.time.delay(200)
            pet.image = pygame.image.load('Pet睡觉1.png')
            animate()
            pygame.time.delay(200)
            pet.image = pygame.image.load('Pet睡觉2.png')
            animate()
            pygame.time.delay(200)
            pet.image = pygame.image.load('Pet睡觉1.png')
            animate()
            pygame.time.delay(200)
            pet.image = pygame.image.load('Pet正常.png')
            animate()
            
            happy += 5
            health = random.randint(6,10)
            hungry = random.randint(5,9)
            sleep = sleep + 1
        else:
            pet.image = pygame.image.load('Pet正常.png')
            animate()
            
                
pygame.quit()