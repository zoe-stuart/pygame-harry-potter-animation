# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
width = 800
height = 600
SIZE = (width, height)
TITLE = "A Seeker's Match"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

scale = 5


# Timer
clock = pygame.time.Clock()
refresh_rate = 80


# Colors
''' add colors you use as RGB values here '''
R  = (168, 21, 14)
O  = (238, 140, 65)
LY = (255, 224, 74)
Y  = (188, 156, 35)
DY = (108, 81, 10)
SB = (0, 234, 242)
W  = (255, 255, 255)
S  = (233, 206, 163)
DS = (111, 86, 46)
LB = (156, 73, 41)
T  = (185, 126, 60)
DB = (50, 15, 0)
G  = (66, 78, 74)
LG = (116, 115, 118)
B  = (0, 0, 0)

TR = None
 
snitch_a =[[TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
          [TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
          [ Y, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
          [ Y,  Y, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
          [ Y, LY,  Y, TR, TR, TR, TR,  Y, LY,  Y, TR],
          [TR,  Y, LY,  Y,  Y,  Y, TR, TR,  Y,  Y, TR],
          [TR,  Y, LY, LY, LY, LY,  Y, DY, DY, DY, TR],
          [TR, TR,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
          [TR, TR, TR, TR, TR, TR, DY, LY, LY, LY, DY],
          [TR, TR, TR, TR, TR, TR, DY, LY, LY, LY, DY],
          [TR, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR]]

snitch_b = [[TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
            [ Y, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
            [ Y,  Y, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [ Y, LY,  Y, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [TR,  Y, LY,  Y,  Y,  Y, TR, DY, DY, DY, TR],
            [TR,  Y, LY, LY, LY, LY, DY, LY, LY, LY, DY],
            [TR, TR,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR, TR, TR, TR, TR, TR, DY, LY, LY, LY, DY],
            [TR, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR]]


snitch_c = [[TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [ Y, TR, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [ Y,  Y, TR, TR, TR, TR, TR, DY, DY, DY, TR],
            [ Y, LY,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR,  Y, LY, LY, LY, LY, DY, LY, LY, LY, DY],
            [TR, TR,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR]]


snitch_d = [[TR, TR, TR, TR, TR, TR, TR, TR,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [ Y, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR],
            [ Y,  Y, TR, TR, TR, TR, DY, LY, LY, LY, DY],
            [ Y, LY,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR,  Y, LY, LY, LY, LY, DY, LY, LY, LY, DY],
            [TR, TR,  Y,  Y,  Y,  Y, TR, DY, DY, DY, TR]]


snitch_e = [[TR, TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [TR, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR],
            [TR, TR, TR, TR, TR, TR, DY, LY, LY, LY, DY],
            [TR, TR,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR,  Y, LY, LY, LY, LY, DY, LY, LY, LY, DY],
            [ Y, LY,  Y,  Y,  Y,  Y, TR, DY, DY, DY, TR],
            [ Y,  Y, TR, TR, TR, TR, TR, TR, TR, TR, TR],
            [ Y, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]]


snitch_f = [[TR, TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y,  Y, TR, TR],
            [TR, TR, TR, TR, TR, TR, TR,  Y, LY,  Y, TR],
            [TR, TR, TR, TR, TR, TR, TR, DY, DY, DY, TR],
            [TR, TR,  Y,  Y,  Y,  Y, DY, LY, LY, LY, DY],
            [TR,  Y, LY, LY, LY, LY, DY, LY, LY, LY, DY],
            [ Y, LY,  Y,  Y,  Y, LY, DY, LY, LY, LY, DY],
            [ Y,  Y, TR, TR, TR,  Y, TR, DY, DY, DY, TR],
            [ Y, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]]


          
harry_left = [[TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR,  B],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR,  B,  G],
              [TR, TR, TR,  B,  B,  B,  B,  B, TR, TR, TR,  B,  B,  G,  G],
              [TR, TR, TR,  B,  G,  G,  G,  G,  B,  B,  B,  G,  G,  G,  G],
              [TR, TR, TR,  B,  G,  G,  G,  G,  G,  G,  G,  G,  G,  G,  G],
              [TR, TR, TR, TR,  B,  G,  G,  G,  G,  G,  G,  G,  G,  G,  G],
              [TR, TR, TR, TR,  B,  G,  G,  G,  G,  G,  G,  G,  G,  G,  G],
              [LB, LB, LB, LB, LB,  B,  G,  G,  G,  G,  G,  G,  G,  G,  G],
              [TR, LB,  T,  T,  T,  T,  B,  G,  G,  G,  G,  G,  G,  G,  B],
              [LB, LB,  T,  T,  T,  T,  T,  B,  G,  G,  G,  G,  G,  B, LB],
              [TR, LB,  T,  T,  T,  T,  T,  T,  B,  G,  G,  G,  B, LB,  T],
              [TR, TR, LB,  T,  T,  T,  T,  T,  T,  B,  B,  B, LB,  T,  T],
              [TR, TR, LB,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T],
              [TR, LB, LB,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T],
              [TR, TR, TR, LB,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T,  T],
              [TR, TR, TR, TR, LB,  T,  T,  T,  T,  T,  T,  T,  T,  T,  B],
              [TR, TR, LB, LB, LB, LB, LB,  T,  T,  T,  T,  T,  T,  B,  B],
              [TR, TR, TR, TR, TR, TR, LB, LB, LB,  T,  T,  T, LB,  B,  B],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, LB, LB, LB, TR,  B,  B],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR,  B],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR,  B],
             ] 

harry_main = [[TR, TR, TR, TR, TR, TR, TR,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR, TR],
              [TR, TR, TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR],
              [TR, TR, TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR],
              [TR, TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR],
              [TR, TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR],
              [TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR],
              [ B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR],
              [TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  S,  B,  B,  B,  B,  B,  B,  B,  B,  B],
              [TR,  B,  B,  B,  B,  B,  B,  B,  B,  B,  S,  S,  B,  S,  B,  B,  B,  B,  B,  B, TR],
              [ B,  B,  B,  B,  B,  B,  S,  B,  S,  S,  S,  S,  S,  S,  B,  S,  S,  B,  B,  B,  B],
              [ B,  B,  B,  B,  B,  B,  S, LG, LG, LG, LG,  S,  S, LG, LG, LG, LG,  S,  B,  B,  B],
              [ B,  B,  B,  B,  B, LG, LG,  W,  B,  B,  W, LG, LG,  W,  B,  B,  W, LG,  B,  B, TR],
              [ B,  B,  B,  B,  B,  S, LG,  W,  B,  B,  W, LG, LG,  W,  B,  B,  W, LG,  B,  B, TR],
              [TR,  B,  B,  S,  S,  S, LG,  W,  B,  B,  W, LG, LG,  W,  B,  B,  W, LG,  B,  B, TR],
              [TR,  B,  B,  S,  S,  S, LG,  W,  W,  W,  W, LG, LG,  W,  W,  W,  W, LG, DS, TR, TR],
              [TR, TR,  B,  B,  B,  S,  S, LG, LG, LG, LG,  S,  S, LG, LG, LG, LG,  S, DS, TR, TR],
              [TR, TR,  B,  B,  B, DS,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, DS, TR,  B,  B],
              [TR, TR, TR,  B,  B, DS,  S,  S,  S,  B,  B,  B,  B,  B,  S,  S,  S, DS,  B,  G,  G],
              [TR, TR,  B,  G,  R,  R, DS,  S,  S,  S,  S,  S,  S,  S,  S,  S, DS,  G,  G,  G,  G],
              [TR,  B,  G,  G,  R,  R,  R, DS,  S,  S,  S,  S,  S,  S,  S, DS,  G,  G,  G,  G,  G],
              [TR,  B,  G,  G,  G,  R,  R,  W, DS, DS, DS, DS, DS, DS, DS,  R,  G,  G,  G,  G,  B],
              [ B,  G,  G,  G,  G,  G,  R,  W,  W,  W,  R,  W,  W,  R,  R,  G,  G,  G,  B,  B, TR],
              [ B,  G,  G,  G,  G,  G,  R,  R,  W,  R,  R,  R,  W,  R,  R,  G,  G,  B, TR, TR, TR],
              [ B,  G,  G,  G,  G,  G,  B,  R,  O,  R,  R,  R,  O,  R,  R,  G,  B, TR, TR, TR, TR],
              [ G,  G,  G,  G,  G,  G,  B,  R, LG,  O,  R,  R,  O,  R,  G,  B, TR, TR, TR, TR, TR],
              [ G,  G,  B,  G,  G,  G,  G,  B, LG, LG,  O,  O, LG,  G,  G,  B, TR, TR, TR, TR, TR],
              [ G,  G,  B,  G,  G,  G,  G,  G,  B, LG, LG, LG, LG,  G,  G,  B, TR, TR, TR, TR, TR],
              [ G,  G,  G,  B,  G,  G,  G,  G,  G,  B, LG, LG, LG,  G,  B, TR, TR, TR, TR, TR, TR],
              [ G,  G,  G,  B,  G,  G,  G,  G,  G,  G,  G,  B,  G,  G,  B, TR, TR, TR, TR, TR, TR],
              [ G,  G,  B,  B,  G,  G,  G,  G,  G,  G,  B,  B,  G,  G,  B, TR, TR, TR, DB, DB, DB],
              [ G,  B,  B,  B,  B,  G,  G,  G,  G,  B,  R,  R, DS, DS,  B, DB, DB, DB, LB, LB, LB],
              [ B,  B,  B,  B,  B,  G,  G,  G,  B,  R,  S,  S,  S,  S, DS, LB, LB, LB, LB, LB, LB],
              [LB,  B,  B,  B,  B,  G,  B,  B,  R,  S,  S,  S,  S,  S, DS, LB, LB, LB, LB, DB, DB],
              [LB,  B,  B,  B,  B,  B,  R,  R,  B,  S,  S,  S,  S, DS,  S,  S, DS, DB, DB, TR, TR],
              [LB,  B,  B,  B,  B,  R,  R,  B,  B, DS,  S,  S,  S, DS,  S,  S, DS, TR, TR, TR, TR],
              [LB,  B,  B,  B,  B,  B,  B,  B,  B,  B, DS, DS, DS,  B, DS, DS, TR, TR, TR, TR, TR],
              [LB,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B,  B,  B, TR,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B,  B, TR, TR,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B, TR, TR, TR,  B,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B, TR, TR, TR, TR,  B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B, TR, TR, TR, TR, TR,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [ B,  B,  B,  B, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
             ]

harry_right = [[TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, DB, DB], 
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB],
              [TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, DB, LB, DB, TR],
              [TR, TR, TR, TR, TR, TR, TR, DB, LB, DB, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, DB, LB, DB, TR, TR],
              [TR, TR, TR, TR, TR, DS, DS, DB, LB, DB, TR, TR],
              [TR, TR,  B,  B, DS,  S,  S, DS, DB, DB, TR, TR],
              [ B,  B,  G,  G, DS,  S,  S, DS,  S,  S, DS, TR],
              [ G,  G,  G,  G,  G, DS, DS,  S,  S,  S, DS, TR],
              [ G,  G,  G,  G,  G,  B,  S,  S,  S,  S, DS, TR],
              [ G,  G,  G,  G,  G,  B,  S,  S,  S, DS, TR, TR],
              [ G,  G,  G,  G,  G,  B, DB, DB, DS, TR, TR, TR],
              [ B,  B,  G,  G,  G,  B, LB, DB, TR, TR, TR, TR],
              [TR, TR,  B,  B,  B,  B, LB, DB, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, DB, DB, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, DB, DB, DB, TR, TR, TR],
              [TR, TR, TR, DB, DB, DB, LB, LB, LB, DB, TR, TR],
              [DB, DB, DB, LB, LB, LB, LB, LB, LB, DB, TR, TR],
              [LB, LB, LB, LB, LB, LB, LB, DB, DB, TR, TR, TR],
              [LB, LB, LB, LB, DB, DB, DB, TR, TR, TR, TR, TR],
              [LB, DB, DB, DB, TR, TR, TR, TR, TR, TR, TR, TR],
              [DB, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]]


C5 = (100, 251, 255)
C4 = (128, 252, 255)
C3 = (179, 253, 255)
C2 = (210, 254, 255)
C1 = (255, 255, 255)

cloud =[]

cloud.append([[TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C1, C1, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, TR, C1, C2, C2, C2, C2, C2, C1, C1, C1, C1, TR, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, C1, C2, C2, C2, C2, C2, C2, C2, C2, C2, C2, C4, C4, TR],
	   [TR, TR, TR, TR, TR, TR, TR, C2, C2, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4],
	   [TR, TR, TR, TR, TR, C1, C1, C2, C2, C3, C3, C3, C3, C3, C2, C2, C3, C2, C2, C3, C3, C4],
	   [TR, TR, TR, TR, C1, C1, C2, C2, C3, C3, C3, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C4],
	   [TR, TR, C1, C2, C2, C2, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C4, C4],
	   [TR, C1, C1, C2, C2, C3, C3, C3, C3, C2, C2, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4, C4],
	   [TR, C1, C1, C2, C2, C3, C3, C3, C3, C2, C2, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4, C4],
	   [TR, C2, C2, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4, C4, C4, C4, C3, C4, C4],
	   [TR, C4, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C4, C4, C3, C3, C4, C4, C4, C4, C4, TR],
	   [C4, C4, C4, C4, C4, C4, C4, C4, C4, C3, C3, C4, C4, C3, C4, C4, C5, C5, C5, TR, TR, TR],
	   [TR, C4, C5, C5, C5, C5, C4, C4, C4, C4, C4, C4, C4, C4, C4, TR, TR, TR, TR, TR, TR, TR],
	   [TR, TR, TR, TR, TR, C5, C5, C5, C5, C5, C5, C4, C5, C4, TR, TR, TR, TR, TR, TR, TR, TR]])


cloud.append([[TR, TR, TR, TR, TR, C2, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
	   [TR, TR, TR, C1, C1, C2, C2, C2, C2, C1, C1, C1, C1, C1, C1, TR, TR, TR, TR],
	   [TR, TR, TR, C1, C2, C2, C2, C2, C2, C2, C2, C2, C2, C2, C1, C1, TR, TR, TR],
	   [TR, TR, C2, C2, C2, C3, C2, C3, C3, C2, C3, C3, C2, C2, C2, C1, C1, TR, TR],
	   [TR, C1, C2, C2, C3, C3, C2, C3, C3, C3, C2, C3, C3, C3, C2, C2, C2, TR, TR],
	   [TR, C1, C2, C3, C3, C3, C3, C3, C3, C3, C2, C2, C3, C3, C2, C2, C2, C2, TR],
	   [TR, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C4, C5],
	   [C2, C2, C3, C3, C4, C4, C3, C4, C4, C3, C3, C4, C4, C4, C4, C4, C4, C4, C5],
	   [C4, C4, C3, C3, C3, C4, C4, C3, C4, C4, C3, C3, C4, C4, C5, C5, C5, C5, TR],
	   [C5, C4, C4, C4, C3, C3, C4, C4, C4, C4, C4, C4, C4, C5, TR, TR, TR, TR, TR],
	   [C5, C4, C4, C4, C4, C4, C4, C4, C5, C5, C4, C5, C5, TR, TR, TR, TR, TR, TR],
	   [TR, C5, C5, C4, C4, C4, C4, C5, C5, C5, TR, TR, TR, TR, TR, TR, TR, TR, TR],
	   [TR, TR, C5, C5, C5, C5, C5, C5, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]])

cloud.append([[TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C1, C1, C1, TR, TR, TR, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C2, C2, C2, C2, C2, TR, TR, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C2, C2, C2, C3, C2, C2, C3, TR, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C3, C3, C1, C1, C3, C2, C3, C3, C2, C2, C2, C2, TR, TR],
	   [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C1, C2, C2, C2, C2, C2, C3, C3, C3, C2, C2, C2, C1, TR],
	   [TR, TR, TR, C1, C1, C1, C1, C1, TR, TR, TR, TR, TR, TR, TR, C2, C2, C2, C2, C2, C3, C3, C3, C3, C3, C3, C2, C2, C2, TR],
	   [TR, TR, C3, C1, C2, C2, C2, C2, C2, TR, TR, TR, TR, TR, C4, C4, C4, C3, C3, C3, C3, C4, C4, C3, C3, C3, C3, C3, C4, TR],
	   [TR, TR, C3, C1, C2, C2, C2, C2, C2, TR, TR, TR, TR, TR, C4, C4, C4, C3, C3, C3, C3, C4, C4, C3, C3, C3, C3, C3, C4, TR],
	   [TR, C2, C2, C2, C2, C2, C2, C2, C1, C1, TR, TR, TR, TR, C5, C5, C4, C4, C4, C4, C4, C4, C5, C5, C4, C4, C3, C4, C4, C4],
	   [C4, C4, C3, C3, C3, C3, C3, C2, C2, C2, C2, TR, TR, TR, TR, TR, C5, C5, C5, C5, C5, C5, TR, C5, C5, C4, C4, C4, C4, C5],
	   [C5, C4, C4, C3, C3, C3, C3, C3, C3, C3, C3, C4, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C5, C5, C4, TR],
	   [C5, C5, C4, C4, C4, C4, C3, C3, C3, C3, C3, C4, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
	   [TR, C5, C5, C5, C5, C4, C5, C4, C4, C4, C4, C4, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
	   [TR, TR, TR, TR, C5, C5, C5, C5, C4, C5, C5, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]])

cloud.append([[TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C1, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, C1, C1, C1, C2, C2, C1, C1, C1, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, C2, C2, C2, C2, C2, C2, C2, C2, C2, C2, C1, C2, C1, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, C1, C1, C1, C2, C2, C2, C2, C3, C3, C3, C3, C2, C2, C2, C2, C2, C2, C1, C1, TR, TR, TR, TR, TR, TR, TR, TR],
              [TR, TR, TR, C1, C1, C2, C2, C2, C2, C2, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C2, C2, C2, C1, C1, C1, C1, C2, TR, TR, TR],
              [TR, C1, C1, C2, C2, C2, C3, C3, C2, C2, C3, C3, C3, C3, C2, C2, C2, C2, C3, C3, C2, C2, C2, C2, C2, C2, C2, C2, C2, TR, TR],
              [C4, C3, C3, C3, C3, C3, C3, C3, C3, C2, C2, C2, C3, C3, C2, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C2, C2, C2, C2, TR, TR],
              [C4, C4, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C5, TR],
              [C5, C4, C4, C4, C4, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4, C4, C4, C5],
              [C5, C5, C4, C4, C4, C4, C4, C4, C4, C4, C4, C3, C3, C4, C4, C3, C4, C3, C3, C3, C3, C3, C3, C3, C4, C4, C4, C5, C5, C5, C5],
              [TR, TR, C5, C5, C5, C5, C5, C5, C5, C4, C4, C4, C4, C4, C4, C3, C3, C4, C4, C3, C4, C4, C4, C4, C4, C4, C5, C5, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, C4, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C5, C5, C5, C5, C5, C5, C5, C5, C5, C5, C5, TR, TR, TR, TR, TR],
              [TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, C5, C5, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR, TR]])






def draw_pixel(screen, color, a, b, scale):
    pygame.draw.rect(screen, color, [a, b, scale, scale])


def draw_image(pixel_list, x, y, scale):

    a = x * scale
    b = y * scale
    
    for row in pixel_list:
        for color in row:
            if color != None:   
                draw_pixel(screen, color, a, b, scale)
            a += scale
        b += scale
        a = x * scale


def which_cloud(x, y, t, scale):
 
    if t == 0:
       draw_image(cloud[0], x, y, scale) 
    elif t == 1:
        draw_image(cloud[1], x, y, scale)
    elif t == 2:
        draw_image(cloud[2], x, y, scale)
    elif t == 3:
        draw_image(cloud[3], x, y, scale)


    
def which_snitch(x, y, scale, frame):
    if frame == 0:
        draw_image(snitch_a, x, y, scale)
    elif frame == 1 or frame == 7:
        draw_image(snitch_b, x, y, scale)
    elif frame == 2 or frame == 6:
        draw_image(snitch_c, x, y, scale)
    elif frame == 3:
        draw_image(snitch_d, x, y, scale)
    elif frame == 4:
        draw_image(snitch_e, x, y, scale)
    elif frame == 5:
        draw_image(snitch_f, x, y, scale)

    
clouds = []
for i in range(20):
    x = random.randrange(-10, width / scale * 3)
    y = random.randrange(-10, height / scale + 10)
    c_number = random.randint(0, (len(cloud) - 1))
    c_size = random.randint(2, 10)
    clouds.append([x, y, c_number, c_size])


harry = [[harry_left, 65, 37], [harry_main, 80, 12], [harry_right, 101, 17]]


snitch_x = 106
snitch_y = 4



# Game loop
done = False
ticks = 0
            
up = False
down = False
left = False
right = False

s_up = False
s_down = False
s_left = False
s_right = False

snitch_move = False
player_snitch = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                snitch_move = not snitch_move 
            elif event.key == pygame.K_p:
                player_snitch = not player_snitch

    
    state = pygame.key.get_pressed()

    up = state[pygame.K_w]
    down = state[pygame.K_s]
    left = state[pygame.K_a]
    right = state[pygame.K_d]

    s_up = state[pygame.K_UP]
    s_down = state[pygame.K_DOWN]
    s_left = state[pygame.K_LEFT]
    s_right = state[pygame.K_RIGHT]


    # Game logic (Check for collisions, update points, etc.)
    '''ticks'''
    frame = ticks // 5

    ticks += 1

    if ticks >= 40:
        ticks = 0

    
    '''clouds moving, respawning'''
    for c in clouds:
            c[0] -= 1 

            if c[0] < -30:
                c[0] = random.randrange(width / scale * 2, width / scale * 3)
                c[1] = random.randrange(-15, height / scale + 5)
                c[2] = random.randint(0, (len(cloud) - 1))
                c[3] = random.randint(2, 10)
                
    '''harry moving'''
    if up == True:
        for p in harry:
            p[2] -= 1 
    elif down == True:
        for p in harry:
            p[2] += 1 
    elif left == True:
        for p in harry:
            p[1] -= 1 
    elif right == True:
        for p in harry:
            p[1] += 1 

    '''play as snitch'''
    if player_snitch == True:
        if s_up == True:
            snitch_y -= 1 
        elif s_down == True:
            snitch_y += 1 
        elif s_left == True:
            snitch_x -= 1 
        elif s_right == True:
            snitch_x += 1

        if snitch_x < 0:
            snitch_x += 2 
        elif snitch_x > 150:
            snitch_x -= 2 
        elif snitch_y < 0:
            snitch_y += 2 
        elif snitch_y > 110:
            snitch_y -= 2
            
    '''snitch moving'''
    if snitch_move == True and ticks % 2 == 0:
        d_x = random.randint(-1, 1)
        d_y = random.randint(-1, 1)
    
        snitch_x += d_x
        snitch_y -= d_y

        if snitch_x < 0:
            snitch_x += 2 
        elif snitch_x > 160:
            snitch_x -= 2 
        elif snitch_y < 0:
            snitch_y += 2 
        elif snitch_y > 110:
            snitch_y -= 2 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SB)
    
    for c in clouds:
        which_cloud(c[0], c[1], c[2], c[3])
    
    for p in harry:
        draw_image(p[0], p[1], p[2], scale)


    which_snitch(snitch_x, snitch_y, scale, frame)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
