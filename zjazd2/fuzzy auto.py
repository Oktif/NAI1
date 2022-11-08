import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Creating antecedents and consequent according to categories:
distance: small, medium, big
speed: slow, average, fast
acceleration: small-, small+, big -, big +
light: green, yellow, red
'''
distance = ctrl.Antecedent(np.arange(0, 141, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 121, 1), 'speed')
light = ctrl.Antecedent(np.arange(0, 3, 1), 'light')

acceleration = ctrl.Consequent(np.arange(-1, 1.1, 0.001), 'acceleration')

'''
Generating membership degrees with charts to view them
'''
distance.automf(number=3, names=['small', 'medium', 'big'])
speed.automf(number=3, names=['slow', 'average', 'fast'])
light.automf(number=3, names=['Red', 'Yellow', 'Green'])

acceleration.automf(number=4, names=['small-', 'small+', 'big-', 'big+'])

#distance.view()
#speed.view()
#acceleration.view()
#distance['small'].view()

'''
Defining the rules
'''
acceleration['big-'] = fuzz.trapmf(acceleration.universe, [-1,-1, -0.4, 0])
acceleration['small-'] = fuzz.trimf(acceleration.universe, [-0.4, 0.1, 0.2])
acceleration['small+'] = fuzz.trimf(acceleration.universe, [-0.1, 0.1, 0.4])
acceleration['big+'] = fuzz.trapmf(acceleration.universe, [0, 0.4,1, 1])

'''For viewing only'''
distance['small'] = fuzz.trapmf(distance.universe, [0, 0, 30,45 ])
distance['medium'] = fuzz.trapmf(distance.universe, [20,50, 110, 140])
distance['big'] = fuzz.trapmf(distance.universe, [105,130, 140, 140])
#distance.view()
speed['slow'] = fuzz.trapmf(speed.universe, [0, 0, 15, 65])
speed['average'] = fuzz.trapmf(speed.universe, [15, 65, 65, 115])
speed['fast'] = fuzz.trapmf(speed.universe, [65,110, 120, 120])
#speed.view()
'''
Fuzzy functions - PI
'''
#acceleration['big-'] = fuzz.pimf(acceleration.universe, -1, -1, -0.5, 0)
#acceleration['small-'] = fuzz.pimf(acceleration.universe, -0.4, -0.4, 0, 0.25)
#acceleration['small+'] = fuzz.pimf(acceleration.universe, -0.1, -0.1, 0., 0.4)
#acceleration['big+'] = fuzz.pimf(acceleration.universe, 0, 0.4, 1, 1)
#acceleration.view()


rule1 = ctrl.Rule(distance['small'] & speed['slow'], acceleration['big-'])
rule2 = ctrl.Rule(distance['medium'] & speed['slow'], acceleration['small-'])
rule3 = ctrl.Rule(distance['big'] & speed['slow'], acceleration['small-'])
rule4 = ctrl.Rule(distance['small'] & speed['average'], acceleration['big+'])
rule5 = ctrl.Rule(distance['medium'] & speed['average'], acceleration['small-'])
rule6 = ctrl.Rule(distance['big'] & speed['average'], acceleration['small-'])
rule7 = ctrl.Rule(distance['small'] & speed['fast'], acceleration['small+'])
rule8 = ctrl.Rule(distance['medium'] & speed['fast'], acceleration['big-'])
rule9 = ctrl.Rule(distance['big'] & speed['fast'], acceleration['small-'])
'''
Example rule with light
'''
#rule10 = ctrl.Rule(distance['big'] & speed['slow'] & light['Red'], acceleration['small-'])

'''
Implementing control systems to perform the tests and fuzzy system for predictions
'''
control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fuzzy_system = ctrl.ControlSystemSimulation(control_system)

fuzzy_system.input['distance'] = 30
fuzzy_system.input['speed'] = 50
fuzzy_system.compute()

print(fuzzy_system.output['acceleration'])
acceleration.view(sim=fuzzy_system)




