# coding = utf-8

import sys
import pygame
import random
# 分数，及其使用的图片
score = 0
scoreT_img = [
    pygame.image.load(r'images\score\0.png'),
    pygame.image.load(r'images\score\1.png'),
    pygame.image.load(r'images\score\2.png'),
    pygame.image.load(r'images\score\3.png'),
    pygame.image.load(r'images\score\4.png'),
    pygame.image.load(r'images\score\5.png'),
    pygame.image.load(r'images\score\6.png'),
    pygame.image.load(r'images\score\7.png'),
    pygame.image.load(r'images\score\8.png'),
    pygame.image.load(r'images\score\9.png')
]
scoreU_img = [
    pygame.image.load(r'images\score\0.png'),
    pygame.image.load(r'images\score\1.png'),
    pygame.image.load(r'images\score\2.png'),
    pygame.image.load(r'images\score\3.png'),
    pygame.image.load(r'images\score\4.png'),
    pygame.image.load(r'images\score\5.png'),
    pygame.image.load(r'images\score\6.png'),
    pygame.image.load(r'images\score\7.png'),
    pygame.image.load(r'images\score\8.png'),
    pygame.image.load(r'images\score\9.png')
]


# 管道类
class Pipe:
    def __init__(self, coord_x, coord_y):
        # 设置管道的初始位置坐标
        self.coord_x = coord_x
        self.coord_y = coord_y
        # 设置上下管道的图片
        self.pipeB = pygame.image.load(r'images\pipe\g_pipe_b_160.png')
        self.pipeU = pygame.image.load(r'images\pipe\g_pipe_u_160.png')

        self.speed = 1

    # 管道向左移动，超出一定范围后，分数加一
    def move(self):
        self.coord_x -= self.speed

        global score

        if self.coord_x == -54:
            score += 1
        elif self.coord_x < -160:
            self.coord_x = 480
            self.coord_y = random.randint(144, 640)
        else:
            pass


# 小鸟类
class Bird:
    def __init__(self, coord_x, coord_y):
        # 设置小鸟的初始位置坐标
        self.coord_x = coord_x
        self.coord_y = coord_y
        # 小鸟是否死亡
        self.is_dead = False
        # 小鸟的飞行效果
        self.status = 0
        self.image = [
            pygame.image.load(r'images\bird\red_bird_0.png'),
            pygame.image.load(r'images\bird\red_bird_1.png'),
            pygame.image.load(r'images\bird\red_bird_2.png')
        ]
        # 小鸟是否在飞
        self.is_flying = False

    # 飞行移动
    def fly(self):
        if self.is_flying:
            self.coord_y -= 1
        else:
            self.coord_y += 1


if __name__ == '__main__':
    # 设置窗体尺寸
    size = width, height = 480, 640
    # 暂停标识
    is_paused = False
    # 结束标识
    is_end = False

    pygame.init()
    # 设置窗体尺寸、背景图片
    forms = pygame.display.set_mode(size)
    pygame.display.set_caption(r'Happy Bird')
    # 背景图片
    image = [
        pygame.image.load(r'images\background\bg_land.png'),
        pygame.image.load(r'images\background\bg_day.png'),
        pygame.image.load(r'images\background\bg_night.png'),
    ]
    # 设置一个黑底
    black = (0, 0, 0)

    # 创建管道、小鸟对象
    pipe = Pipe(480, 392)
    bird = Bird(116, 296)
    # 主循环
    while True:
        # 游戏开始
        while not bird.is_dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 加载背景图片
            forms.blit(image[1], (0, 0))
            # 加载管道图片
            forms.blit(pipe.pipeB, (pipe.coord_x, pipe.coord_y))
            forms.blit(pipe.pipeU, (pipe.coord_x, (pipe.coord_y - 784)))
            # 加载小鸟图片
            forms.blit(bird.image[bird.status], (bird.coord_x, bird.coord_y))
            # 管道向左移动，产生小鸟向前移动的效果
            pipe.move()
            # 小鸟振翅效果
            bird.status += 1

            if bird.status > 2:
                bird.status = 0
            # 键盘事件检测
            keys = pygame.key.get_pressed()
            # 如果输入 space 则小鸟飞起，否则下落；如果输入 p 则暂停；如果输入 e 则结束
            if keys[pygame.K_SPACE]:
                bird.is_flying = True
            elif keys[pygame.K_p]:
                is_paused = True
                break
            elif keys[pygame.K_e]:
                sys.exit()
            else:
                bird.is_flying = False
            # 小鸟飞翔
            bird.fly()
            # 碰撞检测
            pipeB_rect = pygame.Rect(pipe.coord_x, pipe.coord_y, 96, 640)
            pipeU_rect = pygame.Rect(pipe.coord_x, (pipe.coord_y - 784), 96, 640)
            bird_rect = pygame.Rect(116, bird.coord_y, 48, 48)

            if pipeU_rect.colliderect(bird_rect) or pipeB_rect.colliderect(bird_rect):
                bird.is_dead = True
                is_end = True
                break
            elif bird.coord_y == 0:
                bird.is_dead = True
                is_end = True
                break
            elif bird.coord_y == 592:
                bird.is_dead = True
                is_end = True
                break
            else:
                bird.is_dead = False
                is_end = False
            # 显示分数
            scoreT = score // 10
            scoreU = score % 10

            forms.blit(scoreT_img[scoreT], (216, 50))
            forms.blit(scoreU_img[scoreU], (240, 50))

            if scoreT > 1:
                pipe.speed = scoreT
            # 场景更新
            pygame.display.update()
        # 游戏暂停
        while is_paused:
            # 加载背景图片
            forms.blit(image[1], (0, 0))
            # 加载管道图片
            forms.blit(pipe.pipeB, (pipe.coord_x, pipe.coord_y))
            forms.blit(pipe.pipeU, (pipe.coord_x, (pipe.coord_y - 784)))
            # 加载小鸟图片
            forms.blit(bird.image[bird.status], (bird.coord_x, bird.coord_y))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 检测键盘事件
            keys = pygame.key.get_pressed()
            # 如果输入 r 则继续游戏；如果输入 e 则结束游戏
            if keys[pygame.K_r]:
                is_paused = False
                break
            elif keys[pygame.K_e]:
                sys.exit()
        # 游戏结束
        while is_end:
            # 加载背景图片
            forms.fill(black)
            forms.blit(image[0], (0, 528))
            # 显示分数
            scoreT = score // 10
            scoreU = score % 10

            forms.blit(scoreT_img[scoreT], (216, 50))
            forms.blit(scoreU_img[scoreU], (240, 50))
            # 加载小鸟图片
            forms.blit(bird.image[bird.status], (216, 264))

            pygame.display.update()
            # 设置小鸟飞行姿态
            bird.status += 1

            if bird.status > 2:
                bird.status = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 检测键盘事件
            keys = pygame.key.get_pressed()
            # 如果输入 s 则重置参数，并重新开始游戏
            if keys[pygame.K_s]:
                bird.is_dead = False
                bird.coord_x = 116
                bird.coord_y = 296
                pipe.coord_x = 480
                pipe.coord_y = 392
                score = 0

                break
            else:
                continue
