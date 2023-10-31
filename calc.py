G = 6.67 * 10 ** (-11)
M_Earth = 5.97 * 10 ** 24
M_Sun = 2 * 10 ** 30

R_Earth = 6378.14 * 10 ** 3
r_Earth = 1.496 * 10 ** 11
r_Plut = 39.482 * r_Earth
r_Jup = 5.2043 * r_Earth

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

