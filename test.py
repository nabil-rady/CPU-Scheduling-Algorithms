# Use this file to test 
from roundrobin import roundrobin
from priority_np import priority_np

# processes
p1 = {'name': 'p1', 'arrival_time': 0, 'priority': 3, 'burst_time': 3}
p2 = {'name': 'p2', 'arrival_time': 1, 'priority': 4, 'burst_time': 6}
p3 = {'name': 'p3', 'arrival_time': 3, 'priority': 9, 'burst_time': 1}
p4 = {'name': 'p4', 'arrival_time': 2, 'priority': 7, 'burst_time': 2}
# p5 = {'name': 'p5', 'arrival_time': 4, 'const_arrival_time': 4, 'priority': 8, 'burst_time': 4}

# roundrobin
print(*roundrobin([p1,p2,p3,p4],2))

# priority non preemptive
print(*priority_np([p1,p2,p3,p4]))