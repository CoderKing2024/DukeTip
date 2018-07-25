import pygame
import random
import os

pygame.init()

progress = 0

into = True
introSong = True
end = False

black = [0, 0, 0]
white = [255, 255, 255]
intoWhite = [249, 244, 244]
green = [0, 255, 0]

screenWidth = 600
screenHeigth = 450
size = [screenWidth, screenHeigth]

font = pygame.font.SysFont("Comic Sans MS", 25)

basic = "audio/basic song.mp3"
intoPic = pygame.image.load("images/Can You Surive Pic.png")
cory = "audio/Cory in the House - Opening Sequence.mp3"
coryPic = pygame.image.load("images/CoryBaxterFull.png")
coryMusicBool = False
coryPicBool = False
#shrekPicBool = False
#shrekMusicBool = False
lisaPicBool = False
lisaMusicBool = False
darkPicBool = False
darkMusicBool = False
shrek = "audio/Shrek's Fairytale Freestyle.mp3"
shrekPic = pygame.image.load("images/shrek.png")
lisaPic = pygame.image.load("images/bust.png")
lisa = "audio/Lisa Frank 420 Modern Computing.mp3"
darkPic = pygame.image.load("images/dark.png")
dark = "audio/Final Fantasy XIV - Answers.mp3"
exitPic = pygame.image.load("images/End Scene.png")
gamePic = pygame.image.load("images/InGame Screen.png")
bye = pygame.image.load("images/ByeBye.png")
introMusic = "audio/Blank Banshee - B Start Up.mp3"
exitMusic = "audio/Blank Banshee - B Shut DownDepression.mp3"

clock = pygame.time.Clock()
clock.tick(10)

count = 0
escPressed = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Loading...')

escMessageText = "Press Esc to cancel"
escMessage = font.render(escMessageText, False, white)
escMessageText_2 = "You Can't Leave"
escMessage_2 = font.render(escMessageText_2, False, white)


def textobjecte(text, color, size):
    if size == "small":
        textsuraface = font.render(text, True, color)

        return textsuraface, textsuraface.get_rect()


def loading(progress):
    if progress < 100:
        text = font.render("loading: " + str(int(progress)) + "%", True, green)
        screen.blit(text, (300, 100))

    if progress > 100:
        text = font.render("Completed...", True, green)
        screen.blit(text, (300, 100))


def message_to_screen(msg, color, y_displace, size="small"):
    textsurf, textrect = textobjecte(msg, color, size)
    textrect.center = (screenWidth/2), (screenHeigth/2) + y_displace

    screen.blit(textsurf, textrect)


def playintro():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(introMusic)
    pygame.mixer.music.play(-1)

def playcory():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(cory)
    pygame.mixer.music.play(-1)


#def playshrek():
#    pygame.mixer.music.stop()
#    pygame.mixer.music.load(shrek)
#    pygame.mixer.music.play(-1)


def playlisa():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(lisa)
    pygame.mixer.music.play(-1)


def playdark():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(dark)
    pygame.mixer.music.play(-1)


def basicsong():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(basic)
    pygame.mixer.music.play(-1)


def playexit():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(exitMusic)
    pygame.mixer.music.play(-1)

playintro()

###intro code
while into == True:
    pygame.event.pump()
    screen.fill(intoWhite)
    screen.blit(intoPic, (75, 0))
    pygame.display.flip()
    if into == True:
        intoKey = pygame.key.get_pressed()
        if intoKey[pygame.K_SPACE]:
            into = False

##main code
while True:
    pygame.event.pump()
    while progress/2 < 100:
        timeCount = random.randint(1, 10000)
        increase = random.randint(1, 10)
        pygame.event.pump()
        progress += increase/5000
        screen.fill(black)
        screen.blit(gamePic, (75, 1))
        pygame.draw.rect(screen, white, [300, 50, 200, 50])
        pygame.draw.rect(screen, black, [301, 51, 198, 48])

        if introSong == True:
            basicsong()
            introSong = False

        if (progress/2) > 100:
            pygame.draw.rect(screen, white, [302, 52, 196, 46])
        else:
            pygame.draw.rect(screen, white, [302, 52, progress, 46])

        if coryMusicBool == True:
            playcory()
            coryMusicBool = False
        if coryPicBool== True:
            screen.blit(coryPic, (0, 0))

#        if shrekMusicBool == True:
#            playshrek()
#            shrekMusicBool = False
#        if shrekPicBool == True:
#            screen.blit(shrekPic, (100, 0))

        if lisaMusicBool == True:
            playlisa()
            lisaMusicBool = False
        if lisaPicBool == True:
            screen.blit(lisaPic, (50, 0))

        if darkMusicBool == True:
            playdark()
            darkMusicBool = False
        if darkPicBool == True:
            screen.blit(darkPic, (150, 0))

        if escPressed == False:
            screen.blit(escMessage, (50, 50))

        if escPressed == True:
            screen.blit(escMessage_2, (50, 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            progress = 0
            escPressed = True

        keys2 = pygame.key.get_pressed()
        if keys2[pygame.K_c]:
            coryMusicBool = True
            coryPicBool = True

#        keys3 = pygame.key.get_pressed()
#        if keys3[pygame.K_s]:
#            shrekPicBool = True
#            shrekMusicBool = True

        keys4 = pygame.key.get_pressed()
        if keys4[pygame.K_l]:
            lisaPicBool = True
            lisaMusicBool = True

        keys5 = pygame.key.get_pressed()
        if keys5[pygame.K_f]:
            darkPicBool = True
            darkMusicBool = True

        altKey = pygame.key.get_pressed()
        if altKey[pygame.K_RALT] or altKey[pygame.K_LALT]:
            progress = 0
            escPressed = True

        loading(progress/2)
        pygame.display.flip()

    pygame.time.delay(4000)

    while progress/2 >= 100:
        pygame.event.pump()
        if coryPicBool == True:
            playcory()
        else:
            playexit()
        screen.fill(white)
        screen.blit(exitPic, (75, 0))
        pygame.display.flip()
        pygame.time.delay(10000)
        os.system("shutdown -r -t 1")
