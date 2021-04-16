def findWaitingTime(processes):
    n=len(processes)
    serviceTime = [0]
    # serviceTime[0] = 0
    wt=[]

    # wt[0] = 0
    total=0
    totalTime=0
    processes_names = []
    for i in range(0, n):
        for j in range(i+1,n):
            if(processes[i]['arrival_time']>processes[j]['arrival_time']):
                temp=processes[j]
                processes[j]=processes[i]
                processes[i]=temp
    for k in range (0,n):
        serviceTime.append(serviceTime[k] +processes[k]['burst_time'])
        wt.append(serviceTime[k] - processes[k]['arrival_time'])
        totalTime +=processes[k]['burst_time']
        processes_names.append(processes[k]['name'])
        total += wt[k]
    Avg=total/n
    # serviceTime.append(totalTime)
    return Avg,processes_names,serviceTime

