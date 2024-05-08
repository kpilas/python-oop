import pygame, os, random

pygame.init()

SIZESCREEN = WIDTH, HEIGHT = 1366, 740
screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()
# wczytywanie grafik
path = os.path.join(os.getcwd(), 'images')
file_names = os.listdir(path)

BACKGROUND = pygame.image.load(os.path.join(path, 'background.jpg')).convert()
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
DARKRED = pygame.color.THECOLORS['darkred']

file_names.remove('background.jpg')
IMAGES = {}

for file_name in file_names:
    image_name = file_name[:-4].upper()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, image, cx, cy, fire_list):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
        self.level = None
        self.fire_list = fire_list
        self.fire = self.fire_list[0]
        self._count = 0
        self.lives = 3
        self.points = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.fire, [self.rect.centerx - self.fire.get_rect().width // 2, self.rect.centery + 40])

    def update(self, key_pressed):
        self.get_event(key_pressed)
        self._move(self.fire_list, 3)

        # blokujmy wyjście poza ekran gry
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > WIDTH:
            self.rect.centerx = WIDTH


        # kolizje z meteorem
        if pygame.sprite.spritecollideany(self, self.level.set_of_meteors):
            self.lives -= 1
            pygame.time.delay(200)
            self.level.set_of_meteors.empty()

    def shoot(self):
        if len(self.level.set_of_bullets) < 10:
            bl = Bullet(IMAGES['LASER2'], self.rect.centerx - 45, self.rect.centery, -10)
            br = Bullet(IMAGES['LASER2'], self.rect.centerx + 45, self.rect.centery, -10)
            if not pygame.sprite.groupcollide([bl, br], self.level.set_of_bullets, False, False):
                self.level.set_of_bullets.add(bl, br)

    def _move(self, image_list, speed_animation):
        self.fire = image_list[self._count // speed_animation]
        self._count = (self._count + 1) % (len(image_list) * speed_animation)

    def get_event(self, key_pressed):
        if key_pressed[pygame.K_LEFT]:
            self.rect.move_ip([-8, 0])
        if key_pressed[pygame.K_RIGHT]:
            self.rect.move_ip([8, 0])
        if key_pressed[pygame.K_UP]:
            self.rect.move_ip([0, -8])
        if key_pressed[pygame.K_DOWN]:
            self.rect.move_ip([0, 8])
        if key_pressed[pygame.K_SPACE]:
            self.shoot()


# klasa pocisku
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, cx, cy, movement_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
        self.movement_y = movement_y

    def update(self):
        self.rect.y += self.movement_y


class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_bullets = pygame.sprite.Group()
        self.text_of_points = Text(self.player.points, LIGHTBLUE, WIDTH-80, 40, 78)

    def update(self):
        self.text_of_points.text = str(self.player.points)
        self.set_of_bullets.update()
        self.text_of_points.update()

        # usuwanie pocisków znajdujących się poza ekranem
        for b in self.set_of_bullets:
            if b.rect.bottom < 0:
                b.kill()

    def draw(self, surface):
        self.set_of_bullets.draw(surface)
        self.text_of_points.draw(surface)

        # rysowanie żyć
        for i in range(self.player.lives - 1):
            surface.blit(IMAGES['PLAYERLIFE'], (20 + i * 45, 20))


class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        self.set_of_meteors = pygame.sprite.Group()

    def update(self):
        super().update()
        self.set_of_meteors.update()
        self._add_meteor()

        # usuwanie meteorow znajdujących się poza ekranem
        for m in self.set_of_meteors:
            if m.rect.top > HEIGHT:
                m.kill()
            elif pygame.sprite.spritecollide(m, self.set_of_bullets, True):
                if 'TINY' in m.name:
                    self.player.points += 5
                elif 'SMALL' in m.name:
                    self.player.points += 5
                elif 'MID' in m.name:
                    self.player.points += 2
                else:
                    self.player.points += 1
                m.kill()

    def draw(self, surface):
        self.set_of_meteors.draw(surface)
        super().draw(surface)


    def _add_meteor(self):
        if random.randint(1, 10) == 1:
            name = random.choice(Meteor.name_list)
            m = Meteor(IMAGES[name], 4)
            m.name = name
            m.rect.bottom = 0
            m.rect.x = random.randint(0, WIDTH - m.rect.width)
            if not pygame.sprite.spritecollideany(m, self.set_of_meteors):
                self.set_of_meteors.add(m)


# klasa meteor
class Meteor(pygame.sprite.Sprite):
    name_list = [name for name in IMAGES if 'METEOR' in name]

    def __init__(self, image, movement_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movement_y = movement_y
        self.name = None

    def update(self):
        self.rect.y += self.movement_y


class Text:
    def __init__(self, text, text_color, cx, cy, font_size=36, font_type=None):
        self.text = str(text)
        self.text_color = text_color
        self.font_size = font_size
        self.font_type = font_type
        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        self.cx = cx
        self.cy = cy
        self.update()

    def update(self):
        self.image = self.font.render(self.text, 1, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.cx, self.cy

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player(IMAGES['PLAYER'], WIDTH // 2, 650, [IMAGES[name] for name in IMAGES if 'FIRE' in name])
current_level = Level_1(player)
player.level = current_level
end_text = Text('KONIEC GRY', DARKRED, *screen.get_rect().center, font_size=128, font_type='Ink Free')

window_open = True
while window_open:
    screen.blit(BACKGROUND, (-300, -300))

    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        if event.type == pygame.QUIT:
            window_open = False

    # rysowanie i aktualizacja obiektów
    player.update(pygame.key.get_pressed())
    current_level.update()
    current_level.draw(screen)
    player.draw(screen)
    if player.lives <= 0:
        window_open = False

    # aktualizacja okna
    pygame.display.flip()
    clock.tick(60)

pygame.time.delay(500)
screen.fill(LIGHTBLUE)
end_text.draw(screen)
pygame.display.update()
pygame.time.delay(5000)
pygame.quit()
