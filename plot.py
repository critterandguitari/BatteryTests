import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('t.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='Voltage Level')
plt.xlabel('Voltage')
plt.ylabel('Seconds')
plt.title('Battery Level')
plt.legend()
plt.show()
