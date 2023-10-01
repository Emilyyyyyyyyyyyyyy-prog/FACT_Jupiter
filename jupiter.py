import math
import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11  # гравитационная постоянная
M_earth = 5.974e24  # масса Земли
M_jupiter = 1.898e27  # масса Юпитера
M_sun = 1.989e30  # масса Солнца
T_earth = 23 * 3600 + 56 * 60 + 4  # период вращения Земли вокруг оси
r_start = (G * M_earth * T_earth ** 2 / (4 * math.pi ** 2)) ** (
        1 / 3)  # начальный радиус КА - геостационарная орбита вокруг земли
r_jup = 5.2026 * 1.496 * 10 ** 11
r_plut = 39.5182 * 1.496 * 10 ** 11

# (0, 0) - координаты Солнца
# все считаем гелиоцентрически
x, y = 0, 0  # координаты КА
x_j, y_j = 0, 0  # координаты Юпитера

dt = 0.01
m = 0  # масса КА

trace = []  # координаты точек для прорисовки графика


# v = np.array()

def dist(X, Y):  # расчёт расстояния до центра координат (Солнца)
    return (X ** 2 + Y ** 2) ** 0.5


def f_earth():  # сила гравитационного притяжения Земли
    return G * M_earth * m / ((x ** 2 + y ** 2) ** 0.5)


def f_jupiter():  # сила гравитационного притяжения Юпитера
    return G * M_jupiter * m / (dist(x - x_j, y - y_j) ** 2)


def f_sun():  # сила гравитационного притяжения Солнца
    return G * M_sun * m / (dist(x, y) ** 2)


def move():  # расчёт перемещения
    global v, x, y
    a = acc()
    v = speed(v, a)
    x += v[0] * math.sin(v[1]) * dt
    y += v[0] * math.cos(v[1]) * dt
    trace.append((t, x, y, dist()))
    return x, y
