import pygame
import random
pygame.init()
# WIDHT, HEIGHT = 800, 800
# screen = pygame.display.set_mode((WIDHT, HEIGHT))
# running = True
# RED = (255, 0, 0)
# x, y = 30, 30
# pygame.display.set_caption('Arnur practice')
# image = pygame.image.load('ball.png')
# clock = pygame.time.Clock()
# rect = image.get_rect()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_UP] and y - 30 > 0:
#         y -= 20
#     if pressed[pygame.K_DOWN] and y + 30 < HEIGHT:
#         y += 20
#     if pressed[pygame.K_LEFT] and x - 30 > 0:
#         x -= 20
#     if pressed[pygame.K_RIGHT] and x + 30 < WIDHT:
#         x += 20
#     screen.fill((255, 255, 255))
#     clock.tick(90)
#     pygame.draw.circle(screen, RED, (x, y), 25)
#     pygame.display.flip()
screen = pygame.display.set_mode((800,800))
SONG_END = pygame.USEREVENT +  1
playingnow = None
running = True
songs = ['герой.mp3','discordjoin.mp3', 'ястарался.mp3']
# def play_song():
#  global songs
#  songs = songs[1:] + [songs[0]]
#  pygame.mixer.music.load(songs[0])
#  pygame.mixer.music.play()
#  pygame.display.set_caption(songs[0])
# pygame.mixer.music.set_endevent(SONG_END)
i = 0
int(i)
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()
pygame.display.set_caption(songs[i])
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_RIGHT]:
   if i < 3:
    i += 1
   else :
    i = 0
   pygame.mixer.music.load(songs[i])
   pygame.display.set_caption(songs[i])
   pygame.mixer.music.play()
  elif pressed[pygame.K_LEFT]:
   if i > -3:
    i -= 1
   else:
    i = -1
   pygame.mixer.music.load(songs[i])
   pygame.display.set_caption(songs[i])
   pygame.mixer.music.play()
  elif pressed[pygame.K_UP]:
   pygame.mixer.music.play()
  elif pressed[pygame.K_DOWN]:
   pygame.mixer.music.stop()
 screen.fill((255,255,255))
 pygame.display.flip()