import numpy as np

def SJF(processes):
    number_of_processes = len(processes)
    arrival_times = [process['arrival_time'] for process in processes]
    shift_time = min(arrival_times)
    x_ticks = [shift_time]
    counter = 0
    waiting_time=0
    total_waiting_time=0

    #sort the processes based on their arrival time
    processes = sorted(processes, key=lambda k: (k['arrival_time']))
    for process in range (number_of_processes):
        for p in range (process, number_of_processes):
            if shift_time >= processes[p]['arrival_time']:
                processes[p]['arrival_time'] = counter
        counter += 1
        
        #sort the processes based on their arrival & burst times
        processes = sorted(processes, key=lambda k: (k['arrival_time'], k['burst_time']))
        
        #calculate x_ticks
        shift_time += processes[process]['burst_time']
        x_ticks.append(shift_time)
        
        #calculate average waiting time
        if process == 0:
            waiting_time = 0
        else:
            waiting_time += processes[process-1]['burst_time']
        total_waiting_time += waiting_time
    average_waiting_time = total_waiting_time/number_of_processes

    counter = 0
    
    #get processes names after sorting them
    processes_names = [process['name'] for process in processes]
    

    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)