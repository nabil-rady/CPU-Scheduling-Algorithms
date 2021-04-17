# Use this file to test 
from algorithms.roundrobin import roundrobin
from algorithms.priority_np import priority_np
from algorithms.priority_p import priority_p
from algorithms.FCFS import FCFS
from gantt_chart import gantt_chart

# processes
# p1 = {'name': 'p1', 'arrival_time': 0, 'priority': 2, 'burst_time': 3}
# p2 = {'name': 'p2', 'arrival_time': 2, 'priority': 6, 'burst_time': 5}
# p3 = {'name': 'p3', 'arrival_time': 1, 'priority': 3, 'burst_time': 4}
# p4 = {'name': 'p4', 'arrival_time': 4, 'priority': 5, 'burst_time': 2}
# p5 = {'name': 'p5', 'arrival_time': 6, 'priority': 7, 'burst_time': 9}
# p6 = {'name': 'p6', 'arrival_time': 5, 'priority': 4, 'burst_time': 4}
# p7 = {'name': 'p7', 'arrival_time': 7, 'priority': 10, 'burst_time': 10}

# p1 = {'name': 'p1', 'arrival_time': 0, 'priority': 2, 'burst_time': 11}
# p2 = {'name': 'p2', 'arrival_time': 5, 'priority': 0, 'burst_time': 28}
# p3 = {'name': 'p3', 'arrival_time': 12, 'priority': 3, 'burst_time': 2}
# p4 = {'name': 'p4', 'arrival_time': 2, 'priority': 1, 'burst_time': 10}
# p5 = {'name': 'p5', 'arrival_time': 9, 'priority': 4, 'burst_time': 16}

p1 = {'name': 'p1', 'arrival_time': 1, 'priority': 3, 'burst_time': 8}
p2 = {'name': 'p2', 'arrival_time': 2, 'priority': 4, 'burst_time': 2}
p3 = {'name': 'p3', 'arrival_time': 4, 'priority': 4, 'burst_time': 4}
p4 = {'name': 'p4', 'arrival_time': 5, 'priority': 5, 'burst_time': 1}
p5 = {'name': 'p5', 'arrival_time': 6, 'priority': 2, 'burst_time': 6}
p6 = {'name': 'p6', 'arrival_time': 7, 'priority': 6, 'burst_time': 5}
p7 = {'name': 'p7', 'arrival_time': 11, 'priority': 1, 'burst_time': 1}

# roundrobin
# print(*roundrobin([p1,p2,p3,p4],2))

# priority non preemptive
# print(*priority_np([p1,p2,p3,p4, p5, p6, p7]))

# priority preemptive
# print(*priority_p([p1,p2,p3,p4, p5, p6, p7]))

# FCFS
print(*FCFS([p1, p2, p3, p4, p5, p6, p7]))
print(p1,p2,p3,p4,p5,p6,p7)


# test the gantt chart
average_waiting_time , processes, x_ticks= priority_p([p1, p2, p3,p4,p5,p6,p7])
gantt_chart(processes, x_ticks)
