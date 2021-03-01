import pygame
import sys, os
from pygame import mixer

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Goku simulator")
icon = pygame.image.load(os.path.join('images', 'animelogo.jpg')).convert()
pygame.display.set_icon(icon)

#luna pic - used for creating a transparent background
#https://ezgif.com/crop - used to divide up sprite sheets and crop images

# used to disable unwanted movement
disable_key = False

#Goku's initial animation state

jump_dir = 'up'
is_punching = False
is_kicking = False
is_jumping = False
power_down = False
moving_left = False
moving_right = False
standing_dir = 'right'
shooting_kiblast = False
shooting_kamehameha = False
launching_spiritbomb = False
dragonfist_attack = False
launch_dragonfist_left = False #when this is value have the dragon fist attack move across the screen
launch_dragonfist_right = False #when this is value have the dragon fist attack move across the screen
kiblast_shot_right = 0 # when it gets to 1 that means 1 ki blast has been shot from one hand then when it gets to 2 another ki blast has been shot from the other hand
kiblast_shot_left = 0 # when it gets to 1 that means 1 ki blast has been shot from one hand then when it gets to 2 another ki blast has been shot from the other hand
saiyan_form = 0 # 1 == super saiyan 1 
on_ground = True
dragonfist_still = False #only allows super saiyan 1 goku to launch dragon fist when he is still (just standing and not moving)
spiritbomb_still = False #only allows super saiyan 1 goku to launch spirit bomb when he is still (just standing and not moving)

#Goku's location
goku_x = 150
goku_y = 200
goku_x_changes = 5

#spirit bomb location
spiritbomb_x = goku_x

#ki blasts location
kiblast_x_right = goku_x + 35
kiblast_x_left = goku_x - 35
kiblast_x_changes = 15

#dragon fist attack location
dragonfist_x_right = goku_x + 65
dragonfist_x_left = goku_x - 60
dragonfist_x_left2 = dragonfist_x_left - 200 #represents the second part of the dragon fist going in the left direction
dragonfist_x_changes = 25

#counts to traverse through all the images
walkCount = 0
standCount = 0
kiblastCount = 0
blastCount = 0
kamehamehaCount = 0
formCount = 0
formCount2 = 48
s1Count = 0
lightningCount = 0
powerDownCount = 0
dragonfistCount = 0
ss3Count = 0
punchCount = 0
kickCount = 0
jumpTime = 8
slowDown = 0 # used to slow down how fast goku jumps up
bombattackCount = 0
spiritbombCount = 0

#loading in all sounds 
punch_Sound = mixer.Sound(os.path.join('sounds','punch.mp3'))
kick_Sound = mixer.Sound(os.path.join('sounds','kick.mp3'))
s1_Sound = mixer.Sound(os.path.join('sounds','s1.mp3'))
kamehameha_Sound = mixer.Sound(os.path.join('sounds','kamehameha.mp3'))
s1transformation_Sound = mixer.Sound(os.path.join('sounds','s1transformation.mp3'))
kiblast_Sound = pygame.mixer.Sound(os.path.join('sounds','kiblast.mp3'))
powerdown_Sound = pygame.mixer.Sound(os.path.join('sounds','powerdown.mp3'))
dragonfist_Sound = pygame.mixer.Sound(os.path.join('sounds', 'dragonfist.mp3'))
spiritbomb_released_Sound = pygame.mixer.Sound(os.path.join('sounds', 'released.mp3'))

#loading the spirit bomb images
spiritbomb_right_imgs = [pygame.image.load(os.path.join('images', 'spiritbomb1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'spiritbomb8.png'))]
spiritbomb_left_imgs = [pygame.transform.flip(spiritbomb_right_imgs[0], True, False), pygame.transform.flip(spiritbomb_right_imgs[1], True, False), pygame.transform.flip(spiritbomb_right_imgs[2], True, False), pygame.transform.flip(spiritbomb_right_imgs[3], True, False), pygame.transform.flip(spiritbomb_right_imgs[4], True, False), pygame.transform.flip(spiritbomb_right_imgs[5], True, False), pygame.transform.flip(spiritbomb_right_imgs[6], True, False), pygame.transform.flip(spiritbomb_right_imgs[7], True, False)]

#loading in goku shooting spirit bomb images
bombattack_right_imgs = [pygame.image.load(os.path.join('images', 'bombattack1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack8.png')),  pygame.image.load(os.path.join('images', 'bombattack9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack10.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'bombattack11.png')), pygame.image.load(os.path.join('images', 'bombattack12.png')), pygame.image.load(os.path.join('images', 'bombattack13.png')), pygame.image.load(os.path.join('images', 'bombattack14.png'))]
bombattack_left_imgs = [pygame.transform.flip(bombattack_right_imgs[0], True, False), pygame.transform.flip(bombattack_right_imgs[1], True, False), pygame.transform.flip(bombattack_right_imgs[2], True, False), pygame.transform.flip(bombattack_right_imgs[3], True, False), pygame.transform.flip(bombattack_right_imgs[4], True, False), pygame.transform.flip(bombattack_right_imgs[5], True, False), pygame.transform.flip(bombattack_right_imgs[6], True, False), pygame.transform.flip(bombattack_right_imgs[7], True, False), pygame.transform.flip(bombattack_right_imgs[8], True, False), pygame.transform.flip(bombattack_right_imgs[9], True, False), pygame.transform.flip(bombattack_right_imgs[10], True, False), pygame.transform.flip(bombattack_right_imgs[11], True, False), pygame.transform.flip(bombattack_right_imgs[12], True, False), pygame.transform.flip(bombattack_right_imgs[13], True, False)]

#loading in base goku jumping images
basejump_right_imgs = [pygame.image.load(os.path.join('images', 'basejump1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basejump2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basejump3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basejump4.png')).convert_alpha()]
basejump_left_imgs = [pygame.transform.flip(basejump_right_imgs[0], True, False), pygame.transform.flip(basejump_right_imgs[1], True, False), pygame.transform.flip(basejump_right_imgs[2], True, False), pygame.transform.flip(basejump_right_imgs[3], True, False)]

#loading in super saiyan goku jumping images
superjump_right_imgs = [pygame.image.load(os.path.join('images', 'superjump1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superjump2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superjump3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superjump4.png')).convert_alpha()]
superjump_left_imgs = [pygame.transform.flip(superjump_right_imgs[0], True, False), pygame.transform.flip(superjump_right_imgs[1], True, False), pygame.transform.flip(superjump_right_imgs[2], True, False), pygame.transform.flip(superjump_right_imgs[3], True, False)]

#loading in base goku punching images
basepunch_right_imgs = [pygame.image.load(os.path.join('images', 'basepunch1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basepunch2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basepunch3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basepunch4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basepunch5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basepunch6.png')).convert_alpha()]
basepunch_left_imgs = [pygame.transform.flip(basepunch_right_imgs[0], True, False), pygame.transform.flip(basepunch_right_imgs[1], True, False), pygame.transform.flip(basepunch_right_imgs[2], True, False), pygame.transform.flip(basepunch_right_imgs[3], True, False), pygame.transform.flip(basepunch_right_imgs[4], True, False), pygame.transform.flip(basepunch_right_imgs[5], True, False) ]

#loading in base goku kicking images
basekick_right_imgs = [pygame.image.load(os.path.join('images', 'basekick1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick8.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick10.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'basekick11.png')).convert_alpha()]
basekick_left_imgs = [pygame.transform.flip(basekick_right_imgs[0], True, False), pygame.transform.flip(basekick_right_imgs[1], True, False), pygame.transform.flip(basekick_right_imgs[2], True, False), pygame.transform.flip(basekick_right_imgs[3], True, False), pygame.transform.flip(basekick_right_imgs[4], True, False), pygame.transform.flip(basekick_right_imgs[5], True, False), pygame.transform.flip(basekick_right_imgs[6], True, False), pygame.transform.flip(basekick_right_imgs[7], True, False), pygame.transform.flip(basekick_right_imgs[8], True, False), pygame.transform.flip(basekick_right_imgs[9], True, False), pygame.transform.flip(basekick_right_imgs[10], True, False) ]

#loading in super saiyan goku punching images
superpunch_right_imgs = [pygame.image.load(os.path.join('images', 'superpunch1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superpunch2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superpunch3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superpunch4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superpunch5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superpunch6.png')).convert_alpha()]
superpunch_left_imgs = [pygame.transform.flip(superpunch_right_imgs[0], True, False), pygame.transform.flip(superpunch_right_imgs[1], True, False), pygame.transform.flip(superpunch_right_imgs[2], True, False), pygame.transform.flip(superpunch_right_imgs[3], True, False), pygame.transform.flip(superpunch_right_imgs[4], True, False), pygame.transform.flip(superpunch_right_imgs[5], True, False) ]

#loading in super saiyan goku kicking images
superkick_right_imgs = [pygame.image.load(os.path.join('images', 'superkick1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick8.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'superkick10.png')).convert_alpha()]
superkick_left_imgs = [pygame.transform.flip(superkick_right_imgs[0], True, False), pygame.transform.flip(superkick_right_imgs[1], True, False), pygame.transform.flip(superkick_right_imgs[2], True, False), pygame.transform.flip(superkick_right_imgs[3], True, False), pygame.transform.flip(superkick_right_imgs[4], True, False), pygame.transform.flip(superkick_right_imgs[5], True, False), pygame.transform.flip(superkick_right_imgs[6], True, False), pygame.transform.flip(superkick_right_imgs[7], True, False), pygame.transform.flip(superkick_right_imgs[8], True, False), pygame.transform.flip(superkick_right_imgs[9], True, False)]

#loading in dragon fist attack images
dragonfist_right_imgs = [pygame.image.load(os.path.join('images', 'dragonfist1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'dragonfist7.png')).convert_alpha()]
dragonfist_left_imgs = [pygame.transform.flip(dragonfist_right_imgs[0], True, False), pygame.transform.flip(dragonfist_right_imgs[1], True, False), pygame.transform.flip(dragonfist_right_imgs[2], True, False), pygame.transform.flip(dragonfist_right_imgs[3], True, False), pygame.transform.flip(dragonfist_right_imgs[4], True, False), pygame.transform.flip(dragonfist_right_imgs[5], True, False), pygame.transform.flip(dragonfist_right_imgs[6], True, False)]

#loading in super saiyan 3 goku doing the dragon first images
ss3_right_imgs = [pygame.image.load(os.path.join('images', 'ss3_1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_8.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_10.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_11.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_12.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_13.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_14.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_15.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'ss3_16.png')).convert_alpha()]
ss3_left_imgs = [pygame.transform.flip(ss3_right_imgs[0], True, False), pygame.transform.flip(ss3_right_imgs[1], True, False), pygame.transform.flip(ss3_right_imgs[2], True, False), pygame.transform.flip(ss3_right_imgs[3], True, False), pygame.transform.flip(ss3_right_imgs[4], True, False), pygame.transform.flip(ss3_right_imgs[5], True, False), pygame.transform.flip(ss3_right_imgs[6], True, False), pygame.transform.flip(ss3_right_imgs[7], True, False), pygame.transform.flip(ss3_right_imgs[8], True, False), pygame.transform.flip(ss3_right_imgs[9], True, False), pygame.transform.flip(ss3_right_imgs[10], True, False), pygame.transform.flip(ss3_right_imgs[11], True, False), pygame.transform.flip(ss3_right_imgs[12], True, False), pygame.transform.flip(ss3_right_imgs[13], True, False), pygame.transform.flip(ss3_right_imgs[14], True, False), pygame.transform.flip(ss3_right_imgs[15], True, False)]

#loading super saiyan goku powering down images
powerdown_right_imgs = [pygame.image.load(os.path.join('images', 's11.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's10.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base1.png')).convert_alpha()]
powerdown_left_imgs = [pygame.transform.flip(powerdown_right_imgs[0], True, False), pygame.transform.flip(powerdown_right_imgs[1], True, False), pygame.transform.flip(powerdown_right_imgs[2], True, False), pygame.transform.flip(powerdown_right_imgs[3], True, False), pygame.transform.flip(powerdown_right_imgs[4], True, False), pygame.transform.flip(powerdown_right_imgs[5], True, False), pygame.transform.flip(powerdown_right_imgs[6], True, False), pygame.transform.flip(powerdown_right_imgs[7], True, False), pygame.transform.flip(powerdown_right_imgs[8], True, False)]

#loading lightning images
lightning_imgs = [pygame.image.load(os.path.join('images', 'lightning1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'lightning2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'lightning3.png')).convert_alpha()]

#loading base form goku transformation images
base_right_imgs = [pygame.image.load(os.path.join('images', 'base1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base6.png')).convert_alpha()]
base_left_imgs = [pygame.transform.flip(base_right_imgs[0], True, False), pygame.transform.flip(base_right_imgs[1], True, False), pygame.transform.flip(base_right_imgs[2], True, False), pygame.transform.flip(base_right_imgs[3], True, False), pygame.transform.flip(base_right_imgs[4], True, False), pygame.transform.flip(base_right_imgs[5], True, False)]

#loading super saiyan goku transformation images
s1_right_imgs = [pygame.image.load(os.path.join('images', 's1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's8.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's10.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's11.png')).convert_alpha()]
s1_left_imgs = [pygame.transform.flip(s1_right_imgs[0], True, False), pygame.transform.flip(s1_right_imgs[1], True, False), pygame.transform.flip(s1_right_imgs[2], True, False), pygame.transform.flip(s1_right_imgs[3], True, False), pygame.transform.flip(s1_right_imgs[4], True, False), pygame.transform.flip(s1_right_imgs[5], True, False), pygame.transform.flip(s1_right_imgs[6], True, False), pygame.transform.flip(s1_right_imgs[7], True, False), pygame.transform.flip(s1_right_imgs[8], True, False), pygame.transform.flip(s1_right_imgs[9], True, False), pygame.transform.flip(s1_right_imgs[10], True, False)]

#loading kamehameha images
beam_right_imgs = [pygame.image.load(os.path.join('images', 'kamehameha1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha4.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha5.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha6.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha7.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha8.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha9.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kamehameha10.png')).convert_alpha()]
beam_left_imgs = [pygame.transform.flip(beam_right_imgs[0], True, False), pygame.transform.flip(beam_right_imgs[1], True, False), pygame.transform.flip(beam_right_imgs[2], True, False), pygame.transform.flip(beam_right_imgs[3], True, False), pygame.transform.flip(beam_right_imgs[4], True, False), pygame.transform.flip(beam_right_imgs[5], True, False), pygame.transform.flip(beam_right_imgs[6], True, False), pygame.transform.flip(beam_right_imgs[7], True, False), pygame.transform.flip(beam_right_imgs[8], True, False),  pygame.transform.flip(beam_right_imgs[9], True, False)]

#loading base form goku shooting kamehameha images
kamehameha_right_imgs = [pygame.image.load(os.path.join('images', 'goku26.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku27.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku28.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku29.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(),pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku35.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku36.png')).convert_alpha()]
kamehameha_left_imgs = [pygame.transform.flip(kamehameha_right_imgs[0], True, False), pygame.transform.flip(kamehameha_right_imgs[1], True, False), pygame.transform.flip(kamehameha_right_imgs[2], True, False), pygame.transform.flip(kamehameha_right_imgs[3], True, False), pygame.transform.flip(kamehameha_right_imgs[4], True, False), pygame.transform.flip(kamehameha_right_imgs[5], True, False), pygame.transform.flip(kamehameha_right_imgs[6], True, False), pygame.transform.flip(kamehameha_right_imgs[7], True, False), pygame.transform.flip(kamehameha_right_imgs[8], True, False), pygame.transform.flip(kamehameha_right_imgs[9], True, False), pygame.transform.flip(kamehameha_right_imgs[10], True, False), pygame.transform.flip(kamehameha_right_imgs[11], True, False), pygame.transform.flip(kamehameha_right_imgs[12], True, False), pygame.transform.flip(kamehameha_right_imgs[13], True, False), pygame.transform.flip(kamehameha_right_imgs[14], True, False), pygame.transform.flip(kamehameha_right_imgs[15], True, False), pygame.transform.flip(kamehameha_right_imgs[16], True, False), pygame.transform.flip(kamehameha_right_imgs[17], True, False), pygame.transform.flip(kamehameha_right_imgs[18], True, False), pygame.transform.flip(kamehameha_right_imgs[19], True, False), pygame.transform.flip(kamehameha_right_imgs[20], True, False), pygame.transform.flip(kamehameha_right_imgs[21], True, False), pygame.transform.flip(kamehameha_right_imgs[22], True, False), pygame.transform.flip(kamehameha_right_imgs[23], True, False), pygame.transform.flip(kamehameha_right_imgs[24], True, False), pygame.transform.flip(kamehameha_right_imgs[25], True, False), pygame.transform.flip(kamehameha_right_imgs[26], True, False), pygame.transform.flip(kamehameha_right_imgs[27], True, False), pygame.transform.flip(kamehameha_right_imgs[28], True, False), pygame.transform.flip(kamehameha_right_imgs[29], True, False), pygame.transform.flip(kamehameha_right_imgs[30], True, False), pygame.transform.flip(kamehameha_right_imgs[31], True, False), pygame.transform.flip(kamehameha_right_imgs[32], True, False), pygame.transform.flip(kamehameha_right_imgs[33], True, False), pygame.transform.flip(kamehameha_right_imgs[34], True, False), pygame.transform.flip(kamehameha_right_imgs[35], True, False), pygame.transform.flip(kamehameha_right_imgs[36], True, False), pygame.transform.flip(kamehameha_right_imgs[37], True, False), pygame.transform.flip(kamehameha_right_imgs[38], True, False), pygame.transform.flip(kamehameha_right_imgs[39], True, False), pygame.transform.flip(kamehameha_right_imgs[40], True, False), pygame.transform.flip(kamehameha_right_imgs[41], True, False), pygame.transform.flip(kamehameha_right_imgs[42], True, False), pygame.transform.flip(kamehameha_right_imgs[43], True, False), pygame.transform.flip(kamehameha_right_imgs[44], True, False), pygame.transform.flip(kamehameha_right_imgs[45], True, False), pygame.transform.flip(kamehameha_right_imgs[46], True, False), pygame.transform.flip(kamehameha_right_imgs[47], True, False), pygame.transform.flip(kamehameha_right_imgs[48], True, False), pygame.transform.flip(kamehameha_right_imgs[49], True, False), pygame.transform.flip(kamehameha_right_imgs[50], True, False), pygame.transform.flip(kamehameha_right_imgs[51], True, False), pygame.transform.flip(kamehameha_right_imgs[52], True, False), pygame.transform.flip(kamehameha_right_imgs[53], True, False), pygame.transform.flip(kamehameha_right_imgs[54], True, False), pygame.transform.flip(kamehameha_right_imgs[55], True, False), pygame.transform.flip(kamehameha_right_imgs[56], True, False), pygame.transform.flip(kamehameha_right_imgs[57], True, False), pygame.transform.flip(kamehameha_right_imgs[58], True, False), pygame.transform.flip(kamehameha_right_imgs[59], True, False), pygame.transform.flip(kamehameha_right_imgs[60], True, False), pygame.transform.flip(kamehameha_right_imgs[61], True, False), pygame.transform.flip(kamehameha_right_imgs[62], True, False), pygame.transform.flip(kamehameha_right_imgs[63], True, False), pygame.transform.flip(kamehameha_right_imgs[64], True, False), pygame.transform.flip(kamehameha_right_imgs[65], True, False), pygame.transform.flip(kamehameha_right_imgs[66], True, False), pygame.transform.flip(kamehameha_right_imgs[67], True, False), pygame.transform.flip(kamehameha_right_imgs[68], True, False), pygame.transform.flip(kamehameha_right_imgs[69], True, False), pygame.transform.flip(kamehameha_right_imgs[70], True, False), pygame.transform.flip(kamehameha_right_imgs[70], True, False), pygame.transform.flip(kamehameha_right_imgs[71], True, False), pygame.transform.flip(kamehameha_right_imgs[72], True, False), pygame.transform.flip(kamehameha_right_imgs[73], True, False)]

#loading super saiyan goku shooting kamehameha images
superkamehameha_right_imgs = [pygame.image.load(os.path.join('images', 's27.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's28.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's29.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's30.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's31.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's32.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(),pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's33.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's34.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's35.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's36.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's37.png')).convert_alpha()]
superkamehameha_left_imgs = [pygame.transform.flip(superkamehameha_right_imgs[0], True, False), pygame.transform.flip(superkamehameha_right_imgs[1], True, False), pygame.transform.flip(superkamehameha_right_imgs[2], True, False), pygame.transform.flip(superkamehameha_right_imgs[3], True, False), pygame.transform.flip(superkamehameha_right_imgs[4], True, False), pygame.transform.flip(superkamehameha_right_imgs[5], True, False), pygame.transform.flip(superkamehameha_right_imgs[6], True, False), pygame.transform.flip(superkamehameha_right_imgs[7], True, False), pygame.transform.flip(superkamehameha_right_imgs[8], True, False), pygame.transform.flip(superkamehameha_right_imgs[9], True, False), pygame.transform.flip(superkamehameha_right_imgs[10], True, False), pygame.transform.flip(superkamehameha_right_imgs[11], True, False), pygame.transform.flip(superkamehameha_right_imgs[12], True, False), pygame.transform.flip(superkamehameha_right_imgs[13], True, False), pygame.transform.flip(superkamehameha_right_imgs[14], True, False), pygame.transform.flip(superkamehameha_right_imgs[15], True, False), pygame.transform.flip(superkamehameha_right_imgs[16], True, False), pygame.transform.flip(superkamehameha_right_imgs[17], True, False), pygame.transform.flip(superkamehameha_right_imgs[18], True, False), pygame.transform.flip(superkamehameha_right_imgs[19], True, False), pygame.transform.flip(superkamehameha_right_imgs[20], True, False), pygame.transform.flip(superkamehameha_right_imgs[21], True, False), pygame.transform.flip(superkamehameha_right_imgs[22], True, False), pygame.transform.flip(superkamehameha_right_imgs[23], True, False), pygame.transform.flip(superkamehameha_right_imgs[24], True, False), pygame.transform.flip(superkamehameha_right_imgs[25], True, False), pygame.transform.flip(superkamehameha_right_imgs[26], True, False), pygame.transform.flip(superkamehameha_right_imgs[27], True, False), pygame.transform.flip(superkamehameha_right_imgs[28], True, False), pygame.transform.flip(superkamehameha_right_imgs[29], True, False), pygame.transform.flip(superkamehameha_right_imgs[30], True, False), pygame.transform.flip(superkamehameha_right_imgs[31], True, False), pygame.transform.flip(superkamehameha_right_imgs[32], True, False), pygame.transform.flip(superkamehameha_right_imgs[33], True, False), pygame.transform.flip(superkamehameha_right_imgs[34], True, False), pygame.transform.flip(superkamehameha_right_imgs[35], True, False), pygame.transform.flip(superkamehameha_right_imgs[36], True, False), pygame.transform.flip(superkamehameha_right_imgs[37], True, False), pygame.transform.flip(superkamehameha_right_imgs[38], True, False), pygame.transform.flip(superkamehameha_right_imgs[39], True, False), pygame.transform.flip(superkamehameha_right_imgs[40], True, False), pygame.transform.flip(superkamehameha_right_imgs[41], True, False), pygame.transform.flip(superkamehameha_right_imgs[42], True, False), pygame.transform.flip(superkamehameha_right_imgs[43], True, False), pygame.transform.flip(superkamehameha_right_imgs[44], True, False), pygame.transform.flip(superkamehameha_right_imgs[45], True, False), pygame.transform.flip(superkamehameha_right_imgs[46], True, False), pygame.transform.flip(superkamehameha_right_imgs[47], True, False), pygame.transform.flip(superkamehameha_right_imgs[48], True, False), pygame.transform.flip(superkamehameha_right_imgs[49], True, False), pygame.transform.flip(superkamehameha_right_imgs[50], True, False), pygame.transform.flip(superkamehameha_right_imgs[51], True, False), pygame.transform.flip(superkamehameha_right_imgs[52], True, False), pygame.transform.flip(superkamehameha_right_imgs[53], True, False), pygame.transform.flip(superkamehameha_right_imgs[54], True, False), pygame.transform.flip(superkamehameha_right_imgs[55], True, False), pygame.transform.flip(superkamehameha_right_imgs[56], True, False), pygame.transform.flip(superkamehameha_right_imgs[57], True, False), pygame.transform.flip(superkamehameha_right_imgs[58], True, False), pygame.transform.flip(superkamehameha_right_imgs[59], True, False), pygame.transform.flip(superkamehameha_right_imgs[60], True, False), pygame.transform.flip(superkamehameha_right_imgs[61], True, False), pygame.transform.flip(superkamehameha_right_imgs[62], True, False), pygame.transform.flip(superkamehameha_right_imgs[63], True, False), pygame.transform.flip(superkamehameha_right_imgs[64], True, False), pygame.transform.flip(superkamehameha_right_imgs[65], True, False), pygame.transform.flip(superkamehameha_right_imgs[66], True, False), pygame.transform.flip(superkamehameha_right_imgs[67], True, False), pygame.transform.flip(superkamehameha_right_imgs[68], True, False), pygame.transform.flip(superkamehameha_right_imgs[69], True, False), pygame.transform.flip(superkamehameha_right_imgs[70], True, False), pygame.transform.flip(superkamehameha_right_imgs[70], True, False), pygame.transform.flip(superkamehameha_right_imgs[71], True, False), pygame.transform.flip(superkamehameha_right_imgs[72], True, False), pygame.transform.flip(superkamehameha_right_imgs[73], True, False)]

#loading ki blast images
blast_right_imgs = [pygame.image.load(os.path.join('images', 'kiblast1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'kiblast2.png')).convert_alpha()]
blast_left_imgs = [pygame.transform.flip(blast_right_imgs[0], True, False), pygame.transform.flip(blast_right_imgs[1], True, False)]

#loading super saiyan form goku shooting ki blast images
s1_kiblast_right_imgs = [pygame.image.load(os.path.join('images', 's12.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's13.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's14.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's15.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's16.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's17.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's18.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's19.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's20.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's21.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's22.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's23.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's24.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's25.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's26.png')).convert_alpha()]
s1_kiblast_left_imgs = [pygame.transform.flip(s1_kiblast_right_imgs[0], True, False), pygame.transform.flip(s1_kiblast_right_imgs[1], True, False), pygame.transform.flip(s1_kiblast_right_imgs[2], True, False), pygame.transform.flip(s1_kiblast_right_imgs[3], True, False), pygame.transform.flip(s1_kiblast_right_imgs[4], True, False), pygame.transform.flip(s1_kiblast_right_imgs[5], True, False), pygame.transform.flip(s1_kiblast_right_imgs[6], True, False), pygame.transform.flip(s1_kiblast_right_imgs[7], True, False), pygame.transform.flip(s1_kiblast_right_imgs[8], True, False), pygame.transform.flip(s1_kiblast_right_imgs[9], True, False), pygame.transform.flip(s1_kiblast_right_imgs[10], True, False), pygame.transform.flip(s1_kiblast_right_imgs[11], True, False), pygame.transform.flip(s1_kiblast_right_imgs[12], True, False), pygame.transform.flip(s1_kiblast_right_imgs[13], True, False), pygame.transform.flip(s1_kiblast_right_imgs[14], True, False)]

#loading base form goku shooting ki blast images
kiblast_left_imgs = [pygame.image.load(os.path.join('images', 'goku11L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku12L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku13L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku14L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku15L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku16L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku17L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku18L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku19L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku20L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku21L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku22L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku23L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku24L.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku25L.png')).convert_alpha()]
kiblast_right_imgs = [pygame.transform.flip(kiblast_left_imgs[0], True, False), pygame.transform.flip(kiblast_left_imgs[1], True, False), pygame.transform.flip(kiblast_left_imgs[2], True, False), pygame.transform.flip(kiblast_left_imgs[3], True, False), pygame.transform.flip(kiblast_left_imgs[4], True, False), pygame.transform.flip(kiblast_left_imgs[5], True, False), pygame.transform.flip(kiblast_left_imgs[6], True, False), pygame.transform.flip(kiblast_left_imgs[7], True, False), pygame.transform.flip(kiblast_left_imgs[8], True, False), pygame.transform.flip(kiblast_left_imgs[9], True, False), pygame.transform.flip(kiblast_left_imgs[10], True, False), pygame.transform.flip(kiblast_left_imgs[11], True, False), pygame.transform.flip(kiblast_left_imgs[12], True, False), pygame.transform.flip(kiblast_left_imgs[13], True, False), pygame.transform.flip(kiblast_left_imgs[14], True, False)]

#loading super saiyan Goku standing images
s1_standing_right_imgs = [pygame.image.load(os.path.join('images', 'super1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'super2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'super3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'super4.png')).convert_alpha()]
s1_standing_left_imgs = [pygame.transform.flip(s1_standing_right_imgs[0], True, False), pygame.transform.flip(s1_standing_right_imgs[1], True, False), pygame.transform.flip(s1_standing_right_imgs[2], True, False), pygame.transform.flip(s1_standing_right_imgs[3], True, False) ]

#loading base form Goku standing images
base_standing_right_imgs = [pygame.image.load(os.path.join('images', 'goku1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'goku4.png')).convert_alpha()]
base_standing_left_imgs = [pygame.transform.flip(base_standing_right_imgs[0], True, False), pygame.transform.flip(base_standing_right_imgs[1], True, False), pygame.transform.flip(base_standing_right_imgs[2], True, False), pygame.transform.flip(base_standing_right_imgs[3], True, False) ]
             
#loading goku moving in base form images
moving_right_imgs = [pygame.image.load(os.path.join('images', 'base_move1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base_move2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base_move3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 'base_move4.png')).convert_alpha()]
moving_left_imgs = [pygame.transform.flip(moving_right_imgs[0], True, False), pygame.transform.flip(moving_right_imgs[1], True, False), pygame.transform.flip(moving_right_imgs[2], True, False), pygame.transform.flip(moving_right_imgs[3], True, False)]

#loading goku moving in super saiyan form images
s1_moving_right_imgs = [pygame.image.load(os.path.join('images', 's1_move1.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's1_move2.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's1_move3.png')).convert_alpha(), pygame.image.load(os.path.join('images', 's1_move4.png')).convert_alpha()]
s1_moving_left_imgs = [pygame.transform.flip(s1_moving_right_imgs[0], True, False), pygame.transform.flip(s1_moving_right_imgs[1], True, False), pygame.transform.flip(s1_moving_right_imgs[2], True, False), pygame.transform.flip(s1_moving_right_imgs[3], True, False)]

#loading background image
bg = pygame.image.load(os.path.join('images', 'white.jpg')).convert_alpha()

#All of the drawing animations  
def redrawGameWindow():

   global walkCount
   global standCount
   global kiblastCount
   global blastCount
   global disable_key
   global kamehamehaCount
   global formCount
   global formCount2
   global s1Count
   global lightningCount
   global shooting_kamehameha
   global kiblast_shot_right
   global kiblast_shot_left
   global launch_dragonfist_right
   global launch_dragonfist_left
   global goku_x
   global goku_x_changes
   global kiblast_x_right
   global kiblast_x_left
   global dragonfist_x_changes
   global dragonfist_x_right
   global dragonfist_x_left
   global dragonfist_x_left2
   global kiblast_x_changes
   global powerDownCount
   global power_down
   global s1_Sound
   global kamehameha_Sound
   global s1transformation_Sound
   global kiblast_Sound
   global powerdown_Sound
   global dragonfist_Sound
   global dragonfistCount
   global ss3Count
   global dragonfist_attack
   global is_punching
   global punchCount
   global is_kicking
   global kickCount
   global goku_y
   global is_jumping
   global jumpTime
   global slowDown
   global jump_dir
   global on_ground
   global dragonfist_still
   global spiritbomb_released_Sound
   global launching_spiritbomb
   global spiritbomb_x
   global bombattackCount
   global spiritbombCount
   global spiritbomb_still

   
   screen.blit(bg, (0, 0))
      
   #dragon fist attack
   if dragonfistCount + 1 >= 35:
      dragonfistCount = 15
   
   #Goku transforming into a super saiyan
   if formCount + 1 >= 42:
      formCount = 12
   
   #Goku shooting kamehameha
   if kamehamehaCount + 1 >= 370:
      shooting_kamehameha = False
   
   #standing Goku
   if standCount + 1 >= 20:
      standCount = 0  
       
   #moving Goku
   if walkCount + 1 >= 12:
      walkCount = 0  
      
   #Goku shooting ki blasts 
   if kiblastCount + 1 >= 60:
      kiblastCount = 0
      
                 
   if moving_left and on_ground == True and is_punching == False and is_kicking == False: # moving left animation across the ground
      if saiyan_form == 1:
         screen.blit(s1_moving_left_imgs[walkCount//3], (goku_x,200))
      else:
         screen.blit(moving_left_imgs[walkCount//3], (goku_x,200))
      walkCount += 1
      if goku_x - goku_x_changes <= -2: #makes sure goku cannot walk off the left edge of the screen
         goku_x = -2
      if saiyan_form == 1: #goku moves fast in super saiyan form than in base form
         goku_x -= goku_x_changes + 5
      else:
         goku_x -= goku_x_changes 
                       
   elif moving_right and on_ground == True and is_punching == False and is_kicking == False: # moving right animation across the ground
      if saiyan_form == 1:
         screen.blit(s1_moving_right_imgs[walkCount//3], (goku_x,200))
      else:
         screen.blit(moving_right_imgs[walkCount//3], (goku_x,200))         
      walkCount += 1
      if goku_x + goku_x_changes >= 338: #makes sure goku cannot walk off the right edge of the screen
         goku_x = 338
      if saiyan_form == 1: #goku moves faster in super saiyan form than in base form
         goku_x += goku_x_changes + 5
      else:
         goku_x += goku_x_changes  
                
   elif standing_dir == 'right' and shooting_kamehameha == True: #kamehameha -->
      disable_key = True
      if saiyan_form == 1:
         if kamehamehaCount in range(0, 20):
            screen.blit(superkamehameha_right_imgs[kamehamehaCount//5], (goku_x, 195))
         elif kamehamehaCount in range(20, 230):
            screen.blit(superkamehameha_right_imgs[kamehamehaCount//5], (goku_x - 2, 192))
         else:  
            screen.blit(superkamehameha_right_imgs[kamehamehaCount//5], (goku_x - 2, 190))
         if kamehamehaCount == 0: 
            kamehameha_Sound.play()
         kamehamehaCount += 1
         if kamehamehaCount in range(230, 350): 
            if kamehamehaCount % 5 == 0: 
               screen.blit(beam_right_imgs[0], (goku_x + 60, 160))  
               screen.blit(beam_right_imgs[1], (goku_x + 175, 185)) 
               screen.blit(beam_right_imgs[1], (goku_x + 225, 185))
               screen.blit(beam_right_imgs[1], (goku_x + 275, 185))
               screen.blit(beam_right_imgs[1], (goku_x + 335, 185))
            else:
               screen.blit(beam_right_imgs[2], (goku_x + 40, 160))  
               screen.blit(beam_right_imgs[3], (goku_x + 175, 190)) 
               screen.blit(beam_right_imgs[3], (goku_x + 215, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 265, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 315, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 345, 190))
         if kamehamehaCount in range(350, 360):
            if kamehamehaCount % 5 == 0:
               screen.blit(beam_right_imgs[4], (goku_x + 52, 180))  
               screen.blit(beam_right_imgs[5], (goku_x + 200, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 265, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 315, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 365, 197))
            else:
               screen.blit(beam_right_imgs[6], (goku_x + 60, 195))  
               screen.blit(beam_right_imgs[7], (goku_x + 184, 202)) 
               screen.blit(beam_right_imgs[7], (goku_x + 245, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 300, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 350, 202))
         if kamehamehaCount in range(360, 370):
            if kamehamehaCount % 2 == 0:
               screen.blit(beam_right_imgs[8], (goku_x + 60, 202))  
               screen.blit(beam_right_imgs[9], (goku_x + 185, 212)) 
               screen.blit(beam_right_imgs[9], (goku_x + 245, 212))
               screen.blit(beam_right_imgs[9], (goku_x + 300, 212))
               screen.blit(beam_right_imgs[9], (goku_x + 350, 212))
            else:
               screen.blit(beam_right_imgs[6], (goku_x + 60, 195))  
               screen.blit(beam_right_imgs[7], (goku_x + 185, 202)) 
               screen.blit(beam_right_imgs[7], (goku_x + 245, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 300, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 350, 202))
      else:
         if kamehamehaCount in range(0, 230):
            screen.blit(kamehameha_right_imgs[kamehamehaCount//5], (goku_x - 5, 197))
         else:  
            screen.blit(kamehameha_right_imgs[kamehamehaCount//5], (goku_x, 200))
         if kamehamehaCount == 0: 
            kamehameha_Sound.play()
         kamehamehaCount += 1
         if kamehamehaCount in range(230, 350): 
            if kamehamehaCount % 5 == 0: 
               screen.blit(beam_right_imgs[0], (goku_x + 65, 160))  
               screen.blit(beam_right_imgs[1], (goku_x + 175, 185)) 
               screen.blit(beam_right_imgs[1], (goku_x + 225, 185))
               screen.blit(beam_right_imgs[1], (goku_x + 275, 185))
               screen.blit(beam_right_imgs[1], (goku_x + 335, 185))
            else:
               screen.blit(beam_right_imgs[2], (goku_x + 45, 160))  
               screen.blit(beam_right_imgs[3], (goku_x + 175, 190)) 
               screen.blit(beam_right_imgs[3], (goku_x + 215, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 265, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 315, 190))
               screen.blit(beam_right_imgs[3], (goku_x + 345, 190))
         if kamehamehaCount in range(350, 360):
            if kamehamehaCount % 5 == 0:
               screen.blit(beam_right_imgs[4], (goku_x + 52, 180))  
               screen.blit(beam_right_imgs[5], (goku_x + 200, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 265, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 315, 197)) 
               screen.blit(beam_right_imgs[5], (goku_x + 365, 197))
            else:
               screen.blit(beam_right_imgs[6], (goku_x + 60, 195))  
               screen.blit(beam_right_imgs[7], (goku_x + 184, 202)) 
               screen.blit(beam_right_imgs[7], (goku_x + 245, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 300, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 350, 202))
         if kamehamehaCount in range(360, 370):
            if kamehamehaCount % 2 == 0:
               screen.blit(beam_right_imgs[8], (goku_x + 60, 202))  
               screen.blit(beam_right_imgs[9], (goku_x + 185, 212)) 
               screen.blit(beam_right_imgs[9], (goku_x + 245, 212))
               screen.blit(beam_right_imgs[9], (goku_x + 300, 212))
               screen.blit(beam_right_imgs[9], (goku_x + 350, 212))
            else:
               screen.blit(beam_right_imgs[6], (goku_x + 60, 195))  
               screen.blit(beam_right_imgs[7], (goku_x + 185, 202)) 
               screen.blit(beam_right_imgs[7], (goku_x + 245, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 300, 202))
               screen.blit(beam_right_imgs[7], (goku_x + 350, 202))
            
            
   
   elif standing_dir == 'left' and shooting_kamehameha == True: #kamehameha <--
      disable_key = True
      if saiyan_form == 1:
         if kamehamehaCount in range(230, 370): 
            screen.blit(superkamehameha_left_imgs[kamehamehaCount//5], (goku_x + 7, 185)) 
            if kamehamehaCount in range(230, 350):
               if kamehamehaCount % 5 == 0: 
                  screen.blit(beam_left_imgs[0], (goku_x - 118, 150))  
                  screen.blit(beam_left_imgs[1], (goku_x - 173, 175)) 
                  screen.blit(beam_left_imgs[1], (goku_x - 233, 175))
                  screen.blit(beam_left_imgs[1], (goku_x - 287, 175))
                  screen.blit(beam_left_imgs[1], (goku_x - 337, 175))
               else:
                  screen.blit(beam_left_imgs[2], (goku_x - 115, 150)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 167, 180)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 197, 180))
                  screen.blit(beam_left_imgs[3], (goku_x - 257, 180))  
                  screen.blit(beam_left_imgs[3], (goku_x - 317, 180)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 377, 180)) 
            if kamehamehaCount in range(350, 360):
               if kamehamehaCount % 5 == 0:
                  screen.blit(beam_left_imgs[4], (goku_x - 132, 170))  
                  screen.blit(beam_left_imgs[5], (goku_x - 189, 187)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 249, 187)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 299, 187)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 349, 187)) 
               else:
                  screen.blit(beam_left_imgs[6], (goku_x - 127, 185))  
                  screen.blit(beam_left_imgs[7], (goku_x - 173, 192)) 
                  screen.blit(beam_left_imgs[7], (goku_x - 233, 192))
                  screen.blit(beam_left_imgs[7], (goku_x - 287, 192))
                  screen.blit(beam_left_imgs[7], (goku_x - 337, 192))
            if kamehamehaCount in range(360, 370):
               if kamehamehaCount % 2 == 0:
                  screen.blit(beam_left_imgs[8], (goku_x - 129, 192))  
                  screen.blit(beam_left_imgs[9], (goku_x - 173, 192)) 
                  screen.blit(beam_left_imgs[9], (goku_x - 233, 192))
                  screen.blit(beam_left_imgs[9], (goku_x - 287, 192))
                  screen.blit(beam_left_imgs[9], (goku_x - 337, 192))
               else:
                  screen.blit(beam_left_imgs[6], (goku_x - 127, 185))  
                  screen.blit(beam_left_imgs[7], (goku_x - 173, 192)) 
                  screen.blit(beam_left_imgs[7], (goku_x - 233, 192))
                  screen.blit(beam_left_imgs[7], (goku_x - 287, 192))
                  screen.blit(beam_left_imgs[7], (goku_x - 337, 192))   
            kamehamehaCount += 1
         else:
            if kamehamehaCount in range(0, 20):
               screen.blit(superkamehameha_left_imgs[kamehamehaCount//5], (goku_x + 19, 190)) 
            elif kamehamehaCount in range(20, 230): 
               screen.blit(superkamehameha_left_imgs[kamehamehaCount//5], (goku_x + 17, 185))  
            if kamehamehaCount == 0: 
               kamehameha_Sound.play()
            kamehamehaCount+=1
      else:
         if kamehamehaCount in range(230, 370): 
            screen.blit(kamehameha_left_imgs[kamehamehaCount//5], (goku_x - 15, 200)) 
            if kamehamehaCount in range(230, 350):
               if kamehamehaCount % 5 == 0: 
                  screen.blit(beam_left_imgs[0], (goku_x - 128, 160))  
                  screen.blit(beam_left_imgs[1], (goku_x - 186, 185)) 
                  screen.blit(beam_left_imgs[1], (goku_x - 246, 185))
                  screen.blit(beam_left_imgs[1], (goku_x - 300, 185))
                  screen.blit(beam_left_imgs[1], (goku_x - 350, 185))
               else:
                  screen.blit(beam_left_imgs[2], (goku_x - 128, 160)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 180, 190)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 210, 190))
                  screen.blit(beam_left_imgs[3], (goku_x - 270, 190))  
                  screen.blit(beam_left_imgs[3], (goku_x - 330, 190)) 
                  screen.blit(beam_left_imgs[3], (goku_x - 390, 190)) 
            if kamehamehaCount in range(350, 360):
               if kamehamehaCount % 5 == 0:
                  screen.blit(beam_left_imgs[4], (goku_x - 145, 180))  
                  screen.blit(beam_left_imgs[5], (goku_x - 202, 197)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 262, 197)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 312, 197)) 
                  screen.blit(beam_left_imgs[5], (goku_x - 362, 197)) 
               else:
                  screen.blit(beam_left_imgs[6], (goku_x - 140, 195))  
                  screen.blit(beam_left_imgs[7], (goku_x - 186, 202)) 
                  screen.blit(beam_left_imgs[7], (goku_x - 246, 202))
                  screen.blit(beam_left_imgs[7], (goku_x - 300, 202))
                  screen.blit(beam_left_imgs[7], (goku_x - 350, 202))
            if kamehamehaCount in range(360, 370):
               if kamehamehaCount % 2 == 0:
                  screen.blit(beam_left_imgs[8], (goku_x - 142, 202))  
                  screen.blit(beam_left_imgs[9], (goku_x - 186, 212)) 
                  screen.blit(beam_left_imgs[9], (goku_x - 246, 212))
                  screen.blit(beam_left_imgs[9], (goku_x - 300, 212))
                  screen.blit(beam_left_imgs[9], (goku_x - 350, 212))
               else:
                  screen.blit(beam_left_imgs[6], (goku_x - 140, 195))  
                  screen.blit(beam_left_imgs[7], (goku_x - 186, 202)) 
                  screen.blit(beam_left_imgs[7], (goku_x - 246, 202))
                  screen.blit(beam_left_imgs[7], (goku_x - 300, 202))
                  screen.blit(beam_left_imgs[7], (goku_x - 350, 202))   
            kamehamehaCount += 1
         else:
            screen.blit(kamehameha_left_imgs[kamehamehaCount//5], (goku_x, 200))
            if kamehamehaCount == 0: 
               kamehameha_Sound.play()
            kamehamehaCount+=1
         
         
   elif standing_dir == 'right' and shooting_kiblast == False and dragonfist_attack == False and is_punching == False and is_kicking == False and is_jumping == False and launching_spiritbomb == False: # standing -->
      kamehamehaCount = 0
      launch_dragonfist_right = False
      dragonfistCount = 0
      ss3Count = 0
      dragonfist_x_right = goku_x + 65
      standCount += 1
      launching_spiritbomb = False 
      bombattackCount = 0
      spiritbomb_x = goku_x
      spiritbombCount = 0
      if saiyan_form == 1: #turning goku into a super saiyan animation + s1 goku standing animation
         
         power_down = True # allows goku to power down after becoming a super saiyan
         
         if s1Count < 520: #doesn't allow the player to move goku while he is transforming into a super saiyan
            disable_key = True
         else:
            disable_key = False
            
         if s1Count == 0:
            s1transformation_Sound.play()
            
            
         if s1Count in range(200, 205):
            screen.blit(lightning_imgs[lightningCount//3], (goku_x - 40, 150))
            lightningCount+=1
            
         if s1Count == 519:
            s1_Sound.play(-1)
                   
         if s1Count in range(0, 200) or s1Count in range (226, 400):
            if formCount in range(14, 21):
               screen.blit(base_right_imgs[formCount//7], (goku_x - 9, 176))
            elif formCount in range(21, 28):
               screen.blit(base_right_imgs[formCount//7], (goku_x - 9, 171))
            elif formCount in range(28, 35):
               screen.blit(base_right_imgs[formCount//7], (goku_x - 13, 168))
            else:
               screen.blit(base_right_imgs[formCount//7], (goku_x + 5, 176))
            s1Count += 1
            formCount += 1
         elif s1Count < 410:
            if formCount in range(14, 21):
               screen.blit(s1_right_imgs[formCount//7], (goku_x - 9, 173))
            elif formCount in range(21, 28):
               screen.blit(s1_right_imgs[formCount//7], (goku_x - 9, 168))
            elif formCount in range(28, 35):
               screen.blit(s1_right_imgs[formCount//7], (goku_x - 13, 165))
            else:
               screen.blit(s1_right_imgs[formCount//7], (goku_x + 5, 173))
            s1Count += 1
            formCount += 1
         elif s1Count in range(410, 470):
            if formCount2 + 1 >= 71:
               formCount2 = 56
            screen.blit(s1_right_imgs[formCount2//8], (goku_x + 16, 183))
            s1Count += 1
            formCount2 += 1
         elif s1Count in range(470, 520):
            if formCount2 + 1 >= 87:
               formCount2 = 72
            screen.blit(s1_right_imgs[formCount2//8], (goku_x + 16, 183))
            s1Count += 1
            formCount2 += 1   
         elif s1Count == 520:
            if standCount in range(5, 10):
               screen.blit(s1_standing_right_imgs[standCount//5], (goku_x - 12, 164)) 
            elif standCount in range(10, 20):
               screen.blit(s1_standing_right_imgs[standCount//5], (goku_x - 22, 161)) 
            else:
               screen.blit(s1_standing_right_imgs[standCount//5], (goku_x - 7, 164)) 
      elif saiyan_form == 0:
         if power_down == True:
            s1_Sound.stop()
            if powerDownCount + 1 <= 54:
               if powerDownCount in range (0, 18):
                  screen.blit(powerdown_right_imgs[powerDownCount//6], (goku_x + 16, 183))
               else:
                  screen.blit(powerdown_right_imgs[powerDownCount//6], (goku_x + 5, 173))
               powerDownCount += 1
               if powerDownCount == 54:
                  power_down = False
                  powerDownCount = 0
         if power_down == False:
            screen.blit(base_standing_right_imgs[standCount//5], (goku_x, goku_y))
          
      
      
   elif standing_dir == 'right' and shooting_kiblast == True:# kiblast -->
      if saiyan_form == 1:
         if kiblastCount in range(0, 4): 
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x + 1, 197))
         elif kiblastCount in range(4, 16): 
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 4, 195))
         elif kiblastCount in range(16, 24):
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 4, 190)) 
         elif kiblastCount in range(24, 32):
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 3, 178)) 
         elif kiblastCount in range(32, 36):
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 4, 195))
         elif kiblastCount in range(36, 44):
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 7, 195))
         elif kiblastCount in range(44, 48): 
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 4, 187)) 
         elif kiblastCount in range(48, 52): 
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 2, 187)) 
         else: 
            screen.blit(s1_kiblast_right_imgs[kiblastCount//4], (goku_x - 4, 182))
      else:
         if kiblastCount in range(16, 20):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x + 2, 198))
         elif kiblastCount in range(20, 24):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x + 4, 198))
         elif kiblastCount in range(24, 28):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x - 1, 181))
         elif kiblastCount in range(28, 32):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x + 1, 181))
         elif kiblastCount in range(44, 48):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x, 197))
         elif kiblastCount in range(48, 52):
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x + 6, 197))
         elif kiblastCount in range(52, 60): 
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x, 178))
         else:
            screen.blit(kiblast_right_imgs[kiblastCount//4], (goku_x - 2, 200))
      kiblastCount += 1
      if kiblastCount == 31: #shoots ki blast to the right only at the end of Goku's shooting animation 
         kiblast_Sound.play() 
         kiblast_shot_right = 1
         kiblast_x_right = goku_x + 80
      if kiblastCount == 59: 
         kiblast_Sound.play()   
         kiblast_shot_right = 2
         kiblast_x_right = goku_x + 80
         
         
   elif standing_dir == 'left' and shooting_kiblast == False and dragonfist_attack == False and is_punching == False and is_kicking == False and is_jumping == False and launching_spiritbomb == False: # standing <--
      kamehamehaCount = 0
      launch_dragonfist_left = False
      dragonfistCount = 0
      ss3Count = 0
      dragonfist_x_left = goku_x - 60
      dragonfist_x_left2 = dragonfist_x_left - 200
      standCount += 1
      launching_spiritbomb = False 
      bombattackCount = 0
      spiritbomb_x = goku_x
      spiritbombCount = 0
      if saiyan_form == 1: #turning goku into a super saiyan animation + s1 goku standing animation
      
         power_down = True # allows goku to power down after becoming a super saiyan
      
         if s1Count < 520: #doesn't allow the player to move goku while he is transforming into a super saiyan
            disable_key = True
         else:
            disable_key = False
            
         if s1Count == 0:
            s1transformation_Sound.play()
            
         if s1Count in range(200, 205):
            screen.blit(lightning_imgs[lightningCount//3], (goku_x - 40, 150))
            lightningCount+=1
            
         if s1Count == 519:
            s1_Sound.play(-1)
            
         if s1Count in range(0, 200) or s1Count in range (226, 400):
            if formCount in range(14, 21):
               screen.blit(base_left_imgs[formCount//7], (goku_x - 15, 175))
            elif formCount in range(21, 28):
               screen.blit(base_left_imgs[formCount//7], (goku_x - 15, 170))
            elif formCount in range(28, 35):
               screen.blit(base_left_imgs[formCount//7], (goku_x - 19, 167))
            else:
               screen.blit(base_left_imgs[formCount//7], (goku_x + 3, 175))
            s1Count += 1
            formCount += 1
         elif s1Count < 410:
            if formCount in range(14, 21):
               screen.blit(s1_left_imgs[formCount//7], (goku_x - 15, 175))
            elif formCount in range(21, 28):
               screen.blit(s1_left_imgs[formCount//7], (goku_x - 15, 170))
            elif formCount in range(28, 35):
               screen.blit(s1_left_imgs[formCount//7], (goku_x - 19, 167))
            else:
               screen.blit(s1_left_imgs[formCount//7], (goku_x + 3, 175))
            s1Count += 1
            formCount += 1
         elif s1Count in range(410, 470):
            if formCount2 + 1 >= 71:
               formCount2 = 56
            screen.blit(s1_left_imgs[formCount2//8], (goku_x + 10, 180))
            s1Count += 1
            formCount2 += 1
         elif s1Count in range(470, 520):
            if formCount2 + 1 >= 87:
               formCount2 = 72
            screen.blit(s1_left_imgs[formCount2//8], (goku_x + 10, 180))
            s1Count += 1
            formCount2 += 1   
         elif s1Count == 520:
            if standCount in range(5, 10):
               screen.blit(s1_standing_left_imgs[standCount//5], (goku_x - 18, 160)) 
            elif standCount in range(10, 15):
               screen.blit(s1_standing_left_imgs[standCount//5], (goku_x - 27, 157))
            elif standCount in range(15, 20):
               screen.blit(s1_standing_left_imgs[standCount//5], (goku_x - 30, 155)) 
            else:
               screen.blit(s1_standing_left_imgs[standCount//5], (goku_x - 12, 160)) 
      elif saiyan_form == 0:
         if power_down == True:
            s1_Sound.stop()
            if powerDownCount + 1 <= 54:
               if powerDownCount in range (0, 18):
                  screen.blit(powerdown_left_imgs[powerDownCount//6], (goku_x + 10, 180))
               else:
                  screen.blit(powerdown_left_imgs[powerDownCount//6], (goku_x + 3, 175))
               powerDownCount += 1
               if powerDownCount == 54:
                  power_down = False
                  powerDownCount = 0
         if power_down == False:
            screen.blit(base_standing_left_imgs[standCount//5], (goku_x, goku_y)) 
      
      
   elif standing_dir == 'left' and shooting_kiblast == True: # kiblast <-- 
      if saiyan_form == 1:
         if kiblastCount in range(0, 4):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x + 10, 190))
         elif kiblastCount in range(4 , 16):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x + 10, 190))
         elif kiblastCount in range(16, 20):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 40, 185)) 
         elif kiblastCount in range(20, 24):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 42, 185))
         elif kiblastCount in range(24, 32):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 45, 175)) 
         elif kiblastCount in range(32, 44):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x + 15, 190))
         elif kiblastCount in range(44, 52):
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 36, 183)) 
         elif kiblastCount in range(52, 56): 
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 41, 178)) 
         else:
            screen.blit(s1_kiblast_left_imgs[kiblastCount//4], (goku_x - 45, 178))  
      else:
         if kiblastCount in range(0, 4):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x + 3, 200))
         elif kiblastCount in range(4, 16):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x + 6, 200))
         elif kiblastCount in range(16, 20):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 44, 198))
         elif kiblastCount in range(20, 24):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 47, 198))
         elif kiblastCount in range(24, 28):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 52, 181))
         elif kiblastCount in range(28, 32): 
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 55, 181))
         elif kiblastCount in range(32, 44):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x + 3, 200))
         elif kiblastCount in range(44, 48):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 42, 198))
         elif kiblastCount in range(48, 52):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 50, 198))
         elif kiblastCount in range(52, 56):
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 52, 178))
         else: 
            screen.blit(kiblast_left_imgs[kiblastCount//4], (goku_x - 54, 178))
      kiblastCount += 1         
      if kiblastCount == 31: #shoot ki blast to the left out of one hand only at the end of Goku's shooting animation
         kiblast_Sound.play()
         kiblast_shot_left = 1
         kiblast_x_left = goku_x - 35
      if kiblastCount == 59: #shoots ki blast to the left out of the other hand only at the end of Goku's shooting animation
         kiblast_Sound.play() 
         kiblast_shot_left = 2
         kiblast_x_left = goku_x - 35
     
     
   if kiblast_shot_left == 1: #shoot a ki blast across the screen to the left only at the frames when Goku is at the end of his shooting animation out of one hand
      if kiblast_x_left <= 400:
         screen.blit(blast_left_imgs[blastCount//3], (kiblast_x_left, 205))
         kiblast_x_left -= kiblast_x_changes
         blastCount += 1
         if blastCount + 1 >= 6: 
            blastCount = 0
                        
   if kiblast_shot_left == 2: #shoot a ki blast across the screen to the left only at the frames when Goku is at the end of his shooting animation out of the other hand
      if kiblast_x_left <= 400:
         screen.blit(blast_left_imgs[blastCount//3], (kiblast_x_left, 205))
         kiblast_x_left -= kiblast_x_changes
         blastCount += 1
         if blastCount + 1 >= 6: 
            blastCount = 0         
         
   if kiblast_shot_right == 1: #shoot a ki blast across the screen to the right only at the frames when Goku is at the end of his shooting animation out of one hand
      if kiblast_x_right >= 0:
         screen.blit(blast_right_imgs[blastCount//3], (kiblast_x_right, 205))
         kiblast_x_right += kiblast_x_changes
         blastCount += 1
         if blastCount + 1 >= 6: 
            blastCount = 0
            
            
   if kiblast_shot_right == 2: #shoot a ki blast across the screen to the right only at the frames when Goku is at the end of his shooting animation out of the other hand
      if kiblast_x_right >= 0:
         screen.blit(blast_right_imgs[blastCount//3], (kiblast_x_right, 205))
         kiblast_x_right += kiblast_x_changes
         blastCount += 1
         if blastCount + 1 >= 6: 
            blastCount = 0
            
            
           
   if dragonfist_attack == True and standing_dir == 'right': #dragonfist -->
      disable_key = True
      if ss3Count in range(0, 126):
         screen.blit(ss3_right_imgs[ss3Count//9], (goku_x + 5, 180))
      if ss3Count in range(126, 135):
         screen.blit(ss3_right_imgs[ss3Count//9], (goku_x + 5, 173)) 
      if ss3Count in range(135, 143):
         screen.blit(ss3_right_imgs[ss3Count//9], (goku_x + 16, 183)) 
      ss3Count += 1
      if ss3Count == 80: #adjust to time when dragon fist attack gets launched across the screen
         launch_dragonfist_right = True
      if ss3Count == 143:
         dragonfist_attack = False
                
   if launch_dragonfist_right == True: #launch the dragon fist attack across the screen once ss3 goku has finished punching
      if dragonfist_x_right <= 450:
         if dragonfistCount in range(0, 5):
            screen.blit(dragonfist_right_imgs[dragonfistCount//5], (dragonfist_x_right, 190))
         if dragonfistCount in range(5, 15):
            screen.blit(dragonfist_right_imgs[dragonfistCount//5], (dragonfist_x_right, 185))
         if dragonfistCount in range (15, 36):
            screen.blit(dragonfist_right_imgs[dragonfistCount//5], (dragonfist_x_right, 185))
            dragonfist_x_right += dragonfist_x_changes
         dragonfistCount += 1

                 
   if dragonfist_attack == True and standing_dir == 'left': #dragonfist <--
      disable_key = True           
      if ss3Count in range(0, 81):
         screen.blit(ss3_left_imgs[ss3Count//9], (goku_x + 15, 180))
      if ss3Count in range(81, 99):
         screen.blit(ss3_left_imgs[ss3Count//9], (goku_x, 180))
      if ss3Count in range(99, 126):
         screen.blit(ss3_left_imgs[ss3Count//9], (goku_x + 15, 180))
      if ss3Count in range(126, 135):
         screen.blit(ss3_left_imgs[ss3Count//9], (goku_x + 3, 175))
      if ss3Count in range(135, 143):
         screen.blit(ss3_left_imgs[ss3Count//9], (goku_x + 10, 180))
      ss3Count += 1
      if ss3Count == 80: #adjust to time when dragon fist attack gets launched across the screen
         launch_dragonfist_left = True
      if ss3Count == 143:
         dragonfist_attack = False
                
   if launch_dragonfist_left == True: #launch the dragon fist attack across the screen once ss3 goku has finished punching
      if dragonfist_x_left >= -150:
         if dragonfistCount in range(0, 5):
            screen.blit(dragonfist_left_imgs[dragonfistCount//5], (dragonfist_x_left, 190))
         if dragonfistCount in range(5, 10):
            screen.blit(dragonfist_left_imgs[dragonfistCount//5], (dragonfist_x_left - 80, 185))
         if dragonfistCount in range(10, 15):
            screen.blit(dragonfist_left_imgs[dragonfistCount//5], (dragonfist_x_left - 145, 185))
         if dragonfistCount in range (15, 36):
            screen.blit(dragonfist_left_imgs[dragonfistCount//5], (dragonfist_x_left2, 185))
            dragonfist_x_left2 -= dragonfist_x_changes
         dragonfistCount += 1
         
         
   if is_punching == True and standing_dir == 'right' and shooting_kiblast == False: #punch -->
      disable_key = True
      if saiyan_form == 0:
         if punchCount in range(0, 15) or punchCount in range(25, 30):
            screen.blit(basepunch_right_imgs[punchCount//5], (goku_x, 198))
         elif punchCount in range(15, 25):
            screen.blit(basepunch_right_imgs[punchCount//5], (goku_x, 195))
         else:
            is_punching = False
            punchCount = 0
         punchCount += 1
      else:
         if punchCount in range(0, 30):
            screen.blit(superpunch_right_imgs[punchCount//5], (goku_x - 3, 190))
         else:
            is_punching = False
            punchCount = 0
         punchCount += 1
            
      
   if is_punching == True and standing_dir == 'left' and shooting_kiblast == False: #punch <--
      disable_key = True
      if saiyan_form == 0:
         if punchCount in range(0, 15) or punchCount in range(25, 30):
            screen.blit(basepunch_left_imgs[punchCount//5], (goku_x, 198))
         elif punchCount in range(15, 25):
            screen.blit(basepunch_left_imgs[punchCount//5], (goku_x - 20, 195))
         else:
            is_punching = False
            punchCount = 0
         punchCount += 1
      else:
         if punchCount in range(0, 15) or punchCount in range (25, 30):
            screen.blit(superpunch_left_imgs[punchCount//5], (goku_x + 15, 185))
         elif punchCount in range (15, 25):
            screen.blit(superpunch_left_imgs[punchCount//5], (goku_x - 7, 185))
         else:
            is_punching = False
            punchCount = 0
         punchCount += 1
         
         
   if is_kicking == True and standing_dir == 'right' and shooting_kiblast == False: #kick -->
      disable_key = True
      if saiyan_form == 0:
         if kickCount in range(0, 55):
            screen.blit(basekick_right_imgs[kickCount//5], (goku_x, 200))
         else:
            is_kicking = False
            kickCount = 0
         kickCount += 1
      else:
         if kickCount in range(0, 50):
            screen.blit(superkick_right_imgs[kickCount//5], (goku_x + 10, 190))
         else:
            is_kicking = False
            kickCount = 0
         kickCount += 1
 
   if is_kicking == True and standing_dir == 'left' and shooting_kiblast == False: #kick <--
      disable_key = True
      if saiyan_form == 0:
         if kickCount in range(0, 55):
            screen.blit(basekick_left_imgs[kickCount//5], (goku_x, 200))
         else:
            is_kicking = False
            kickCount = 0
         kickCount += 1
      else:
         if kickCount in range(0, 50):
            screen.blit(superkick_left_imgs[kickCount//5], (goku_x - 10, 190))
         else:
            is_kicking = False
            kickCount = 0
         kickCount += 1 
         
         
   if is_jumping == True and standing_dir == 'right' and shooting_kiblast == False: #jumping up facing right
      if saiyan_form == 0:
         if jumpTime >= -8:
            if goku_y == 200 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[0], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 125.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 113 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
            
                  
            if goku_y == 105 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1 
            
                  
            if goku_y == 100.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                          
            if goku_y == 98.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                         
            if goku_y == 98.0 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jump_dir = 'down'
                  jumpTime -= 1
                             
            if goku_y == 98.0 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 98.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                        
            if goku_y == 100.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1            
                                                                     
            if goku_y == 105 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1   
                  
            if goku_y == 113 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                  
            if goku_y == 125.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1      
                  
            if goku_y == 200 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_right_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1                      
         else: 
            jumpTime = 8
            jump_dir = 'up'
            is_jumping = False 
            on_ground = True 
      else:   
         if jumpTime >= -8:
            if goku_y == 200 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[0], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[1], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[1], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 125.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[1], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 113 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[1], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
            
                  
            if goku_y == 105 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[1], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1 
            
                  
            if goku_y == 100.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                          
            if goku_y == 98.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                         
            if goku_y == 98.0 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jump_dir = 'down'
                  jumpTime -= 1
                             
            if goku_y == 98.0 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 98.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                        
            if goku_y == 100.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[2], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1            
                                                                     
            if goku_y == 105 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1   
                  
            if goku_y == 113 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                  
            if goku_y == 125.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1      
                  
            if goku_y == 200 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_right_imgs[3], (goku_x + 5 + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1                      
         else: 
            jumpTime = 8
            jump_dir = 'up'
            is_jumping = False 
            on_ground = True             
            
              
   if is_jumping == True and standing_dir == 'left' and shooting_kiblast == False: #base form goku jumping up facing left 
      if saiyan_form == 0:
         if jumpTime >= -8:
            if goku_y == 200 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[0], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 125.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 113 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
            
                  
            if goku_y == 105 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[1], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1 
            
                  
            if goku_y == 100.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                          
            if goku_y == 98.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                         
            if goku_y == 98.0 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jump_dir = 'down'
                  jumpTime -= 1
                             
            if goku_y == 98.0 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 98.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                        
            if goku_y == 100.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[2], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1            
                                                                     
            if goku_y == 105 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1   
                  
            if goku_y == 113 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                  
            if goku_y == 125.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1      
                  
            if goku_y == 200 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(basejump_left_imgs[3], (goku_x, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1                      
         else: 
            jumpTime = 8
            jump_dir = 'up'
            is_jumping = False 
            on_ground = True 
      else:
         if jumpTime >= -8:
            if goku_y == 200 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[0], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[1], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[1], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 125.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[1], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
                  
            if goku_y == 113 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[1], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
            
                  
            if goku_y == 105 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[1], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1 
            
                  
            if goku_y == 100.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                          
            if goku_y == 98.5 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                         
            if goku_y == 98.0 and jump_dir == 'up':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jump_dir = 'down'
                  jumpTime -= 1
                             
            if goku_y == 98.0 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 98.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                        
            if goku_y == 100.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[2], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1            
                                                                     
            if goku_y == 105 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1   
                  
            if goku_y == 113 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1    
                  
            if goku_y == 125.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 143.5 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1
                  
            if goku_y == 168 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x , goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1      
                  
            if goku_y == 200 and jump_dir == 'down':
               if slowDown in range(0, 2):
                  screen.blit(superjump_left_imgs[3], (goku_x  + 5, goku_y))
                  slowDown += 1
               else:
                  slowDown = 0
                  goku_y -= (jumpTime * abs(jumpTime)) * 0.5
                  jumpTime -= 1                      
         else: 
            jumpTime = 8
            jump_dir = 'up'
            is_jumping = False   
            on_ground = True 
            
            
   if moving_right and on_ground == False: #moving across the air to the right
      goku_x += goku_x_changes
      if goku_x + goku_x_changes >= 338: #makes sure goku cannot walk off the right edge of the screen
         goku_x = 338
  
       
   if moving_left and on_ground == False: #moving across the air to the left
      goku_x -= goku_x_changes 
      if goku_x - goku_x_changes <= -2: #makes sure goku cannot walk off the left edge of the screen
         goku_x = -2 
   
   if standing_dir == 'left' and launching_spiritbomb == True: #spirit bomb <--
      disable_key = True
      if bombattackCount in range(0, 10): #plays bombattack 1 - 2
         screen.blit(bombattack_left_imgs[bombattackCount//5], (goku_x + 7, 187)) 
         bombattackCount += 1
      if bombattackCount in range(10, 20) and spiritbombCount + 1 <= 40:
         screen.blit(bombattack_left_imgs[bombattackCount//5], (goku_x + 7, 187))
         if bombattackCount + 1 >= 20: #alternate between bombattack 3 - 4
            bombattackCount = 10
         bombattackCount += 1
         if spiritbombCount in range(0, 10):
            screen.blit(spiritbomb_left_imgs[spiritbombCount//5], (spiritbomb_x + 10, 120))
         if spiritbombCount in range(10, 20):
            screen.blit(spiritbomb_left_imgs[spiritbombCount//5], (spiritbomb_x - 15, 95))
         if spiritbombCount in range(20, 30):
            screen.blit(spiritbomb_left_imgs[spiritbombCount//5], (spiritbomb_x - 30, 65))
         if spiritbombCount in range(30, 40):
            screen.blit(spiritbomb_left_imgs[spiritbombCount//5], (spiritbomb_x - 45, 45))
         spiritbombCount += 1
         if spiritbombCount == 40:
            bombattackCount = 20
            spiritbombCount = 30 
      if bombattackCount in range(20, 55) and spiritbombCount in range(30, 40):
         screen.blit(bombattack_left_imgs[bombattackCount//5], (goku_x + 7, 187))
         screen.blit(spiritbomb_left_imgs[spiritbombCount//5], (spiritbomb_x - 45, 45))
         if bombattackCount in range(40, 55): #moving spirit bomb to right while alternatiing between bomb attack 9 - 11
            spiritbomb_x -= 10
         if spiritbombCount + 1 >= 40: #alternate between spiritbomb 7 - 8
            spiritbombCount = 30
         if bombattackCount + 1 >= 55: #alternate between bombattack 9 - 11
            bombattackCount = 40
         bombattackCount += 1
         spiritbombCount += 1
      if spiritbomb_x == -100:
         bombattackCount = 55
         spiritbomb_x -= 1
      if spiritbomb_x <= -101:
         screen.blit(bombattack_left_imgs[bombattackCount//5], (goku_x + 7, 187))
         bombattackCount += 1
         if bombattackCount + 1 >= 70:
            launching_spiritbomb = False 
            bombattackCount = 0
            spiritbomb_x = goku_x
            spiritbombCount = 0
            
                 
   if standing_dir == 'right' and launching_spiritbomb == True: #spirit bomb -->
      disable_key = True
      if bombattackCount in range(0, 10): #plays bombattack 1 - 2
         screen.blit(bombattack_right_imgs[bombattackCount//5], (goku_x + 7, 187)) 
         bombattackCount += 1
      if bombattackCount in range(10, 20) and spiritbombCount + 1 <= 40:
         screen.blit(bombattack_right_imgs[bombattackCount//5], (goku_x + 7, 187))
         if bombattackCount + 1 >= 20: #alternate between bombattack 3 - 4
            bombattackCount = 10
         bombattackCount += 1
         if spiritbombCount in range(0, 10):
            screen.blit(spiritbomb_right_imgs[spiritbombCount//5], (spiritbomb_x + 10, 120))
         if spiritbombCount in range(10, 20):
            screen.blit(spiritbomb_right_imgs[spiritbombCount//5], (spiritbomb_x - 15, 95))
         if spiritbombCount in range(20, 30):
            screen.blit(spiritbomb_right_imgs[spiritbombCount//5], (spiritbomb_x - 30, 65))
         if spiritbombCount in range(30, 40):
            screen.blit(spiritbomb_right_imgs[spiritbombCount//5], (spiritbomb_x - 45, 45))
         spiritbombCount += 1
         if spiritbombCount == 40:
            bombattackCount = 20
            spiritbombCount = 30 
      if bombattackCount in range(20, 55) and spiritbombCount in range(30, 40):
         screen.blit(bombattack_right_imgs[bombattackCount//5], (goku_x + 7, 187))
         screen.blit(spiritbomb_right_imgs[spiritbombCount//5], (spiritbomb_x - 45, 45))
         if bombattackCount in range(40, 55): #moving spirit bomb to right while alternatiing between bomb attack 9 - 11
            spiritbomb_x += 10
         if spiritbombCount + 1 >= 40: #alternate between spiritbomb 7 - 8
            spiritbombCount = 30
         if bombattackCount + 1 >= 55: #alternate between bombattack 9 - 11
            bombattackCount = 40
         bombattackCount += 1
         spiritbombCount += 1
      if spiritbomb_x == 400:
         bombattackCount = 55
         spiritbomb_x += 1
      if spiritbomb_x >= 401:
         screen.blit(bombattack_right_imgs[bombattackCount//5], (goku_x + 7, 187))
         bombattackCount += 1
         if bombattackCount + 1 >= 70:
            launching_spiritbomb = False 
            bombattackCount = 0
            spiritbomb_x = goku_x
            spiritbombCount = 0
            
                                       
   pygame.display.update()
   clock.tick(60)  
 
while True:
   redrawGameWindow()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()  
      
      if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_1 and shooting_kamehameha == False and shooting_kiblast == False and is_jumping == False: #turns base form goku into a super saiyan 1
            saiyan_form = 1
         if event.key == pygame.K_0 and disable_key == False and power_down == True and saiyan_form == 1 and shooting_kiblast == False and shooting_kamehameha == False and is_jumping == False: # turns super saiyan goku back into base form goku
            s1Count = 0
            saiyan_form = 0
            lightningCount = 0
            powerdown_Sound.play()
         if event.key == pygame.K_LSHIFT and disable_key == False and is_jumping == False: #shooting kamehameha animation
            shooting_kamehameha = True  
         if event.key == pygame.K_a and disable_key == False and is_jumping == False and is_kicking == False: #punch
            is_punching = True
            punch_Sound.play()
         if event.key == pygame.K_s and disable_key == False and is_jumping == False and is_punching == False: #kick
            is_kicking = True
            kick_Sound.play()
         if event.key == pygame.K_2 and disable_key == False and is_jumping == False and saiyan_form == 1 and spiritbomb_still == True: #spirit bomb - only when in super saiyan form
            launching_spiritbomb = True
            spiritbomb_released_Sound.play()
         if event.key == pygame.K_3 and disable_key == False and saiyan_form == 1 and is_jumping == False and dragonfist_still == True: #dragon fist - only when in super saiyan form
            dragonfist_attack = True
            dragonfist_Sound.play()
         if event.key == pygame.K_SPACE and disable_key == False: #jumping
            is_jumping = True    
            on_ground = False         
   if event.type == pygame.KEYDOWN:
      keys = pygame.key.get_pressed()  #checking pressed keys
      if keys[pygame.K_TAB] and disable_key == False and is_jumping == False: #shoot kiblast
         shooting_kiblast = True
      if keys[pygame.K_LEFT] and disable_key == False: #moving left
         standing_dir = 'left'
         moving_left = True
         moving_right = False
         dragonfist_still = False
         spiritbomb_still = False
         if is_jumping:
            on_ground = False
      if keys[pygame.K_RIGHT] and disable_key == False: #moving right
         standing_dir = 'right'
         moving_left = False
         moving_right = True
         spiritbomb_still = False
         dragonfist_still = False
         if is_jumping:
            on_ground = False
   if event.type == pygame.KEYUP: #goes back to Goku standing animation
      if not is_jumping:  
         moving_left = False
         moving_right = False
      shooting_kiblast = False
      disable_key = False
      spiritbomb_still = True
      dragonfist_still = True

