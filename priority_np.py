import numpy as np

def handle_priority(processes,finished_processes,x_ticks):
    # get the last executed process
    prev = {
        'name': processes[0]['name'],
        'priority': processes[0]['priority'],
        'burst_time': processes[0]['burst_time'],
        'const_arrival_time': processes[0]['const_arrival_time']
    }

    finished_processes.append(prev)
    processes.pop(0)
    
    # to calculate the waiting time and complete the gantt_chart
    finished_processes[0] += x_ticks[len(x_ticks) - 1] - prev['const_arrival_time']
    time = x_ticks[len(x_ticks) - 1] + prev['burst_time']
    x_ticks.append(time)

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            if prev['burst_time'] >= processes[i]['arrival_time']:
                processes[i]['arrival_time'] = 0
            else:
                processes[i]['arrival_time'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    return processes



# The priority_np function arguments

# process = {
#     burst_time: ,
#     priority:
# }
# processes = [{}, {}, ......]

def priority_np(processes):
    # using global variables
    finished_processes = [0]
    x_ticks = [0]
    
    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    
    n = len(processes)
    i = n
    
    while i > 0:
        processes = handle_priority(processes,finished_processes,x_ticks)
        i-=1

    average_waiting_time = finished_processes[0] / n
    processes_names = []

    for i in range(1, len(finished_processes)):
        processes_names.append(finished_processes[i]['name'])


    return average_waiting_time, np.asanyarray(processes_names), np.asarray(x_ticks)


