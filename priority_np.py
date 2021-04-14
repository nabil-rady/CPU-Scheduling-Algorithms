# global variables
finishedProcesses = [0]
gantChart = [0]


def handel_priority(processes):
    # using global variables
    global finishedProcesses
    global gantChart
    
    # get the last executed process
    prev = {
        'name': processes[0]['name'],
        'priority': processes[0]['priority'],
        'burst_time': processes[0]['burst_time'],
        'const_arrival': processes[0]['const_arrival']
    }

    finishedProcesses.append(prev)
    processes.pop(0)
    
    # to calculate the waiting time and complete the gantChart
    finishedProcesses[0] += gantChart[len(gantChart) - 1] - prev['const_arrival']
    time = gantChart[len(gantChart) - 1] + prev['burst_time']
    gantChart.append(time)

    # handel the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival'] > 0:
            if prev['burst_time'] >= processes[i]['arrival']:
                processes[i]['arrival'] = 0
            else:
                processes[i]['arrival'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival'], k['const_arrival'], k['priority'], k['burst_time']))
    return processes



# The priority_np function arguments

# process = {
#     burst_time: ,
#     priority:
# }
# processes = [{}, {}, ......]

# the return array contains average waiting at index 0,
# the gantChart times at the last elemet

def priority_np(processes):
    # using global variables
    global finishedProcesses
    global gantChart
    
    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival'], k['priority'], k['burst_time']))
    
    n = len(processes)
    i = n
    
    while i > 0:
        processes = handel_priority(processes)
        i-=1
    
    finishedProcesses[0] /=  n
    finishedProcesses.append(gantChart)

    return finishedProcesses


