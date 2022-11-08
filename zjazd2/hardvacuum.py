'''
Fuzzy logic vacuum cleaner -

Programming Team : Oktawian Filipkowski, Maciej Zakrzewski
Expert : Bobik THE DOG

Antecedents:
    Surface: what is the difficulty level of the surface (0-10)
        * easy, moderate, hard
    Dirt: how much dirt on the surface (0-10)
        * light, moderate, heavy
    Brush speed: with what speed does brushes spin (0-10)
        * slow, medium, fast
Consequent:
    Suction: what level should be suction level set to (0-100)
        * low, medium, high
Rules:
    *If surface is easy, dirt light and brushes slow then suction will be low
    *If surface is easy, dirt moderate and brushes moderate then suction will be medium
    *If surface is easy, dirt heavy and brushes fast then suction will be high
    *If surface is moderate, dirt light and brushes slow then suction will be low
    *If surface is moderate, dirt moderate and brushes moderate then suction will be medium
    *If surface is moderate, dirt heavy and brushes fast then suction will be high
    *If surface is hard, dirt light and brushes slow then suction will be low
    *If surface is hard, dirt moderate and brushes moderate then suction will be medium
    *If surface is hard, dirt heavy and brushes fast then suction will be high
'''

'''
Importing essential libraries and creating variables
'''
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_surface = np.arange(0, 11, 1)
x_dirt = np.arange(0, 11, 1)
x_brush = np.arange(0, 11, 1)

x_suction = np.arange(0,101,1)

'''
implementing using np.arrays
'''
y_surface_easy = fuzz.trimf(x_surface, [0, 0, 5])
y_surface_moderate = fuzz.trimf(x_surface, [0, 5, 10])
y_surface_hard = fuzz.trimf(x_surface, [5, 10, 10])

y_dirt_light = fuzz.trimf(x_dirt, [0, 0, 5])
y_dirt_moderate = fuzz.trimf(x_dirt, [0, 5, 10])
y_dirt_heavy = fuzz.trimf(x_dirt, [5, 10, 10])

y_brush_slow = fuzz.trimf(x_brush, [0, 0, 5])
y_brush_medium = fuzz.trimf(x_brush, [0, 5, 10])
y_brush_fast = fuzz.trimf(x_brush, [5, 10, 10])

y_suction_low = fuzz.trimf(x_suction, [0, 0, 50])
y_suction_medium = fuzz.trimf(x_suction, [0, 50, 100])
y_suction_high = fuzz.trimf(x_suction, [50, 100, 100])

'''
defining inputs
'''
surface_num_easy = fuzz.interp_membership(x_surface,y_surface_easy, 0.0)
surface_num_moderate = fuzz.interp_membership(x_surface,y_surface_moderate, 0.0)
surface_num_hard = fuzz.interp_membership(x_surface,y_surface_hard, 0.0)

dirt_num_easy = fuzz.interp_membership(x_dirt,y_dirt_light, 0.0)
dirt_num_moderate = fuzz.interp_membership(x_dirt,y_dirt_moderate, 0.0)
dirt_num_hard = fuzz.interp_membership(x_dirt,y_dirt_heavy, 0.0)

brush_num_easy = fuzz.interp_membership(x_brush,y_brush_slow, 0.0)
brush_num_moderate = fuzz.interp_membership(x_brush,y_brush_medium, 0.0)
brush_num_hard = fuzz.interp_membership(x_brush,y_brush_fast, 0.0)

'''
defining the rules
'''
activate_rule1 = np.fmax(surface_num_easy, dirt_num_easy) and brush_num_easy
activation_suction_low = np.fmin(activate_rule1, y_suction_low)
activate_rule2 = np.fmax(surface_num_easy, dirt_num_moderate) and brush_num_moderate
activation_suction_medium = np.fmin(activate_rule2, y_suction_medium)
activate_rule3 = np.fmax(surface_num_easy, dirt_num_hard) and brush_num_hard
activation_suction_high = np.fmin(activate_rule3, y_suction_high)

activate_rule4 = np.fmax(surface_num_moderate, dirt_num_easy) and brush_num_easy
activation_suction_low = np.fmin(activate_rule4, y_suction_low)
activate_rule5 = np.fmax(surface_num_moderate, dirt_num_moderate) and brush_num_moderate
activation_suction_medium = np.fmin(activate_rule5, y_suction_medium)
activate_rule6 = np.fmax(surface_num_hard, dirt_num_hard) and brush_num_hard
activation_suction_high = np.fmin(activate_rule6, y_suction_high)

activate_rule7 = np.fmax(surface_num_hard, dirt_num_easy) and brush_num_easy
activation_suction_low = np.fmin(activate_rule7, y_suction_low)
activate_rule8 = np.fmax(surface_num_hard, dirt_num_moderate) and brush_num_moderate
activation_suction_medium = np.fmin(activate_rule8, y_suction_medium)
activate_rule9 = np.fmax(surface_num_hard, dirt_num_hard) and brush_num_hard
activation_suction_high = np.fmin(activate_rule9, y_suction_high)

'''
Creating visualization
'''
x_suction0 = np.zeros_like(x_suction)
x_suction.shape, x_suction0.shape
fig, ax = plt.subplots(figsize = (8,5))
ax.fill_between (x_suction, x_suction0, activation_suction_low, facecolor='r')
ax.plot(x_suction, y_suction_low, 'r')
ax.fill_between(x_suction, x_suction0, activation_suction_medium, facecolor='g')
ax.plot(x_suction, y_suction_medium, 'g')
ax.fill_between(x_suction, x_suction0, activation_suction_high, facecolor='b')
ax.plot(x_suction, y_suction_high, 'b')
plt.show()

'''
Creating deffuzification to verify results
'''
control = np.fmax(activation_suction_low,np.fmax(activation_suction_medium,activation_suction_medium))
suction = fuzz.defuzz(x_suction, control,'centroid')
print(suction)
suction_activation = fuzz.interp_membership(x_suction, control, suction)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_suction, y_suction_low, 'r')
ax.plot(x_suction, y_suction_medium, 'r')
ax.plot(x_suction, y_suction_high, 'r')
ax.fill_between(x_suction, x_suction0, control, facecolor='yellow')
ax.plot([suction,suction],[0, suction_activation], 'black')
ax.set_title('Defuzz')
plt.show()




