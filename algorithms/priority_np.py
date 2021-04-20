import numpy as np

def handle_priority(processes,finished_processes,x_ticks,processes_arrival_times):
    # check if the first arrival is not 0
    if len(x_ticks) == 1 and x_ticks[0] > 0:
        for i in range(len(processes)):
            if processes[i]['arrival_time'] > x_ticks[0]:
                processes[i]['arrival_time'] -= x_ticks[0]
            else:
                processes[i]['arrival_time'] = 0
    
    # get the last executed process
    prev = processes[0]

    finished_processes.append(prev)
    processes.pop(0)
    
    # to calculate the waiting time and complete the gantt_chart
    finished_processes[0] += x_ticks[len(x_ticks) - 1] - processes_arrival_times[prev['name']]
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



def priority_np(processes): 
    for i in range(len(processes)):
        processes[i] = processes[i].copy()   
    finished_processes = [0]    
    processes_arrival_times = {
        process['name']:process['arrival_time'] for process in processes
    }
    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    x_ticks = [processes[0]['arrival_time']]     # Shift time to lowest arrival time
    n = len(processes)
    i = n
    
    while i > 0:
        processes = handle_priority(processes,finished_processes,x_ticks,processes_arrival_times)
        i-=1

    average_waiting_time = finished_processes[0] / n
    processes_names = []

    for i in range(1, len(finished_processes)):
        processes_names.append(finished_processes[i]['name'])


    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)


