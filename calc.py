import matplotlib.pyplot as plt

import numpy as np

G = 6.67 * 10 ** (-11)
M_Earth = 5.97 * 10 ** 24
M_Sun = 2 * 10 ** 30
M_Jup = 1.899 * 10 ** 27

R_Earth = 6378.14 * 10 ** 3
r_Earth = 1.496 * 10 ** 11
r_Plut = 39.482 * r_Earth
r_Jup = 5.2043 * r_Earth
R_Jup = 71492 * 10 ** 3

r_start = 400 * 10 ** 3 + R_Earth  # геоцентрическая орбита
v0 = (G * M_Earth / r_start) ** 0.5
v_Earth = (G * M_Sun / r_Earth) ** 0.5
print(v0 / 1000, 'км/c')
v0_with = v0 + v_Earth
print(v0_with / 1000, 'км/c - начальная скорость (на гомановской орбите) КА')

a = (r_Plut + r_Earth) / 2
print(a / r_Earth)
v_p = (G * M_Sun * (2 / r_Earth - 1 / a)) ** 0.5
print(v_p / 1000, 'км/c')
print('добавка скорости: ', (v_p - v0_with) / 1000, 'км/c')
a1 = (r_Jup + r_Earth) / 2
print(a1 / r_Earth)
v1 = (G * M_Sun * (2 / r_Jup - 1 / a1)) ** 0.5
v1_real = (G * M_Sun * (2 / r_Jup - 1 / a)) ** 0.5
print(v1 / 1000, 'км/c - по гомановской в юпитер, ', v1_real / 1000, 'км/c - реально')

v_plut = (G * M_Sun / r_Plut) ** 0.5
print('скорость, чтобы плавно приземлиться на плутон, равна скорости плутона по орбите:', v_plut / 1000, 'км/c')
v_k_without = (G * M_Sun * (2 / r_Plut - 1 / a)) ** 0.5
print(v_k_without / 1000, 'км/c - скорость у плутона без маневра')
print('необходимая добавка скорости от маневра:', (v_plut - v_k_without) / 1000, 'км/c')

r_f_jup = r_Jup * (M_Jup / M_Sun) ** (2 / 5)
print('сфера действия Юпитера:', r_f_jup / r_Earth, 'а.е.')
a_g = 1 / (v1_real ** 2 / (G * M_Jup) - 2 / r_f_jup)
print('большая полуось гиперболы: ', a_g)
print('зависимость скорости на гиперболе от расстояния до фокуса: ')
list_d = []
list_v_d = []
for d in np.linspace(2 * R_Jup, a_g, 10):
    list_d.append(d)
    v_d = (G * M_Jup * (2 / d + 1 / a_g)) ** 0.5
    list_v_d.append(v_d)
    print(d / 1000, 'км,', v_d / 1000, 'км/c')
plt.plot(list_d, list_v_d)
# plt.show()
v_gr = v_d
a_new = 1 / (2 / r_Jup - v_gr ** 2 / (G * M_Sun))
v_k_with = (G * M_Sun * (2 / r_Plut - 1 / a_new)) ** 0.5
print(v_k_with / 1000, 'км/c')
