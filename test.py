# Use this file to test 
from roundrobin import roundrobin
from priority_np import priority_np

# roundrobin

# priority non preemptive
p1 = {'name': 'p1', 'arrival_time': 0, 'const_arrival_time': 0, 'priority': 3, 'burst_time': 3}
p2 = {'name': 'p2', 'arrival_time': 1, 'const_arrival_time': 1, 'priority': 4, 'burst_time': 6}
p3 = {'name': 'p3', 'arrival_time': 3, 'const_arrival_time': 3, 'priority': 9, 'burst_time': 1}
p4 = {'name': 'p4', 'arrival_time': 2, 'const_arrival_time': 2, 'priority': 7, 'burst_time': 2}
p5 = {'name': 'p5', 'arrival_time': 4, 'const_arrival_time': 4, 'priority': 8, 'burst_time': 4}

print(*roundrobin([p1,p2,p3,p4],2))

# processes = [p1, p2, p3, p4, p5]
# result = priority_np(processes)

# print("\n# Priority non preemptive")
# print(f"the average waiting time: {result[0]}")
# print("the order of execution:", end=' ')
# for i in range(1, len(result) - 1):
#     print(f"{result[i]['name']}", end=" ")
# print()
# print("the gantChart times:", end=' ')
# for i in range(len(result[len(result)-1])):
#     print(f"{result[len(result)-1][i]}", end=" ")
# print()
