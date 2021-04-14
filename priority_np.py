def handel_priority(processes):
    prev = {
        'name': processes[0]['name'],
        'priority': processes[0]['priority'],
        'burst_time': processes[0]['burst_time']
    }

    finishedProcesses.append(prev)
    processes.pop(0)
    
    for i in range(len(processes)):
        if processes[i]['arrival'] > 0:
            if prev['burst_time'] >= processes[i]['arrival']:
                processes[i]['arrival'] = 0
            else:
                processes[i]['arrival'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival'], k['priority'], k['burst_time']))
    return processes



# The priority_np function arguments

# process = {
#     burst_time: ,
#     priority:
# }
# processes = [{}, {}, ......]

def priority_np(processes):
    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival'], k['priority'], k['burst_time']))
    
    global finishedProcesses
    finishedProcesses = [0]

    n = len(processes)
    
    while n > 0:
        processes = handel_priority(processes)
        n-=1
    
    return finishedProcesses



