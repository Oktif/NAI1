'''
Fuzzy logic vacuum cleaner - it supports the decision making to set the suction power
by rules depending on external factors.

Programming Team : Oktawian Filipkowski, Maciej Zakrzewski
Expert : Ex wife

To run program install:
pip install scikit-fuzzy
pip install matplotlib

Antecedents (inputs):
    Surface: what is the difficulty level of the surface (0-5 in our world example)
        *In our fuzzy set: easy, moderate, hard
    Dirt: how much dirt on the surface (0-5 in our world example)
        *In our fuzzy set: light, moderate, heavy
    Brush speed: with what speed does brushes spin (0-1)
        *In our fuzzy set: slow, fast
Consequent (outputs):
    Suction: what level should be suction level set to (0-10)
        *low, medium, high, very high
Rules:
    *If surface is easy, dirt light and brushes slow then suction will be low
    *If surface is easy, dirt moderate and brushes slow then suction will be low
    *If surface is easy, dirt heavy and brushes slow then suction will be medium
    *If surface is moderate, dirt light and brushes slow then suction will be low
    *If surface is moderate, dirt moderate and brushes slow then suction will be medium
    *If surface is moderate, dirt heavy and brushes fast then suction will be high
    *If surface is hard, dirt light and brushes slow then suction will be medium
    *If surface is hard, dirt moderate and brushes fast then suction will be high
    *If surface is hard, dirt heavy and brushes fast then suction will be very high
'''

'''
Importing essential libraries and creating variables
'''
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

surface = ctrl.Antecedent(np.arange(0, 3, 1), 'surface')
dirt = ctrl.Antecedent(np.arange(0, 3, 1), 'dirt')
brush = ctrl.Antecedent(np.arange(0, 2, 1), 'brush')

suction = ctrl.Consequent(np.arange(0, 11, 1), 'suction')

'''
Creating Membership functions
'''
surface.automf(number=3, names=['easy', 'moderate', 'hard'])
dirt.automf(number=3, names=['light', 'moderate', 'heavy'])
brush.automf(number=2, names=['slow', 'fast'])


suction['low'] = fuzz.trimf(suction.universe, [0, 0, 4])
suction['medium'] = fuzz.trimf(suction.universe, [0, 4, 8])
suction['high'] = fuzz.trimf(suction.universe, [4, 8, 8])
suction['very_high'] = fuzz.trimf(suction.universe, [5, 10, 10])

'''
Creating rules
'''
rule1 = ctrl.Rule(surface['easy'] & dirt['light'] & brush['slow'], suction['low'])
rule2 = ctrl.Rule(surface['easy'] & dirt['moderate'] & brush['slow'], suction['low'])
rule3 = ctrl.Rule(surface['easy'] & dirt['heavy'] & brush['fast'], suction['medium'])
rule4 = ctrl.Rule(surface['moderate'] & dirt['light'] & brush['slow'], suction['low'])
rule5 = ctrl.Rule(surface['moderate'] & dirt['moderate'] & brush['slow'], suction['medium'])
rule6 = ctrl.Rule(surface['moderate'] & dirt['heavy'] & brush['fast'], suction['high'])
rule7 = ctrl.Rule(surface['hard'] & dirt['light'] & brush['slow'], suction['medium'])
rule8 = ctrl.Rule(surface['hard'] & dirt['moderate'] & brush['fast'], suction['high'])
rule9 = ctrl.Rule(surface['hard'] & dirt['heavy'] & brush['fast'], suction['very_high'])

'''
Creating control system with inputs and output
'''
control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fuzzy_system = ctrl.ControlSystemSimulation(control_system)

fuzzy_system.input['surface'] = 0
fuzzy_system.input['dirt'] = 2
fuzzy_system.input['brush'] = 1
fuzzy_system.compute()
print(fuzzy_system.output['suction'])
suction.view(sim=fuzzy_system)