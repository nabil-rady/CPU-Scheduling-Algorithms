import numpy as np

def SJF(processes):
    number_of_processes = len(processes) 
    arrival_times = [process['arrival_time'] for process in processes]
    shift_time = min(arrival_times)
    x_ticks = [shift_time]
    waiting_time=0
    total_waiting_time=0

    #sort the processes based on their burst time
    processes = sorted(processes, key=lambda k: (k['burst_time']))
    
    #get processes burst times after sorting them
    burst_times = [process['burst_time'] for process in processes]
    #calculate x_ticks
    for time in range(number_of_processes):
        shift_time += burst_times[time]
        x_ticks.append(shift_time)
    
    #get processes names after sorting them
    processes_names = [process['name'] for process in processes]

    #calculate average waiting time
    for i in range(number_of_processes):
        if i == 0:
            waiting_time = 0
        else:
            waiting_time += burst_times[i-1]
        total_waiting_time += waiting_time
    average_waiting_time = total_waiting_time/number_of_processes
    

    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)