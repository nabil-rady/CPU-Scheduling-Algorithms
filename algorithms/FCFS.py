import numpy as np
def FCFS(processes):
    processes=processes.copy()
    n=len(processes)
    x_ticks = [sorted(processes,key=lambda x:x['arrival_time'])[0]['arrival_time']]
    # x_ticks[0] = 0
    wt=[]

    # wt[0] = 0
    total=0
    total_time=0
    processes_names = []
    for i in range(n):
        for j in range(i+1,n):
            if(processes[i]['arrival_time']>processes[j]['arrival_time']):
                processes[i],processes[j] = processes[j],processes[i]
    for k in range(n):
        x_ticks.append(x_ticks[k] +processes[k]['burst_time'])
        wt.append(x_ticks[k] - processes[k]['arrival_time'])
        total_time +=processes[k]['burst_time']
        processes_names.append(processes[k]['name'])
        total += wt[k]
    average_waiting_time=total/n
    # x_ticks().append(total_time)
    return round(average_waiting_time,2),processes_names,x_ticks