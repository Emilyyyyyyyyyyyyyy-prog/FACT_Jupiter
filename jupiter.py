import numpy

import math
import numpy as np
import matplotlib.pyplot as plt
import time

# pygame.init()
# screen = pygame.display.set_mode((1200, 640))
# run = True

G = 6.67e-11  # гравитационная постоянная
M_earth = 5.974e24  # масса Земли
M_jupiter = 1.898e27  # масса Юпитера
M_sun = 1.989e30  # масса Солнца
T_earth = 23 * 3600 + 56 * 60 + 4  # период вращения Земли вокруг оси
T_jup = 11.862  # период обращения Юпитера вокруг Солнца в годах
r_start = (G * M_earth * T_earth ** 2 / (4 * math.pi ** 2)) ** (
        1 / 3)  # начальный радиус КА - геостационарная орбита вокруг земли
r_jup = 5.2026 * 1.496 * 10 ** 11
r_plut = 39.5182 * 1.496 * 10 ** 11
r_earth = 1 * 1.496 * 10 ** 11
k = 1.496 * 10 ** 11

k_r = (M_sun / M_jupiter) ** 0.5  # точка Лагранжа Юпитер-Солнце

global x_j, y_j
x_j, y_j = 0, r_jup / k
x, y = 0, r_earth / k

# (0, 0) - координаты Солнца
# все считаем гелиоцентрически
coord_ka = (0, r_earth / k)  # координаты КА
coord_jup = (0, r_jup / k)  # координаты Юпитера - необходимо найти маленьким школьникам

trace = []  # координаты точек для прорисовки графика

pos_vel = np.ndarray(shape=(500000, 4), dtype=float)
pos_vel[0] = np.array([r_earth, 0, 0, 0])
time = np.ndarray(shape=(500000,), dtype=float)
dtime = 5
m = 10000  # масса КА


def r_sun(X, Y):  # расчёт расстояния до центра координат (Солнца)
    return (X ** 2 + Y ** 2) ** 0.5


def f_earth():  # сила гравитационного притяжения Земли
    return G * M_earth * m / ((x ** 2 + y ** 2) ** 0.5)


def f_jupiter():  # сила гравитационного притяжения Юпитера
    return G * M_jupiter * m / (r_sun(x - x_j, y - y_j) ** 2)


def f_sun():  # сила гравитационного притяжения Солнца
    return G * M_sun * m / (r_sun(x, y) ** 2)


def maneuver():  # если сила притяжения Юпитера становится больше, чем Солнца, начинается гравитационный маневр
    if f_jupiter() > f_sun():
        return True
    else:
        return False


#
# def move_jupiter():
#     dx_jup = dtime / T_jup * r_jup / k
#     dy_jup = ((r_jup / k) ** 2 - dx_jup ** 2) ** 0.5
#     if x_j + dx_jup >= r_jup / k:
#         x_j -= dx_jup
#     else:
#         x_j += dx_jup
#
#     if y_j + dy_jup >= r_jup / k:
#         y_j -= dy_jup
#     else:
#         y_j += dy_jup


def dist_vecs(a, b):  # расстояние между векторами
    return np.norm(a - b, ord=4)


def ang_vecs(a, b):  # угол между векторами
    return numpy.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def where_jupiter(time):
    fas_0 = ang_vecs((x, y), (x_j, y_j))
    return r_jup * np.array(
        [np.cos(fas_0 + time / T_jup), np.sin(fas_0 + time / T_jup)])


def accel(pos_vel, isOn):  # ускорение КА
    pos_norm = np.linalg.norm(pos_vel[:2])
    vel_norm = np.linalg.norm(pos_vel[2:])


def move():  # главная функция движения
    pass


# def move():  # расчёт перемещения
#     global v, x, y
#     a = acc()
#     v = speed(v, a)
#     x += v[0] * math.sin(v[1]) * dt
#     y += v[0] * math.cos(v[1]) * dt
#     trace.append((t, x, y, dist()))
#     return x, y

f1, ax1 = plt.subplots()
# f2, ax2 = plt.subplots()

# красным цветом показаны орбиты планет: Земля, Юпитер и Плутон
x_e1 = np.linspace(-1, 1, 100)
y_e1 = np.array([(1 - x_e_i ** 2) ** 0.5 for x_e_i in x_e1])
ax1.plot(x_e1, y_e1, color="red")
x_e2 = np.linspace(-1, 1, 100)
y_e2 = np.array([-(1 - x_e_i ** 2) ** 0.5 for x_e_i in x_e2])
ax1.plot(x_e2, y_e2, color="red")

x_j_1 = np.linspace(-(r_jup / k), (r_jup / k), 100)
y_j_1 = np.array([((r_jup / k) ** 2 - x_j_i ** 2) ** 0.5 for x_j_i in x_j_1])
ax1.plot(x_j_1, y_j_1, color="red")
x_j_2 = np.linspace(-(r_jup / k), (r_jup / k), 100)
y_j_2 = np.array([-((r_jup / k) ** 2 - x_j_i ** 2) ** 0.5 for x_j_i in x_j_2])
ax1.plot(x_j_2, y_j_2, color="red")

x_p_1 = np.linspace(-(r_plut / k), (r_plut / k), 100)
y_p_1 = np.array([((r_plut / k) ** 2 - x_p_i ** 2) ** 0.5 for x_p_i in x_p_1])
ax1.plot(x_p_1, y_p_1, color="red")
x_p_2 = np.linspace(-(r_plut / k), (r_plut / k), 100)
y_p_2 = np.array([-((r_plut / k) ** 2 - x_p_i ** 2) ** 0.5 for x_p_i in x_p_2])
ax1.plot(x_p_2, y_p_2, color="red")

# синим цветом показана гомановская орбита от Земли до Плутона
a = (r_plut + r_earth) / 2 / k
q = r_earth / k
e = 1 - (q / a)
b = a * (1 - e) ** 0.5
v = (a - 1)
u = 0.
pi = np.pi
t = np.linspace(-pi / 2, pi / 2, 50)
gom = np.array([b * np.cos(t), a * np.sin(t)])
ax1.plot(u + gom[0, :], v + gom[1, :], color="blue")
ax1.scatter(u + gom[0, :], v + gom[1, :], color="blue", marker="*")

#  зеленым цветом показана траектория с применением гравитационного маневра
a = (r_plut + r_earth) / 2 / k
q = r_earth / k
e = 1 - (q / a)
b = a * (1 - e ** 2) ** 0.5
x_j_ = (a / (b - a) * (b - (r_jup / k) ** 2)) ** 0.5
y_j_ = ((r_jup / k) ** 2 - x_j_ ** 2) ** 0.5
v = (a - 1)
u = 0.
pi = 3.1415
alpha = math.atan(x / y)
print(alpha, pi / 3.7)
t = np.linspace(-pi / 2, -pi / 3.7, 100)
gom = np.array([b * np.cos(t), a * np.sin(t)])
# ax1.plot(u + gom[0, :], v + gom[1, :], color="green")
# формула для гиперболы: x**2 / a**2 - y**2 / b**2 = 1
# гипербола рисуется из списка координат траектории КА
# x_g = np.linspace(-6, 6, 100)
# y_g = a * np.sqrt((x_g ** 2 / b ** 2) - 1)
# plt.plot(x_g, y_g, 'b')
# plt.plot(x_g, -y_g, 'b')
plt.show()

# отдельный график, показывающий маневр
# x_j_b = np.linspace(-r_jup / k, r_jup / k, 100)
# y_j_b_up = np.array([((r_jup / k) ** 2 - x_j_b[i] ** 2) ** 0.5 for i in range(len(x_j_b))])
# y_j_b_down = np.array([-((r_jup / k) ** 2 - x_j_b[i] ** 2) ** 0.5 for i in range(len(x_j_b))])
# ax2.plot(x_j_b, y_j_b_up, color='red')
# ax2.plot(x_j_b, y_j_b_down, color='red')
# print(x_j_b)
# print(y_j_b_up)
# print(y_j_b_down)

# plt.show()

# анимация гравитационного маневра
# start_move = False
# x_j_now = x_j
# y_j_now = y_j
# dx = 0.5
# dy = ((r_jup / k) ** 2 - dx ** 2) ** 0.5
# while run:
#     time.sleep(dt)
#     if start_move:
#         screen.fill((255, 255, 255))
#         pygame.draw.circle(screen, (0, 0, 0), (0, 0), r_jup / k)
#         pygame.draw.circle(screen, (255, 0, 0), (x_j_now, y_j_now), 0.5)
#         if x_j_now + dx >= r_jup / k:
#             x_j_now -= dx
#         elif x_j_now - dx <= 0:
#             x_j_now += dx
#         else:
#             x_j_now += dx
#         y_j_now = ((r_jup / k) ** 2 - x_j_now ** 2) ** 0.5
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYDOWN:
#             start_move = True
#     pygame.display.update()
#
