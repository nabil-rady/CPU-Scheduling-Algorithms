def handle_priority(processes,finished_processes,gantt_chart):
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
    finished_processes[0] += gantt_chart[len(gantt_chart) - 1] - prev['const_arrival_time']
    time = gantt_chart[len(gantt_chart) - 1] + prev['burst_time']
    gantt_chart.append(time)

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            if prev['burst_time'] >= processes[i]['arrival_time']:
                processes[i]['arrival_time'] = 0
            else:
                processes[i]['arrival_time'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['const_arrival_time'], k['priority'], k['burst_time']))
    return processes



# The priority_np function arguments

# process = {
#     burst_time: ,
#     priority:
# }
# processes = [{}, {}, ......]

# the return array contains average waiting at index 0,
# the gantt_chart times at the last elemet

def priority_np(processes):
    # using global variables
    finished_processes = [0]
    gantt_chart = [0]
    
    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    
    n = len(processes)
    i = n
    
    while i > 0:
        processes = handle_priority(processes,finished_processes,gantt_chart)
        i-=1
    
    finished_processes[0] /=  n
    finished_processes.append(gantt_chart)

    return finished_processes


