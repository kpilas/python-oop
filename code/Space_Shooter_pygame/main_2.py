import pygame, os, random

pygame.init()

SIZESCREEN = WIDTH, HEIGHT = 1366, 740
screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()
# wczytywanie grafik
# path = os.path.join(os.pardir, 'images')
path = os.path.join(os.getcwd(), 'images')
file_names = os.listdir(path)
BACKGROUND = pygame.image.load(os.path.join(path, 'background.jpg')).convert()
file_names.remove('background.jpg')
IMAGES = {}
for file_name in file_names:
    image_name = file_name[:-4].upper()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)


# klasa gracza
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.fire, [self.rect.centerx - self.fire.get_rect().width // 2,
                                 self.rect.centery + 40])

    def update(self, key_pressed):
        self.get_event(key_pressed)
        self._move(self.fire_list, 4)

        # blokujmy wyjście poza ekran gry
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > WIDTH:
            self.rect.centerx = WIDTH

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


player = Player(IMAGES['PLAYER'], 100, 100, [IMAGES[name] for name in IMAGES if 'FIRE' in name])

# główna pętla gry
window_open = True
while window_open:
    # screen.fill((123, 200, 120, 255))
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
    player.draw(screen)

    # aktualizacja okna
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
