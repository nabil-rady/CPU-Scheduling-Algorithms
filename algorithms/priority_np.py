import numpy as np

def handle_priority(processes,time_line_processes,x_ticks,processes_times):
    # check if the first arrival is not 0
    if len(x_ticks) == 1 and x_ticks[0] > 0:
        for i in range(len(processes)):
            if processes[i]['arrival_time'] > x_ticks[0]:
                processes[i]['arrival_time'] -= x_ticks[0]
            else:
                processes[i]['arrival_time'] = 0
    
    # get the last executed process and manipulate the gantt chart
    prev = processes[0]
    processes.pop(0)
    time_line_processes.append(prev)
    x_ticks.append(x_ticks[len(x_ticks) - 1] + prev['burst_time'])

    # calculate waiting time
    for i in range(len(processes)):
        for p in processes_times:
            if p['name'] == processes[i]['name']:
                if x_ticks[len(x_ticks) - 2] >= p['arrival_time']:
                    p['waiting_time'] += prev['burst_time']
                elif x_ticks[len(x_ticks) - 1] > p['arrival_time']:
                    p['waiting_time'] += x_ticks[len(x_ticks) - 1] - p['arrival_time']

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            if prev['burst_time'] >= processes[i]['arrival_time']:
                processes[i]['arrival_time'] = 0
            else:
                processes[i]['arrival_time'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    return processes


def priority_np(processes): 
    for i in range(len(processes)):
        processes[i] = processes[i].copy()   
    time_line_processes = []

    processes_times = []
    for process in processes:
        p = {
            'name': process['name'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'waiting_time': 0
        }
        processes_times.append(p)

    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    x_ticks = [processes[0]['arrival_time']]     # Shift time to lowest arrival time
    
    n = len(processes)

    i = n
    # for counter in range(n):
    #     i += processes[counter]['burst_time']
    # burst_total = i

    while i > 0:
        processes = handle_priority(processes,time_line_processes,x_ticks,processes_times)
        i-=1


    total_waiting_time = 0
    for p in processes_times:
        total_waiting_time += p['waiting_time']

    
    average_waiting_time = total_waiting_time / n
    processes_names = []

    for i in range(0, len(time_line_processes)):
        processes_names.append(time_line_processes[i]['name'])


    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)


