import numpy as np

# Function to check if all processes are done
def prcoesses_done(processes):
    for process in processes:
        if process>0:
            return False
    return True


def roundrobin(burst_times,time_quantum):
    number_of_processes = len(burst_times)    
    burst_times = burst_times.copy()
    x_ticks = list()    # This variable represents ticks on the  X-axis
    processes = list()  # This variable represents the process on the respective X-axis tick
    current_time = 0
    counter = 0
    while not prcoesses_done(burst_times):
        # Check if process is finished
        if (burst_times[counter]!=0):
            # Check if time quantum is smaller than process burst time
            if (burst_times[counter]>=time_quantum):
                x_ticks.append(current_time+time_quantum)
                current_time+=time_quantum
                burst_times[counter]-=time_quantum
                processes.append(counter+1)
            else:
                x_ticks.append(current_time+burst_times[counter])
                current_time+=burst_times[counter]
                burst_times[counter]=0
                processes.append(counter+1)
        counter = (counter+1)%number_of_processes
    return np.asarray(processes),np.asarray(x_ticks)






