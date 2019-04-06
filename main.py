#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Wonz
# 功能：主程序

import pygame
import sys
import random
import time
from pygame.locals import *
from random import randint, choice
import maze
import color


# 设置屏幕宽度和高度为全局变量
global screen_width
screen_width = 800
global screen_height
screen_height = 600


# 输出文本信息
def print_text(font, x, y, text, color, shadow=True):
    if shadow:
        imgText = font.render(text, True, (0, 0, 0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))


# 游戏开始
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Maze_AI——by Wonz') # 游戏标题
    global font1, font2, font3, font4 # 文字


    clock = pygame.time.Clock()
    fps = 20
    screen.fill(color.White)


    r_list = maze.room.creat_map(maze.room_m, maze.room_n)
    begin_point = [0, 0]
    begin_room = r_list[0][0]
    maze.room.creat_migong(r_list, begin_room)
    # 画出去起点和终点的其他点
    for i in range(maze.room_m):
        for j in range(maze.room_n):
            begin_point[0] = 25 + i * maze.room_size
            begin_point[1] = 25 + j * maze.room_size
            r_color = color.Black
            maze.room.draw_room(screen, begin_point, r_list[i][j].walls, maze.room_size, r_color)
    # 画起点
    maze.room.draw_room(screen, [25, 25], [0, 0, 0, 1], maze.room_size, color.White)
    # 画终点
    maze.room.draw_room(screen, [25 + (maze.room_m - 1) * maze.room_size, 25 + (maze.room_n - 1) * maze.room_size],
                        [0, 1, 0, 0], maze.room_size, color.White)


    # 加载角色照片
    user = pygame.image.load("user.png").convert_alpha()
    width,height = user.get_size()
    user = pygame.transform.smoothscale(user, (8,8))
    # 画角色
    width, height = user.get_size()
    x = 27
    y = 30
    roomx = 0
    roomy = 0
    screen.blit(user, (x, y))


    # 键盘控制角色移动
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 走到终点
            elif(roomx == maze.room_m-1 and roomy == maze.room_n-1):
                font4 = pygame.font.Font(None, 32)
                print_text(font4, 350, 350, "Win" , color.Red)
                break
            # 键盘响应，只取按“→”键作为例子，“↑”、“↓”、“←”类似，只要改改参数即可
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 右边无墙
                    if(r_list[roomx][roomy].walls[1] == False):
                        x += maze.room_size
                        roomx += 1 # 计房间数
                        maze.steps += 1 # 计步
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25)) # x:25 y:0 width:200 height:25
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x-15,y,10,10))
                        screen.blit(user, (x, y))
                    # 右边有墙
                    elif (r_list[roomx][roomy].walls[1] == True):
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))  # x:25 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_LEFT:
                    # 左边无墙
                    if (r_list[roomx][roomy].walls[3] == False):
                        x -= maze.room_size
                        roomx -= 1
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x+15,y,10,10))
                        screen.blit(user, (x, y))
                    # 左边有墙
                    elif (r_list[roomx][roomy].walls[3] == True):
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_UP:
                    # 上边无墙
                    if (r_list[roomx][roomy].walls[0] == False):
                        y -= maze.room_size
                        roomy -= 1
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x,y+15,10,10))
                        screen.blit(user, (x, y))
                    # 上边有墙
                    elif (r_list[roomx][roomy].walls[0] == True):
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))

                elif event.key == pygame.K_DOWN:
                    # 下边无墙
                    if (r_list[roomx][roomy].walls[2] == False):
                        y += maze.room_size
                        roomy += 1
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        pygame.display.flip()
                        screen.fill(color.White, (x,y-15,10,10))
                        screen.blit(user, (x, y))
                    # 下边无墙
                    elif (r_list[roomx][roomy].walls[2] == True):
                        maze.steps += 1
                        font1 = pygame.font.Font(None, 32)
                        font2 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(maze.steps), color.Black)
                        print_text(font2, 350, 0, "This is a wall!", color.Black)
                        pygame.display.flip()
                        screen.blit(user, (x, y))


            # 鼠标响应，执行 AI 程序
            elif event.type == pygame.MOUSEBUTTONUP:
                font3 = pygame.font.Font(None, 32)
                print_text(font3, 750, 0, "AI", color.Red)
                pygame.display.flip()
                start_x = 0
                start_y = 0
                steps = 0
                for i in range(1000000000):
                    if (start_x == maze.room_m-1 and start_y == maze.room_n-1):
                        font4 = pygame.font.Font(None, 32)
                        print_text(font4, 350, 350, "Win", color.Red)
                        break
                    d = random.randint(1,4)
                    # 上边无墙
                    if (d == 1 and 0 <= start_x <= maze.room_m - 1 and 0 <= start_y <= maze.room_n - 1 and
                            r_list[start_x][start_y].walls[0] == False): # 在迷宫地图范围内且上边无墙
                        start_y -= 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))  # x:25 y:0 width:200 height:25
                        screen.fill(color.White, (300, 0, 200, 25))  # x:300 y:0 width:200 height:25
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black) # 步数统计
                        pygame.display.flip()
                        screen.blit(user, ((start_x+2) * maze.room_size, (start_y+2) * maze.room_size))
                    # 右边无墙
                    if (d == 2 and 0 <= start_x <= maze.room_m - 1 and 0 <= start_y <= maze.room_n - 1 and
                            r_list[start_x][start_y].walls[1] == False):
                        start_x += 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.blit(user, ((start_x+2) * maze.room_size, (start_y+2) * maze.room_size))
                    # 下边无墙
                    if (d == 3 and 0 <= start_x <= maze.room_m - 1 and 0 <= start_y <= maze.room_n - 1 and
                            r_list[start_x][start_y].walls[2] == False):
                        start_y += 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.blit(user, ((start_x+2) * maze.room_size, (start_y+2) * maze.room_size))
                    # 左边无墙
                    if (d == 4 and 0 <= start_x <= maze.room_m - 1 and 0 <= start_y <= maze.room_n - 1 and
                            r_list[start_x][start_y].walls[3] == False):
                        start_x -= 1
                        steps += 1
                        font1 = pygame.font.Font(None, 32)
                        screen.fill(color.White, (25, 0, 200, 25))
                        screen.fill(color.White, (300, 0, 200, 25))
                        print_text(font1, 25, 0, "Steps:" + str(steps), color.Black)
                        pygame.display.flip()
                        screen.blit(user, ((start_x+2) * maze.room_size, (start_y+2) * maze.room_size))


        # 更新屏幕
        pygame.display.update()