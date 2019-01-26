import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
#plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
#set chart title and label the coordinate axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

#set tick parameters
plt.tick_params(axis='both', which='major', labelsize=14)

#set the range of axis
plt.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('squares_plot.png')