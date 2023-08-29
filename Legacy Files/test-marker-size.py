import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4]
y_data = [5, 7, 2, 8]
sizes1 = [20, 50, 80, 30]

plt.scatter(x_data, y_data, s=sizes1, label='Marker Group 1')
plt.legend()
plt.show()
