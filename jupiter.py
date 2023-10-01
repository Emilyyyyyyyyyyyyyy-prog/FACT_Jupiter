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
r_earth = 1 * 1.496 * 10 ** 11

# (0, 0) - координаты Солнца
# все считаем гелиоцентрически
x, y = 0, 0  # координаты КА
# x_j, y_j = 0, 0  # координаты Юпитера

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


# def move():  # расчёт перемещения
#     global v, x, y
#     a = acc()
#     v = speed(v, a)
#     x += v[0] * math.sin(v[1]) * dt
#     y += v[0] * math.cos(v[1]) * dt
#     trace.append((t, x, y, dist()))
#     return x, y

plt.figure(figsize=(10, 10))
# красным цветом показаны орбиты планет: Земля, Юпитер и Плутон
k = 1.496 * 10 ** 11
x_e1 = np.linspace(-1, 1, 100)
y_e1 = np.array([(1 - x_e_i ** 2) ** 0.5 for x_e_i in x_e1])
plt.plot(x_e1, y_e1, color="red")
x_e2 = np.linspace(-1, 1, 100)
y_e2 = np.array([-(1 - x_e_i ** 2) ** 0.5 for x_e_i in x_e2])
plt.plot(x_e2, y_e2, color="red")

x_j_1 = np.linspace(-(r_jup / k), (r_jup / k), 100)
y_j_1 = np.array([((r_jup / k) ** 2 - x_j_i ** 2) ** 0.5 for x_j_i in x_j_1])
plt.plot(x_j_1, y_j_1, color="red")
x_j_2 = np.linspace(-(r_jup / k), (r_jup / k), 100)
y_j_2 = np.array([-((r_jup / k) ** 2 - x_j_i ** 2) ** 0.5 for x_j_i in x_j_2])
plt.plot(x_j_2, y_j_2, color="red")

x_p_1 = np.linspace(-(r_plut / k), (r_plut / k), 100)
y_p_1 = np.array([((r_plut / k) ** 2 - x_p_i ** 2) ** 0.5 for x_p_i in x_p_1])
plt.plot(x_p_1, y_p_1, color="red")
x_p_2 = np.linspace(-(r_plut / k), (r_plut / k), 100)
y_p_2 = np.array([-((r_plut / k) ** 2 - x_p_i ** 2) ** 0.5 for x_p_i in x_p_2])
plt.plot(x_p_2, y_p_2, color="red")

# синим цветом показана гомановская орбита от Земли до Плутона
a = (r_plut + 2 * r_earth) / 2 / k
print(a)
q = r_earth / k
e = 1 - (q / a)
b = a * (1 - e) ** 0.5
y_g = np.linspace(-1, a, 100)
x_g = np.linspace(0, b, 100)
x_g1 = []
y_g1 = []
v = (a - 1)
u = 0.
pi = 3.1415
t = np.linspace(-pi / 2, pi / 2, 100)
gom = np.array([b * np.cos(t), a * np.sin(t)])
plt.plot(u + gom[0, :], v + gom[1, :])

plt.show()
