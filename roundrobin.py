import numpy as np

def is_sorted(arr):
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<last:
            return False
        last = arr[i]
    return True

# Function to check if all processes are done
def prcoesses_done(processes):
    for process in processes:
        if process>0:
            return False
    return True


def roundrobin(burst_times,time_quantum,*,arrival_times=None):
    number_of_processes = len(burst_times)    
    if arrival_times is None:
        arrival_times = [0]*number_of_processes 
    if len(burst_times)!=len(arrival_times):
        raise Exception('Invalid Input')
    current_time = min(arrival_times)
    counter = 0
    burst_times = burst_times.copy()
    x_ticks = [current_time]    # This variable represents ticks on the  X-axis
    processes = list()  # This variable represents the process on the respective X-axis tick
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
                    processes.append(counter+1)
                    last_time_checked[counter]=current_time
                else:
                    x_ticks.append(current_time+burst_times[counter])
                    waiting_time[counter]+=current_time-last_time_checked[counter]
                    current_time+=burst_times[counter]
                    burst_times[counter]=0
                    processes.append(counter+1)
                    last_time_checked[counter]=current_time
        counter = (counter+1)%number_of_processes
        average_waiting_time = sum(waiting_time)/len(waiting_time)
    return average_waiting_time,np.asarray(processes),np.asarray(x_ticks)