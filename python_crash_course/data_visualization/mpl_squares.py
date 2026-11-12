import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=5)
#ax.scatter(x_values, y_values, color='red', s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()