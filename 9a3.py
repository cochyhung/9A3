import os, colorama, random, pystyle
import requests
from colorama import *
from pystyle import *
from math import *
import turtle
from turtle import * 
red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET
loading_banner = rf"""





                                         {lred}                         __
                                         {lred}           ---_ ...... _/_ -
                                         {lred}          /  .      ./ .'*\ \
                                         {lred}          : '         /__-'   \.
                                         {lred}         /                      )     
                                         {lred}       _/                  >   .'     
                                         {lred}     /   '   .       _.-" /  .'      
                                         {white}     \           __/"     /.'      
                                         {white}       \ '--  .-" /     //'          
                                         {white}        \|  \ | /     //      
                                         {white}          `\/     //
                                         {white}           \__`\/ /                    
                                         {white}               \_|{reset}

"""
def anhyeuem():
  d1 = ["anh yeu em"]
  for dong1 in d1:
          for a in dong1:
            print(Colorate.Vertical(Colors.purple_to_red, f'''{a}''', True), end='', flush = True)
            time.sleep(0.4)
def loading_b():
  for _ in range(10):
    clears()
    print(f"{loading_banner}", end= ' ')
    time.sleep(0.4)
def ayee():
   print(Colorate.Vertical(Colors.blue_to_purple, f'''
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣤⣶⣶⣾⣿⣿⣿⣿⣿⣷⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠀⠀⠀⠘⠛⠛⠛⣻⣿⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣿⣿⣶⣶⣶⠀⠀⠀⢰⣶⣶⣶⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠀⠀⠀⠘⠛⠛⠋⠁⠀

Facebook: https://wwwfacebook.com/chh2k8.business⠀⠀⠀⠀⠀
   ''', True), end=' ')
def aye():
   print(Colorate.Vertical(Colors.blue_to_purple, f'''
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠙⠿⠿⠛⠉⣠⣾⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⠟⠁⢀⣠⣄⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡇
⠈⣿⣿⣿⣿⣟⣥⣶⣾⣿⣿⣿⣷⣦⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
messenger: https://m.me/chh2k8.business
   ''', True), end=' ')
def clears():
    os.system ('cls' if os.name == 'nt' else 'clear')
def anhthichem():
  for s in range(10):
    clears()
    print(Colorate.Vertical(Colors.purple_to_red, f'''
 ▄▄▄·  ▐ ▄  ▄ .▄    ▄▄▄▄▄ ▄ .▄▪   ▄▄·  ▄ .▄    ▄▄▄ .• ▌ ▄ ·. 
▐█ ▀█ •█▌▐███▪▐█    •██  ██▪▐███ ▐█ ▌▪██▪▐█    ▀▄.▀··██ ▐███▪
▄█▀▀█ ▐█▐▐▌██▀▐█     ▐█.▪██▀▐█▐█·██ ▄▄██▀▐█    ▐▀▀▪▄▐█ ▌▐▌▐█·
▐█ ▪▐▌██▐█▌██▌▐▀     ▐█▌·██▌▐▀▐█▌▐███▌██▌▐▀    ▐█▄▄▌██ ██▌▐█▌
 ▀  ▀ ▀▀ █▪▀▀▀ ·     ▀▀▀ ▀▀▀ ·▀▀▀·▀▀▀ ▀▀▀ ·     ▀▀▀ ▀▀  █▪▀▀▀
   ''', True), end=' ')
def fc():
   print('hiii')
def emdongy():
  for s in range(10):
    clears()
    print(Colorate.Vertical(Colors.purple_to_red, f'''
▄▄▄ .• ▌ ▄ ·.     ·▄▄▄▄         ▐ ▄  ▄▄ •      ▄· ▄▌
▀▄.▀··██ ▐███▪    ██▪ ██ ▪     •█▌▐█▐█ ▀ ▪    ▐█▪██▌
▐▀▀▪▄▐█ ▌▐▌▐█·    ▐█· ▐█▌ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄    ▐█▌▐█▪
▐█▄▄▌██ ██▌▐█▌    ██. ██ ▐█▌.▐▌██▐█▌▐█▄▪▐█     ▐█▀·.
 ▀▀▀ ▀▀  █▪▀▀▀    ▀▀▀▀▀•  ▀█▄▀▪▀▀ █▪·▀▀▀▀       ▀ • 
   ''', True), end=' ')
def lamnianhnhe():
  for s in range(10):
    clears()
    print(Colorate.Vertical(Colors.purple_to_red, f'''
▄▄▌   ▄▄▄· • ▌ ▄ ·.      ▐ ▄  ▄· ▄▌     ▄▄▄·  ▐ ▄  ▄ .▄     ▐ ▄  ▄ .▄▄▄▄ .
██•  ▐█ ▀█ ·██ ▐███▪    •█▌▐█▐█▪██▌    ▐█ ▀█ •█▌▐███▪▐█    •█▌▐███▪▐█▀▄.▀·
██▪  ▄█▀▀█ ▐█ ▌▐▌▐█·    ▐█▐▐▌▐█▌▐█▪    ▄█▀▀█ ▐█▐▐▌██▀▐█    ▐█▐▐▌██▀▐█▐▀▀▪▄
▐█▌▐▌▐█ ▪▐▌██ ██▌▐█▌    ██▐█▌ ▐█▀·.    ▐█ ▪▐▌██▐█▌██▌▐▀    ██▐█▌██▌▐▀▐█▄▄▌
.▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀    ▀▀ █▪  ▀ •      ▀  ▀ ▀▀ █▪▀▀▀ ·    ▀▀ █▪▀▀▀ · ▀▀▀ 
   ''', True), end=' ')
def quynhhuong():
  for s in range(10):
    clears()
    print(Colorate.Vertical(Colors.purple_to_red, f'''
.▄▄▄  ▄• ▄▌ ▄· ▄▌ ▐ ▄  ▄ .▄     ▄ .▄▄• ▄▌       ▐ ▄  ▄▄ • 
▐▀•▀█ █▪██▌▐█▪██▌•█▌▐███▪▐█    ██▪▐██▪██▌▪     •█▌▐█▐█ ▀ ▪
█▌·.█▌█▌▐█▌▐█▌▐█▪▐█▐▐▌██▀▐█    ██▀▐██▌▐█▌ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄
▐█▪▄█·▐█▄█▌ ▐█▀·.██▐█▌██▌▐▀    ██▌▐▀▐█▄█▌▐█▌.▐▌██▐█▌▐█▄▪▐█
·▀▀█.  ▀▀▀   ▀ • ▀▀ █▪▀▀▀ ·    ▀▀▀ · ▀▀▀  ▀█▄▀▪▀▀ █▪·▀▀▀▀ 
   ''', True), end=' ')

colora = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
]
developer = '''
 ▄▄·        ▄▄·      ▄ .▄ ▄· ▄▌     ▄ .▄▄• ▄▌ ▐ ▄  ▄▄ • 
▐█ ▌▪▪     ▐█ ▌▪    ██▪▐█▐█▪██▌    ██▪▐██▪██▌•█▌▐█▐█ ▀ ▪
██ ▄▄ ▄█▀▄ ██ ▄▄    ██▀▐█▐█▌▐█▪    ██▀▐██▌▐█▌▐█▐▐▌▄█ ▀█▄
▐███▌▐█▌.▐▌▐███▌    ██▌▐▀ ▐█▀·.    ██▌▐▀▐█▄█▌██▐█▌▐█▄▪▐█
·▀▀▀  ▀█▄▀▪·▀▀▀     ▀▀▀ ·  ▀ •     ▀▀▀ · ▀▀▀ ▀▀ █▪·▀▀▀▀ 
'''
helpp = '''
user - ex. cochyhung
iloveyou - python turtle love
love - name of love banner
clear - clear screen
ip - show your ip
connect - show connecting to server
online - online user
alluser - all user use

'''
def love():
  import random
from math import sin, cos, pi, log
from tkinter import *

CANVAS_WIDTH = 640  
CANVAS_HEIGHT = 480  
CANVAS_CENTER_X = CANVAS_WIDTH / 2  
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2  
IMAGE_ENLARGE = 11  
HEART_COLOR = "#f76070"  #chỉnh màu ở đây

def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):

    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    x *= shrink_ratio
    y *= shrink_ratio

 
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):

    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())

    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def shrink(x, y, ratio):
 
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)  
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def curve(p):
  
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class Heart:
  

    def __init__(self, generate_frame=20):
        self._points = set()  
        self._edge_diffusion_points = set()  
        self._center_diffusion_points = set()  
        self.all_points = {}  
        self.build(2000)

        self.random_halo = 1000

        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
    
        for _ in range(number):
            t = random.uniform(0, 2 * pi)  
            x, y = heart_function(t)
            self._points.add((x, y))

       
        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))

    
        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520) 

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calc(self, generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi)  

        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

        all_points = []

      
        heart_halo_point = set()  
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)  
            x, y = heart_function(t, shrink_ratio=11.6)  
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
           
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

  
        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

      
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)

  
clears()
print(Colorate.Vertical(Colors.purple_to_red, f'''
▄• ▄▌.▄▄ · ▄▄▄ .▄▄▄   ▐ ▄  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .
█▪██▌▐█ ▀. ▀▄.▀·▀▄ █·•█▌▐█▐█ ▀█ ·██ ▐███▪▀▄.▀·
█▌▐█▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄
▐█▄█▌▐█▄▪▐█▐█▄▄▌▐█•█▌██▐█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌
 ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ 
   ''', True), end=' ')
user = input('username: ' )
def inputf():
    print(Colorate.Vertical(Colors.purple_to_red, f'''
  ╔═══[9A3[BETA]@{user}]
  ╚══> ''', True), end=' ')
    
    return input().strip().lower()
#r = requests
#ip = r.post("http://fsystem88.ru/ip").text #thank u fsystem))

global all
hinh = f'''






               ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
             ▄▀░░░░░░░░░░░░▄░░░░░░░▀▄
             █░░▄░░░░▄░░░░░░░░░░░░░░█
             █░░░░░░░░░░░░▄█▄▄░░▄░░░█ ▄▄▄
      ▄▄▄▄▄  █░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██
      ██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██
       ▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██                          █████╗  █████╗ ██████╗
         ▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██                         ██╔══██╗██╔══██╗╚════██╗
            ▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██                         ╚██████║███████║ █████╔╝
            ▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀                           ╚═══██║██╔══██║ ╚═══██╗
           █▀▀█████████▀▀▀▀████████████▀                             █████╔╝██║  ██║██████╔╝
            ████▀  ███▀      ▀███  ▀██▀                              ╚════╝ ╚═╝  ╚═╝╚═════╝

welcome username: {user}
please wait for connect to server 9A3
connecting: {Fore.RED}True'''
alluser = '''
- total user -
cochyhung - Cóc Hy Hùng (Developer)
phamvandiem - Phạm Văn Điểm
leanhtuyet - Lê Ánh Tuyết
phuonghoangvu - Phương Hoàng Vũ
buikieuoanh - Bùi Kiều Oanh
nguyenthihongtrang - Nguyễn Thị Hồng Trang
minhyen - Minh Yến
buithihuong - Bùi Thị Hương
kimngan - Nguyễn Thị Kim Ngân
trankieuthuytrang - Trần Kiều Thuỳ Trang
vophamhaidang - Võ Phạm Hải Đăng
thaihuukien - Thái Hữu Kiên
'''
phamvandiem = '''
 ▄▄▄· ▄ .▄ ▄▄▄· • ▌ ▄ ·.      ▌ ▐· ▄▄▄·  ▐ ▄     ·▄▄▄▄  ▪  ▄▄▄ .• ▌ ▄ ·. 
▐█ ▄███▪▐█▐█ ▀█ ·██ ▐███▪    ▪█·█▌▐█ ▀█ •█▌▐█    ██▪ ██ ██ ▀▄.▀··██ ▐███▪
 ██▀·██▀▐█▄█▀▀█ ▐█ ▌▐▌▐█·    ▐█▐█•▄█▀▀█ ▐█▐▐▌    ▐█· ▐█▌▐█·▐▀▀▪▄▐█ ▌▐▌▐█·
▐█▪·•██▌▐▀▐█ ▪▐▌██ ██▌▐█▌     ███ ▐█ ▪▐▌██▐█▌    ██. ██ ▐█▌▐█▄▄▌██ ██▌▐█▌
.▀   ▀▀▀ · ▀  ▀ ▀▀  █▪▀▀▀    . ▀   ▀  ▀ ▀▀ █▪    ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀
'''
thaihuukien = '''
▄▄▄▄▄ ▄ .▄ ▄▄▄· ▪       ▄ .▄▄• ▄▌▄• ▄▌    ▄ •▄ ▪  ▄▄▄ . ▐ ▄ 
•██  ██▪▐█▐█ ▀█ ██     ██▪▐██▪██▌█▪██▌    █▌▄▌▪██ ▀▄.▀·•█▌▐█
 ▐█.▪██▀▐█▄█▀▀█ ▐█·    ██▀▐██▌▐█▌█▌▐█▌    ▐▀▀▄·▐█·▐▀▀▪▄▐█▐▐▌
 ▐█▌·██▌▐▀▐█ ▪▐▌▐█▌    ██▌▐▀▐█▄█▌▐█▄█▌    ▐█.█▌▐█▌▐█▄▄▌██▐█▌
 ▀▀▀ ▀▀▀ · ▀  ▀ ▀▀▀    ▀▀▀ · ▀▀▀  ▀▀▀     ·▀  ▀▀▀▀ ▀▀▀ ▀▀ █▪
'''
phuonghoangvu = '''
 ▄▄▄· ▄ .▄▄• ▄▌       ▐ ▄  ▄▄ •      ▄ .▄       ▄▄▄·  ▐ ▄  ▄▄ •      ▌ ▐·▄• ▄▌
▐█ ▄███▪▐██▪██▌▪     •█▌▐█▐█ ▀ ▪    ██▪▐█▪     ▐█ ▀█ •█▌▐█▐█ ▀ ▪    ▪█·█▌█▪██▌
 ██▀·██▀▐██▌▐█▌ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄    ██▀▐█ ▄█▀▄ ▄█▀▀█ ▐█▐▐▌▄█ ▀█▄    ▐█▐█•█▌▐█▌
▐█▪·•██▌▐▀▐█▄█▌▐█▌.▐▌██▐█▌▐█▄▪▐█    ██▌▐▀▐█▌.▐▌▐█ ▪▐▌██▐█▌▐█▄▪▐█     ███ ▐█▄█▌
.▀   ▀▀▀ · ▀▀▀  ▀█▄▀▪▀▀ █▪·▀▀▀▀     ▀▀▀ · ▀█▄▀▪ ▀  ▀ ▀▀ █▪·▀▀▀▀     . ▀   ▀▀▀ 
'''
hongtrang = '''
 ▄ .▄       ▐ ▄  ▄▄ •     ▄▄▄▄▄▄▄▄   ▄▄▄·  ▐ ▄  ▄▄ • 
██▪▐█▪     •█▌▐█▐█ ▀ ▪    •██  ▀▄ █·▐█ ▀█ •█▌▐█▐█ ▀ ▪
██▀▐█ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄     ▐█.▪▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
██▌▐▀▐█▌.▐▌██▐█▌▐█▄▪▐█     ▐█▌·▐█•█▌▐█ ▪▐▌██▐█▌▐█▄▪▐█
▀▀▀ · ▀█▄▀▪▀▀ █▪·▀▀▀▀      ▀▀▀ .▀  ▀ ▀  ▀ ▀▀ █▪·▀▀▀▀  xinh cá
'''
leanhtuyet = '''
▄▄▌  ▄▄▄ .     ▄▄▄·  ▐ ▄  ▄ .▄    ▄▄▄▄▄▄• ▄▌ ▄· ▄▌▄▄▄ .▄▄▄▄▄
██•  ▀▄.▀·    ▐█ ▀█ •█▌▐███▪▐█    •██  █▪██▌▐█▪██▌▀▄.▀·•██  
██▪  ▐▀▀▪▄    ▄█▀▀█ ▐█▐▐▌██▀▐█     ▐█.▪█▌▐█▌▐█▌▐█▪▐▀▀▪▄ ▐█.▪
▐█▌▐▌▐█▄▄▌    ▐█ ▪▐▌██▐█▌██▌▐▀     ▐█▌·▐█▄█▌ ▐█▀·.▐█▄▄▌ ▐█▌·
.▀▀▀  ▀▀▀      ▀  ▀ ▀▀ █▪▀▀▀ ·     ▀▀▀  ▀▀▀   ▀ •  ▀▀▀  ▀▀▀ 
'''
buikieuoanh = '''
▄▄▄▄· ▄• ▄▌▪      ▄ •▄ ▪  ▄▄▄ .▄• ▄▌           ▄▄▄·  ▐ ▄  ▄ .▄
▐█ ▀█▪█▪██▌██     █▌▄▌▪██ ▀▄.▀·█▪██▌    ▪     ▐█ ▀█ •█▌▐███▪▐█
▐█▀▀█▄█▌▐█▌▐█·    ▐▀▀▄·▐█·▐▀▀▪▄█▌▐█▌     ▄█▀▄ ▄█▀▀█ ▐█▐▐▌██▀▐█
██▄▪▐█▐█▄█▌▐█▌    ▐█.█▌▐█▌▐█▄▄▌▐█▄█▌    ▐█▌.▐▌▐█ ▪▐▌██▐█▌██▌▐▀
·▀▀▀▀  ▀▀▀ ▀▀▀    ·▀  ▀▀▀▀ ▀▀▀  ▀▀▀      ▀█▄▀▪ ▀  ▀ ▀▀ █▪▀▀▀ ·
'''
buithihuong =  '''
▄▄▄▄· ▄• ▄▌▪      ▄▄▄▄▄ ▄ .▄▪       ▄ .▄▄• ▄▌       ▐ ▄  ▄▄ • 
▐█ ▀█▪█▪██▌██     •██  ██▪▐███     ██▪▐██▪██▌▪     •█▌▐█▐█ ▀ ▪
▐█▀▀█▄█▌▐█▌▐█·     ▐█.▪██▀▐█▐█·    ██▀▐██▌▐█▌ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄
██▄▪▐█▐█▄█▌▐█▌     ▐█▌·██▌▐▀▐█▌    ██▌▐▀▐█▄█▌▐█▌.▐▌██▐█▌▐█▄▪▐█
·▀▀▀▀  ▀▀▀ ▀▀▀     ▀▀▀ ▀▀▀ ·▀▀▀    ▀▀▀ · ▀▀▀  ▀█▄▀▪▀▀ █▪·▀▀▀▀ 
'''
minhyen = '''
• ▌ ▄ ·. ▪   ▐ ▄  ▄ .▄ ▄ .▄     ▄· ▄▌▄▄▄ . ▐ ▄  ▐ ▄ 
·██ ▐███▪██ •█▌▐███▪▐███▪▐█    ▐█▪██▌▀▄.▀·•█▌▐█•█▌▐█
▐█ ▌▐▌▐█·▐█·▐█▐▐▌██▀▐███▀▐█    ▐█▌▐█▪▐▀▀▪▄▐█▐▐▌▐█▐▐▌
██ ██▌▐█▌▐█▌██▐█▌██▌▐▀██▌▐▀     ▐█▀·.▐█▄▄▌██▐█▌██▐█▌
▀▀  █▪▀▀▀▀▀▀▀▀ █▪▀▀▀ ·▀▀▀ ·      ▀ •  ▀▀▀ ▀▀ █▪▀▀ █▪
'''
trankieuthuytrang = '''
▄▄▄▄▄ ▄ .▄▄• ▄▌ ▄· ▄▌    ▄▄▄▄▄▄▄▄   ▄▄▄·  ▐ ▄  ▄▄ • 
•██  ██▪▐██▪██▌▐█▪██▌    •██  ▀▄ █·▐█ ▀█ •█▌▐█▐█ ▀ ▪
 ▐█.▪██▀▐██▌▐█▌▐█▌▐█▪     ▐█.▪▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
 ▐█▌·██▌▐▀▐█▄█▌ ▐█▀·.     ▐█▌·▐█•█▌▐█ ▪▐▌██▐█▌▐█▄▪▐█
 ▀▀▀ ▀▀▀ · ▀▀▀   ▀ •      ▀▀▀ .▀  ▀ ▀  ▀ ▀▀ █▪·▀▀▀▀ 
'''
kimngan = '''
▄ •▄ ▪  • ▌ ▄ ·.      ▐ ▄  ▄▄ •  ▄▄▄·  ▐ ▄ 
█▌▄▌▪██ ·██ ▐███▪    •█▌▐█▐█ ▀ ▪▐█ ▀█ •█▌▐█
▐▀▀▄·▐█·▐█ ▌▐▌▐█·    ▐█▐▐▌▄█ ▀█▄▄█▀▀█ ▐█▐▐▌
▐█.█▌▐█▌██ ██▌▐█▌    ██▐█▌▐█▄▪▐█▐█ ▪▐▌██▐█▌
·▀  ▀▀▀▀▀▀  █▪▀▀▀    ▀▀ █▪·▀▀▀▀  ▀  ▀ ▀▀ █▪
'''
vophamhaidang = '''
 ▄ .▄ ▄▄▄· ▪      ·▄▄▄▄   ▄▄▄·  ▐ ▄  ▄▄ • 
██▪▐█▐█ ▀█ ██     ██▪ ██ ▐█ ▀█ •█▌▐█▐█ ▀ ▪
██▀▐█▄█▀▀█ ▐█·    ▐█· ▐█▌▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
██▌▐▀▐█ ▪▐▌▐█▌    ██. ██ ▐█ ▪▐▌██▐█▌▐█▄▪▐█
▀▀▀ · ▀  ▀ ▀▀▀    ▀▀▀▀▀•  ▀  ▀ ▀▀ █▪·▀▀▀▀ 
'''
chh = '''
 █████╗  █████╗ ██████╗                 (c).-.(c)
██╔══██╗██╔══██╗╚════██╗                 | ._. |
╚██████║███████║ █████╔╝               __\( Y )/
 ╚═══██║██╔══██║ ╚═══██╗              (_.-/'-'\-._)
 █████╔╝██║  ██║██████╔╝                 || H ||
 ╚════╝ ╚═╝  ╚═╝╚═════╝                _.' `-' '._ 
                                      (.-./`-'\.-.)
                                       `-'     `-'
----------------------------------------------------------
developer: Coc Hy Hung and ...
'''
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(random.randint(10, 20)):
     os.system('cls' if os.name == 'nt' else 'clear')
     print(Style.RESET_ALL + random.choice(colora) + hinh)
     time.sleep(1)
def bom():
    clears()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clears()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clears()
    print(f'''
     / **/|        
     | == /        
      |  |                  
    ''')
    time.sleep(0.6)
    clears()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(random.randint(40, 50)):
     os.system('cls' if os.name == 'nt' else 'clear')
     print(Style.RESET_ALL + random.choice(colora) + hinh)
     time.sleep(1)
b = True
if b == True:
    import time
    os.system('cls' if os.name == 'nt' else 'clear')
    #banner()
    loading_b()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, f'''
    {chh}
 '''), True), end='')
    print(f'{Style.RESET_ALL + Fore.BLUE}my computer Windows ' if os.name == 'nt' else ('my computer linux'))
    if user == 'cochyhung':
        print(f'you are admin: {user}')
    else:
        print(f'you are member: {user}')
    while True:
      inp = inputf()
      if inp == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        clears()
        print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, f'''
        {chh}
       '''), True), end='')
      elif inp == 'love':
        names = input('name: ')
        while True:
         for i in range(9999):
          os.system ('cls' if os.name == 'nt' else 'clear')
          print(f'''{Style.RESET_ALL+random.choice(colora)}
________0000000000000________0000000000000_________
______00000000_____00000___000000_____00000000_____
____0000000_____________000______________000000____
___0000000_______________0_________________00000___
__000000____________________________________00000__
__00000____________ {names} _____________00000_
_00000_________________ DEV  _______________00000__
_00000_____________________________________000000__
__000000_________________________________0000000___
___0000000______________________________0000000____
_____000000____________________________000000______
_______000000________________________000000________
__________00000_____________________0000___________
_____________0000_________________0000_____________
_______________0000_____________000________________
_________________000_________000___________________
_________________ __000_____00_____________________
______________________00__00_______________________
________________________00_________________________
>------------------------------------------------->
        '''+Style.RESET_ALL)
         time.sleep(0.05)
         ia = input()
      elif inp == 'bom':
        clears()
        bom()
      elif inp == 'ip':
        print(f'{Fore.BLUE}check connecting: ...')
        r = requests
        ip = r.post("http://fsystem88.ru/ip").text #thank u fsystem))
        print(f'{Fore.BLUE}connecting [high speed]:{Fore.RED} True')
        print(Back.GREEN+"Your ip: {}".format(ip)+Style.RESET_ALL)
        print(Back.GREEN+"Your ip is sent to the server." + Style.RESET_ALL)
      elif inp == 'admin':
        if user == 'cochyhung':
            maso = '26122008'
            print(f'{Fore.GREEN}you are admin')
            print('admin id' + maso)
        else:
            print(f'{Fore.RED}you not admin')
      elif inp == 'developer':
        clears()
        print(Colorate.Vertical(Colors.purple_to_red, f'''
{developer}
   ''', True), end=' ')
      elif inp == 'phamvandiem':
        if user == 'phamvandiem':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{phamvandiem}
   ''', True), end=' ')
        else:
          print('you are not phamvandiem')
      elif inp == 'thaihuukien':
        if user == 'thaihuukien':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{thaihuukien}
   ''', True), end=' ')
        else:
          print('you are not thaihuukien')
      elif inp == 'phuonghoangvu':
        if user == 'phuonghoangvu':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{phuonghoangvu}
   ''', True), end=' ')
        else:
          print('you are not phuonghoangvu')
      elif inp == 'nguyenthihongtrang':
        if user == 'nguyenthihongtrang':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{hongtrang}
   ''', True), end=' ')
        else:
          print('you are not nguyenthihongtrang')
      elif inp == 'leanhtuyet':
        if user == 'leanhtuyet':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{leanhtuyet}
   ''', True), end=' ')
        else:
          print('you are not leanhtuyet')
      elif inp == 'buikieuoanh':
        if user == 'buikieuoanh':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{buikieuoanh}
   ''', True), end=' ')
        else:
          print('you are not buikieuoanh')
      elif inp == 'connect':
        print(f"{Fore.BLUE} connect security:{Fore.RED} True")
      elif inp == 'iloveyou':
        if __name__ == '__main__':
         root = Tk()  
         canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
         canvas.pack()
         heart = Heart()  
        draw(root, canvas, heart)  
        root.mainloop()
      elif inp == 'help':
        clears()
        print(Colorate.Vertical(Colors.purple_to_red, f'''
{helpp}
   ''', True), end=' ')
      elif inp == 'online':
        clears()
        print(Colorate.Vertical(Colors.purple_to_red, f'''
{user}
   ''', True), end=' ')
      elif inp == 'alluser':
        clears()
        print(Colorate.Vertical(Colors.purple_to_red, f'''
{alluser}
   ''', True), end=' ')
      elif inp == 'minhyen':
        if user == 'minhyen':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{minhyen}
   ''', True), end=' ')
        else:
          print('you are not minhyen')
      elif inp == 'buithihuong':
        if user == 'buithihuong':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{buithihuong}
   ''', True), end=' ')
        else:
          print('you are not buithihuong')
      elif inp == 'trankieuthuytrang':
        if user == 'trankieuthuytrang':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{trankieuthuytrang}
   ''', True), end=' ')
      elif inp == 'nguyenthikimngan':
        if user == 'nguyenthikimngan':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{kimngan}
   ''', True), end=' ')
        else:
          print('you are not nguyenthikimngan')
      elif inp == 'vophamhaidang':
        if user == 'vophamhaidang':
         clears()
         print(Colorate.Vertical(Colors.purple_to_red, f'''
{vophamhaidang}
   ''', True), end=' ')
        else:
          print('you are not vophamhaidang')
      elif inp == 'turtle':
        turtlep()
      elif inp == 'totinh':
        clears()
        anhthichem()
        time.sleep(2)
        emdongy()
        time.sleep(2)
        lamnianhnhe()
        time.sleep(2)
        quynhhuong()
        time.sleep(5)
        if __name__ == '__main__':
         root = Tk()  
         canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
         canvas.pack()
         heart = Heart()  
        draw(root, canvas, heart)  
        root.mainloop()
      elif inp == 'allname':
        fc()
      elif inp == 'discord':
                clears()
                print(f'''{lcyan}
                               
             ░░░░░░        ░░░░░
          ░░░░░░░░░░░░░░░░░░░░░░░░░          {magenta}Watermelon Discord Server{lcyan}
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░  
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        {lwhite}Join my discord server for:{lcyan}
       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       ░░░░░░░░░▒▒░░░░░░░░░▒▒▒░░░░░░░░░       {lwhite}- Get help or report a bug about the tool.{lcyan}
      ░░░░░░░░▒▒▒▒▒▒░░░░░▒▒▒▒▒▒░░░░░░░░       {lwhite}- Stay up to date with my projects.{lcyan}
      ░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒░░░░░░░░       {lwhite}- You can also talk to me through the server.{lcyan}
      ░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░
      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      {lred}> {lwhite}Server link: {lred}discord.gg/ewPyW4Ghzj{lcyan}
      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
         ░░░░░░░             ░░░░░░░
             ░░                ░\n''')
      elif inp == 'aye':
        clears()
        anhyeuem()
        clears()
        aye()
      elif inp == 'facebook':
        clears()
        ayee()
      else:
        print('what is command you use?')
       
