import numpy as np

# Function to check if all processes are done
def prcoesses_done(burst_times):
    for burst_time in burst_times:
        if burst_time>0:
            return False
    return True


def roundrobin(processes,time_quantum):
    burst_times = [process['burst_time'] for process in processes]
    arrival_times = [process['arrival_time'] for process in processes]
    number_of_processes = len(burst_times)    
    current_time = min(arrival_times)
    counter = 0
    burst_times = burst_times.copy()
    x_ticks = [current_time]    # This variable represents ticks on the  X-axis
    processes_names = list()  # This variable represents the process on the respective X-axis tick
    waiting_time = [0]*number_of_processes  # Waiting time for each process
    last_time_checked = arrival_times.copy()    # Last time the process was active or the time of arrival
    while not prcoesses_done(burst_times):
        # Check if process is not finished
        if (burst_times[counter]!=0):
            if current_time >= arrival_times[counter]:
            # Check if time quantum is smaller than process burst time
                if (burst_times[counter]>=time_quantum):
                    x_ticks.append(current_time+time_quantum)
                    waiting_time[counter]+=current_time-last_time_checked[counter]
                    current_time+=time_quantum
                    burst_times[counter]-=time_quantum
                    processes_names.append(processes[counter]['name'])
                    last_time_checked[counter]=current_time
                else:
                    x_ticks.append(current_time+burst_times[counter])
                    waiting_time[counter]+=current_time-last_time_checked[counter]
                    current_time+=burst_times[counter]
                    burst_times[counter]=0
                    processes_names.append(processes[counter]['name'])
                    last_time_checked[counter]=current_time
        counter = (counter+1)%number_of_processes
        average_waiting_time = sum(waiting_time)/len(waiting_time)
    return average_waiting_time,processes_names,np.asarray(x_ticks)