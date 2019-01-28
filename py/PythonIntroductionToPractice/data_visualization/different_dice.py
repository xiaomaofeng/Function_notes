from die import Die

import pygal

#create a D6 and a D10 dice
die_1 = Die()
die_2 = Die(10)

#roll dice several times, and storage in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#result visualization
hist = pygal.Bar()

hist.title = "Result of rolling a D6 and a D10 5,000 times"
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_labels = [value for value in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequencies"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')


