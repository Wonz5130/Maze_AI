# Maze_AI
## :ghost:一款基于 `Python` + `Pygame` + `AI算法` 的 `迷宫小游戏`

[![](https://img.shields.io/github/stars/Wonz5130/Maze_AI.svg)](https://github.com/Wonz5130/Maze_AI/stargazers) [![](https://img.shields.io/github/forks/Wonz5130/Maze_AI.svg)](https://github.com/Wonz5130/Maze_AI/network/members) [![](https://img.shields.io/github/issues/Wonz5130/Maze_AI.svg)](https://github.com/Wonz5130/Maze_AI/issues) [![](https://img.shields.io/github/license/Wonz5130/Maze_AI.svg)](https://github.com/Wonz5130/Maze_AI/blob/master/LICENSE)

### （一）课题内容
实现走迷宫。  
主要功能为界面显示、上下左右键的响应以及当前步数统计。  
通过该课题全面熟悉数组、字符串等的使用，掌握程序设计的基本方法及友好界面的设计。  

### （二）课题要求
##### 1. 基本要求
（1）游戏界面显示：迷宫地图、上下左右移动的特效。  
（2）动作选择：上下左右键对应于上下左右的移动功能，遇到障碍的处理。  
（3）得分统计功能：步数等。  

##### 2. 扩展要求
（1）用户数据管理。  
（2）设计一个自动走迷宫的程序，使得得到最短路径。

### （三）组队分工情况
##### 团队名称：import python
##### 队员：Wonz（没错就我一个人）
##### 分工：全部（好像给自己挖了个巨坑，嘤...嘤...哎...嘤不出来）

### （四）ToDo
- [ ] 10.29-10.30：学习 `PyQt5` + `Tkinter`  
- [ ] 10.31：学习 `Pygame`、熟悉 `Python`、实现随机生成迷宫地图程序  
- [ ] 11.1：实现游戏界面程序、得分统计功能程序  
- [ ] 11.2：学习 `Python` + `MySQL`，实现用户数据管理程序  
- [ ] 11.3-11.5：设计 `AI 算法`，实现自动走迷宫程序（DFS、BFS、强化学习、遗传算法）  

### （五）实际进度
- [x] 10.29：学习 `PyQt5`
- [x] 10.30：学习 `Tkinter`
- [x] 10.31：放弃 `PyQt5`、`Tkinter`，转 `Pygame`
- [x] 11.1：尝试实现迷宫地图程序
- [x] 11.2-11.3：实现迷宫地图程序
- [x] 11.4-11.6：生成角色、实现键盘控制走迷宫、实现计分功能，改障碍处理的 bug（改了三天）
- [x] 11.7：尝试实现 `遗传算法` 自动走迷宫，设置数据库连接
- [x] 11.8：放弃 `遗传算法` ，转向 `强化学习` 中的 `Deep Q Network` 实现自动走迷宫
- [x] 11.9：`Deep Q Network` 中的 `TensorFlow` 框架看不懂，放弃，转 `DFS`，验收
- [x] 11.10：实现人工生成迷宫地图，非随机生成
- [x] 11.11：3点睡，7点多起，一直写报告到下午5点

### （六）文件说明

* main.py为主函数
* maze.py为随机生成迷宫函数
* color.py为存储颜色函数
* main_new.py为被老师验收之后自己重写的主函数
* mapp.py为被老师验收之后自己重写的自己设计的迷宫（非随机生成迷宫）
* 由于时间等原因，第二种生成迷宫的AI算法还未实现

### （七）结果展示

##### 1. 随机生成地图版本

* 游戏界面

![](https://github.com/Wonz5130/Maze_AI/raw/master/img/%E6%B8%B8%E6%88%8F%E7%95%8C%E9%9D%A2.png)

* 开始游戏：左上角有步数统计

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E8%AE%B0%E6%AD%A5%E6%95%B0.png?1554527510971>)

* 遇到障碍的信息反馈

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E9%9A%9C%E7%A2%8D%E5%8F%8D%E9%A6%88.png?1554527532798>)

* AI自动走迷宫（程序还有待完善，步数统计存在问题）

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/AI%E8%87%AA%E5%8A%A8%E8%B5%B0%E8%BF%B7%E5%AE%AB.png?1554527553844>)

* 存在的问题：有时 AI 程序会崩溃，暂时还没有找到 bug

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E6%B8%B8%E6%88%8F%E5%A5%94%E6%BA%83%E6%88%AA%E5%9B%BE.png?1554527574840>)

##### 2. 非随机生成地图的迷宫

* 游戏界面：起点在最右边，终点在最左边红色位置

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E6%96%B0%E6%B8%B8%E6%88%8F%E7%95%8C%E9%9D%A2(%E9%9D%9E%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E5%9C%B0%E5%9B%BE).png?1554527590212>)

* 开始游戏：左上角有步数统计

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E6%96%B0%E8%AE%B0%E6%AD%A5%E6%95%B0(%E9%9D%9E%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E5%9C%B0%E5%9B%BE).png?1554527613266>)

* 遇到障碍的信息反馈

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E6%96%B0%E9%9A%9C%E7%A2%8D%E5%8F%8D%E9%A6%88(%E9%9D%9E%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E5%9C%B0%E5%9B%BE).png?1554527628476>)

* 走出迷宫：输出“Win”

![](<https://github.com/Wonz5130/Maze_AI/raw/master/img/%E8%B5%B0%E5%87%BA%E8%BF%B7%E5%AE%AB.png?1554527645787>)

### （八）不足与反思

- 基础不扎实：选了不是很熟悉的 Python 语言，期间复习语法也花了点时间
- 自己给自己挖坑：拒绝了同学们的组队邀请，一个人做三个人的任务，结果做不好
- 时间管理不够高效：进度安排不够科学，总是完不成自己规定的任务
- 需求不明确：确实是自己没有问清楚老师的需求，导致自己的程序老师不满意，是自己的问题