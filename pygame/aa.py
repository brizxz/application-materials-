import pygame
import random
FPS=60
WIDTH=500
HEIGHT=600


#遊戲初始化 和 創建視窗
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()  #一秒鐘最多被執行幾次 (FPS)
pygame.display.set_caption("哈哈") #設置名字
running=True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #初始函式
        self.image=pygame.Surface((50,40))  #圖案
        self.image.fill((0,255,0))
        self.rect= self.image.get_rect() #框起來 定位
        self.rect.center=((250,300))
        self.rect.bottom=HEIGHT-10
        self.speedx=8 #定義一個速度的變數

    def update(self):
        keypressed=pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if keypressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH: #使到底後卡住
            self.rect.right= WIDTH
        if self.rect.left < 0:
            self.rect.left=0

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        allsprites.add(bullet)
        bullets.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #初始函式
        self.image=pygame.Surface((30,25))  #圖案
        self.image.fill((255,0,0))
        self.rect= self.image.get_rect() #框起來 定位
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(2,20) #定義一個速度的變數
        self.speedx=random.randrange(-5,5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left>WIDTH or self.rect.right<0:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(2,20) #定義一個速度的變數
            self.speedx=random.randrange(-5,5)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) #初始函式
        self.image=pygame.Surface((10,10))  #圖案
        self.image.fill((255,255,0))
        self.rect= self.image.get_rect() #框起來 定位
        self.rect.centerx=x
        self.rect.bottom=y
        self.speedy= -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom<0:
            self.kill() #移除
#創建sprite群組

allsprites=pygame.sprite.Group()
rocks=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()
allsprites.add(player)
for i in range(8):
    rock=Rock()
    allsprites.add(rock)
    rocks.add(rock)

#遊戲迴圈

while running:
    clock.tick(FPS) #FPS 畫面每秒更新次數

    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #離開
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    allsprites.update() #更新遊戲
    hit=pygame.sprite.groupcollide(rocks,bullets,True,True)
    for hits in hit:
        r=Rock()
        allsprites.add(r)
        rocks.add(r)
    
    gameover=pygame.sprite.spritecollide(player,rocks,False)
    if gameover:
        running = False

    #顯示畫面
    screen.fill((0,0,0)) #RED GREEN BLUE
    allsprites.draw(screen) #將sprite畫出來
    pygame.display.update()

pygame.quit()