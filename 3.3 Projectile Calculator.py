import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print('Projectile calculator')

while True:
    angle = input('Enter initial angle (in deg): ')
    init_height = input('Enter initial height (in m): ')
    init_velocity = input('Enter initial velocity (in m/s): ')
    try:
        angle = float(angle)
        init_height = float(init_height)
        init_velocity = float(init_velocity)
        break
    except:
        hey = input('Uh-oh. Don\'t mess up with me.\n I know you have entered a weird thing.\nQuit? (y/n)')
        if hey == 'y':
            print('Alright.')
            quit()
       
# Initial horizontal/vertical velocity       
g = 9.8
vx = math.cos(math.radians(angle)) * init_velocity
vy1 = math.sin(math.radians(angle)) * init_velocity

# Going up
t1 = vy1 / g
h1 = g * ((t1)**2)/2
h_max = h1 + init_height

# Going down
t2 = math.sqrt(2 * h_max / g)
vy2 = t2 * g
fin_velocity = math.sqrt(((vy2)**2)+((vx)**2))
fin_angle = math.degrees(math.asin((vy2/fin_velocity)))
total_t = t1+t2
v_shift = total_t * vx
v_whenmax = t1 * vx

print('Provided data:',
'\nInitial angle:', round(angle, 2), 's',
'\nInitial height:', round (init_height, 2), 'm',
'\nInitial velocity:', round(init_velocity, 2), 'm/s')

print('\nResults:\nHorizontal velocity:', round(vx, 2), 'm/s',
'\nInitial vertical velocity:', round(vy1, 2), 'm/s',
'\nMaximum height object reaches:', round(h_max, 2), 'm',
'\nTime when reaching maximum height:', round(t1, 2), 's',
'\nHorizontal distance when reaching maximum height:', round(v_whenmax, 2), 'm',
'\nTotal time:', round(total_t, 2), 's',
'\nFinal velocity:', round(fin_velocity, 2), 's',
'\nFinal angle:', round(fin_angle, 2), 'º'
'\nHorizontal distance:', round(v_shift, 2), 'm')

print('\nHere is a vertical position vs. horizontal position graph of your projectile:')
x = np.linspace(0, v_shift)
temp = (0 - h_max) / ((v_shift - v_whenmax)**2) 
y = temp * ((x - v_whenmax)**2) + h_max

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()
