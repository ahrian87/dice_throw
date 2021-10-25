# sourcery skip: for-index-underscore
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Creating two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Making some rolls and adding the results to the list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Results analysis.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Results visualization.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Wynik", "dtick": 1}
y_axis_config = {"title": "Częstotliwość występowania wartości"}
my_layout = Layout(title="Wynik rzucania trzema kośćmi D6 tysiąc razy", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="3_d6.html")

