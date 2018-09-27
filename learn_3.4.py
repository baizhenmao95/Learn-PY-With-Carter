# coding:utf-8
import sys, pygame, random
skier_images = ["/home/sjt/PycharmProjects/f&s_learnpy/skier_down.png","/home/sjt/PycharmProjects/f&s_learnpy/skier_right1.png",
                "/home/sjt/PycharmProjects/f&s_learnpy/skier_right2.png","/home/sjt/PycharmProjects/f&s_learnpy/skier_left2.png",
                "/home/sjt/PycharmProjects/f&s_learnpy/skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/home/sjt/PycharmProjects/f&s_learnpy/skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.angle = 0
    def turn(self,direction):
        self.angel = self.angle + direction
        if self.angle <-2: self.angle = -2
        if self.angle > 2: self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed
    def move(self,speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
            pygame.sprite.Sprite.__init__(self)
            self.image_flie = image_file
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.center = location
            self.type = type
            self.passed = False
    def update(self):
            global speed
            self.rect.centery -= speed[1]
            if self.rect.centery <-32:
                self.kill()
def create_map():
        global obstacles
        locations = []
        for i in range(10):
            row = random.randint(0,9)
            col = random.randint(0,9)
            location = [col * 64 +20, row *64 +20 +640]
            if not (location in locations):
                locations.append(location)
                type = random.choice(["tree", "flag"])
                if type == "tree": img = "/home/sjt/PycharmProjects/f&s_learnpy/skier_tree.png"
                elif type == "flag": img = "/home/sjt/PycharmProjects/f&s_learnpy/skier_flag.png"
                obstacle = ObstacleClass(img, location, type)
                obstacles.add(obstacle)
def animate():
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10,10])
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)

# running = True

signinit = 1;

while True:
        clock.tick(30)		# 每秒更新30次图形 ---这就是帧率。
        if signinit == 1:
            pygame.init()
            signinit = 0
        for event in pygame.event.get():    # 检查按键或者窗口是否关闭
            if event.type == pygame.QUIT:
#                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed = skier.turn(1)
        skier.move(speed)			# 移动滑雪者
        map_position += speed[1]		# 滚动场景

        if map_position >=640:
            create_map()
            map_position = 0

        hit = pygame.sprite.spritecollide(skier, obstacles, False)
        if hit:
            if hit[0].type == "tree" and not hit[0].passed:
                points = points - 100
                skier.image = pygame.image.load("/home/sjt/PycharmProjects/f&s_learnpy/skier_crash.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("/home/sjt/PycharmProjects/f&s_learnpy/skier_down.png")
                skier.angle = 0
                speed = [0, 6]
                hit[0].passed = True
            elif hit[0].type == "flag" and not hit[0].passed:
                points += 10
                hit[0].kill()

        obstacles.update()
        score_text = font.render("Score: " + str(points), 1, (0,0,0))
        animate()
pygame.quit()




