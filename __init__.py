import matplotlib.pyplot as plt
import numpy as np
import math


def plot_labeled(xy, l, opt='r+', label=None):
    for i in range(len(xy)):
        x = xy[i][0]
        y = xy[i][1]
        plt.plot((x,), (y,), opt)
        if l[i][1]:
            plt.text(x, y, l[i][0])
        if i == 0 and label is not None:
            plt.text(x, y + 2, label)

def f1(x):
    return math.log10(math.pi / x) + 9

def f2(x):
    return 2 * math.log10(x) - 6

def f3(x):
    return -math.log10(x) + 6

# Nomogram scale parameters
d1 = 4.
m2 = 5.
d2 = 0.2
m1 = 100.
if d1*m2 != d2*m1:
    print 'Nomogram is not scaled properly!'
x1 = -d1
x2 = 0
x3 = d2
y1 = m1
y2 = -(m1*m2) / (m1+m2)
y3 = m2

# Calculate coordinate positions and shifts
z1 = [[400 + 10*a, a % 10 == 0] for a in range(41)]
z2 = [[a * 10**b, a == 1 or a == 10] for a in range(1, 11) for b in range(-2, 1)]
z3 = [[a * 10**b, a == 1 or a == 10] for a in range(1, 11) for b in range(1, 5)]
s1 = f1(z1[len(z1) / 2][0])
s2 = f2(z2[len(z2) / 2][0])
s3 = f3(z3[len(z3) / 2][0])

# Make Plots
fig, ax = plt.subplots()
plot_labeled([[x1, y1*(f1(z[0]) - s1)] for z in z1], z1, opt='r_', label='$\lambda$ (nm)')
plot_labeled([[x2, y2*(f2(z[0]) - s2)] for z in z2], z2, opt='g_', label='Waist (mm)')
plot_labeled([[x3, y3*(f3(z[0]) - s3)] for z in z3], z3, opt='b_', label='$z_R$ ($\mu$m)')
plt.axis('off')
plt.show()
