# Use this file to test 
from roundrobin import roundrobin
from priority_np import priority_np

# roundrobin
print(*roundrobin([5,4,2,1],2,arrival_times=[5,1,1,1]))

# priority non preemptive
p1 = {'name': 'p1', 'arrival': 0, 'priority': 5, 'burst_time': 5}
p2 = {'name': 'p2', 'arrival': 0, 'priority': 0, 'burst_time': 3}
p3 = {'name': 'p3', 'arrival': 2, 'priority': 3, 'burst_time': 7}
p4 = {'name': 'p4', 'arrival': 5, 'priority': 3, 'burst_time': 3}
p5 = {'name': 'p5', 'arrival': 5, 'priority': 3, 'burst_time': 5}

processes = [p1, p2, p3, p4, p5]

print("\n# Priority non preemptive\n")
print(priority_np(processes))
