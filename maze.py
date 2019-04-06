#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Wonz
# 功能：迷宫

import pygame
import sys
import time
from pygame.locals import *
from random import randint, choice
import color


# 设置迷宫的大小
global room_m, room_n, room_size
room_m = 50
room_n = 35
room_size = 15 # 每个小房间的大小
steps = 0

# 设置屏幕宽度和高度为全局变量
global screen_width
screen_width = 800
global screen_height
screen_height = 600

class room():
    def __init__(self, x, y):
        self.walls = [True, True, True, True] # 初始化地图，小房间四周都是墙
        self.visited = False # 初始化小房间都未被访问过
        self.x = x
        self.y = y


    # 画迷宫
    def draw_room(screen, begin_point, walls, size, r_color):
        n = 0
        # 一个小房间的四面墙
        for wall in walls:
            x = begin_point[0] # 迷宫起点的 x 坐标
            y = begin_point[1] # 迷宫起点的 y 坐标
            n += 1
            if n == 1 and wall: # x → x + size 是墙
                pygame.draw.line(screen, r_color, (x, y), (x + size, y))
            if n == 2 and wall:
                pygame.draw.line(screen, r_color, (x + size, y), (x + size, y + size))
            if n == 3 and wall:
                pygame.draw.line(screen, r_color, (x + size, y + size), (x, y + size))
            if n == 4 and wall:
                pygame.draw.line(screen, r_color, (x, y + size), (x, y))


    # 生成迷宫地图
    def creat_map(m, n):
        room_list = [[0 for col in range(n)] for row in range(m)] # 二维数组: m*n
        for i in range(m):
            for j in range(n):
                room_list[i][j] = room(i, j)
        return room_list


    # 获取下一个房间
    def get_next_room(room_list, room):
        temp_rooms = {1: None,
                      2: None,
                      3: None,
                      4: None}
        temp_room_count = 0
        # 判断上下左右四个方向的小房间有没有被访问，没有的话就加入 temp_rooms[]
        if (not room.y - 1 < 0) and (not room_list[room.x][room.y - 1].visited): # 上边没被访问
            temp_rooms[1] = room_list[room.x][room.y - 1]
            temp_room_count += 1
        if (not room.x + 1 > room_m - 1) and (not room_list[room.x + 1][room.y].visited): # 右边
            temp_rooms[2] = room_list[room.x + 1][room.y]
            temp_room_count += 1
        if (not room.y + 1 > room_n - 1) and (not room_list[room.x][room.y + 1].visited): # 下边
            temp_rooms[3] = room_list[room.x][room.y + 1]
            temp_room_count += 1
        if (not room.x - 1 < 0) and (not room_list[room.x - 1][room.y].visited): # 左边
            temp_rooms[4] = room_list[room.x - 1][room.y]
            temp_room_count += 1

        if temp_room_count > 0:
            do = True
            while do:
                room_id = randint(1, 4) # 随机生成，指定某一边没有墙
                if temp_rooms[room_id]:
                    do = False
                    next_room = temp_rooms[room_id]
                    if room_id == 1:
                        room.walls[0] = 0  # 当前房间的上边没有墙
                        next_room.walls[2] = 0  # 上面房间的下边没有墙
                    if room_id == 2:
                        room.walls[1] = 0
                        next_room.walls[3] = 0
                    if room_id == 3:
                        room.walls[2] = 0
                        next_room.walls[0] = 0
                    if room_id == 4:
                        room.walls[3] = 0
                        next_room.walls[1] = 0
            return next_room
        else:
            return None


    # 创建迷宫
    def creat_migong(room_list, next_room, temp_yes_rooms=[]):
        while True:
            if next_room:
                # 下一房间未被访问
                if not next_room.visited:
                    next_room.visited = True
                    temp_yes_rooms.append(next_room)
                next_room = room.get_next_room(room_list, next_room)
            else:
                next_room = temp_yes_rooms.pop()  # 否则出栈
                if len(temp_yes_rooms) == 0:
                    break