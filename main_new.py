#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Wonz
# 功能：由自己设计的迷宫（非随机生成）

import pygame
import sys
import random
import time
from pygame.locals import *
from random import randint, choice
import mapp
import color


# 设置屏幕宽度和高度为全局变量
global screen_width
screen_width = 800
global screen_height
screen_height = 800
room_size = 15 # 每个房间的大小
steps = 0


# 输出文本信息
def print_text(font, x, y, text, color, shadow=True):
    if shadow:
        imgText = font.render(text, True, (0, 0, 0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))


# 存储迷宫
r_list = mapp.map_list


# 游戏开始
if __name__ == '__main__':
    # 初始化 Pygame
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Maze_AI——by Wonz')
    global font1, font2, font3

    clock = pygame.time.Clock()
    fps = 20
    screen.fill(color.White)


    # 加载角色照片
    user = pygame.image.load("user.png").convert_alpha()
    width, height = user.get_size()
    user = pygame.transform.smoothscale(user, (8, 8))
    # draw the user
    width, height = user.get_size()
    x = 25 + 42 * room_size
    y = 25 + 9 * room_size
    roomx = 42
    roomy = 9
    screen.blit(user, (x, y))


    # 画迷宫
    for i in range(43):
        for j in range(42):
            if (r_list[j][i] == 3):
                pygame.draw.circle(screen, color.Red, [30 + i * room_size, 30 + j * room_size], 5, 0)
                pygame.display.flip()
                r_list[j][i] = 0
            elif (r_list[j][i] == 1):
                # 画10*10的矩形，线宽为1，这里不能是0，因为10*10无空白区域
                pygame.draw.rect(screen, color.Black, [25 + i * room_size, 25 + j * room_size, 10, 10], 0)
                pygame.display.flip()
            elif (r_list[j][i] == 0):
                pygame.draw.rect(screen, color.White, [25 + i * room_size, 25 + j * room_size, 10, 10], 1)
                pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 走到终点
            elif(roomx == 0 and roomy == 9):
                font3 = pygame.font.Font(None, 32)
                print_text(font3, 350, 350, "Win", color.Red)
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 右边无墙
                    if(0 <= roomx < 42 and 0 <= roomy <= 41 and r_list[roomy][roomx+1] == 0):
                        x += room_size
                        roomx += 1 # 计房间数
                        steps += 1 # 计步
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25)) # x:25 y:0 width:200 height:25
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x-room_size, y, 10, 10))
                        screen.blit(user, (x, y))
                    # 右边有墙
                    elif (0 <= roomx < 42 and 0 <= roomy <= 41 and r_list[roomy][roomx+1] == 1):
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_LEFT:
                    # 左边无墙
                    if (0 < roomx <= 42 and 0 <= roomy <= 41 and r_list[roomy][roomx-1] == 0):
                        x -= room_size
                        roomx -= 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x+room_size, y, 10, 10))
                        screen.blit(user, (x, y))
                    # 左边有墙
                    elif (0 < roomx <= 42 and 0 <= roomy <= 41 and r_list[roomy][roomx-1] == 1):
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_UP:
                    # 上边无墙
                    if (0 <= roomx <= 42 and 0 < roomy <= 41 and r_list[roomy-1][roomx] == 0):
                        y -= room_size
                        roomy -= 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x, y+room_size, 10, 10))
                        screen.blit(user, (x, y))
                    # 上边有墙
                    elif (0 <= roomx <= 42 and 0 < roomy <= 41 and r_list[roomy-1][roomx] == 1):
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_DOWN:
                    # 下边无墙
                    if (0 <= roomx <= 42 and 0 <= roomy < 41 and r_list[roomy+1][roomx] == 0):
                        y += room_size
                        roomy += 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x, y-room_size, 10, 10))
                        screen.blit(user, (x, y))
                    # 下边无墙
                    elif (0 <= roomx <= 42 and 0 <= roomy < 41 and r_list[roomy+1][roomx] == 1):
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))


        # 更新屏幕
        pygame.display.update()