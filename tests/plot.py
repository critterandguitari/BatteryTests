import matplotlib.pyplot as plt
import csv
import sys

x = []
y = []

label1 = ''
label2 = ''

plot_file =  sys.argv[1]

with open(plot_file,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    row_num = 0
    for row in plots:
        if row_num == 0 :
            label1 = str(row[0])
        elif row_num == 1 :
            label2 = str(row[0])
        else :
            x.append(float(row[0]))
            y.append(float(row[1]))
        row_num = row_num + 1

plt.plot(x,y, label='Battery Level')
plt.xlabel('Seconds')
plt.ylabel('Voltage')
plt.title( label1 + '\n' + label2 )
plt.legend()
plt.show()
