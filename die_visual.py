# sourcery skip: for-index-underscore
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Creating a D6 die.
die = Die()

# Making some rolls and adding the results to the list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Results analysis.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Results visualization.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Wynik"}
y_axis_config = {"title": "Częstotliwość występowania wartości"}
my_layout = Layout(title="Wynik rzucania pojedynczą kością D6 tysiąc razy", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
