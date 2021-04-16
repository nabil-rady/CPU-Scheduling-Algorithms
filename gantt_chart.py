# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt
from priority_p import priority_p 
  
# Declaring a figure "gnt"
fig, gnt = plt.subplots()
  
# Setting Y-axis limits
gnt.set_ylim(0, 1)

# test the gantt chart  
p1 = {'name': 'p1', 'arrival_time': 0, 'priority': 3, 'burst_time': 8}
p2 = {'name': 'p2', 'arrival_time': 1, 'priority': 4, 'burst_time': 2}
p3 = {'name': 'p3', 'arrival_time': 3, 'priority': 4, 'burst_time': 4}
p4 = {'name': 'p4', 'arrival_time': 4, 'priority': 5, 'burst_time': 1}
p5 = {'name': 'p5', 'arrival_time': 5, 'priority': 2, 'burst_time': 6}
p6 = {'name': 'p6', 'arrival_time': 6, 'priority': 6, 'burst_time': 5}
p7 = {'name': 'p7', 'arrival_time': 10, 'priority': 1, 'burst_time': 1}

results = priority_p([p1, p2, p3, p4, p5, p6, p7])



# Setting labels for x-axis and y-axis
gnt.set_xlabel('Time')
gnt.set_ylabel('Processes line')
  
# Setting ticks on x-axis
x_ticks = []

for i in range(1, len(results[2])):
    x_ticks.append(results[2][i])

gnt.set_xticks(x_ticks)
  
# Setting graph attribute
gnt.grid(True)

# colors
color = ['orange', 'red', 'green', 'blue', 'black', 'pink', 'gray', 'orange', 'red', 'green', 'blue', 'black', 'pink', 'gray']

# Declaring a bar in schedule
for i in range(len(results[1])):
    gnt.broken_barh([(results[2][i], results[2][i + 1])], (0, 1), facecolors =color[i])

  
plt.savefig("gantt_cahrt.png")