import numpy as np
import matplotlib.pyplot as plt 
import random
import tkinter as tk
from tkinter import messagebox

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


def handle_priority_np(processes,time_line_processes,x_ticks,processes_times):
    # check if the first arrival is not 0
    if len(x_ticks) == 1 and x_ticks[0] > 0:
        for i in range(len(processes)):
            if processes[i]['arrival_time'] > x_ticks[0]:
                processes[i]['arrival_time'] -= x_ticks[0]
            else:
                processes[i]['arrival_time'] = 0
    
    # get the last executed process and manipulate the gantt chart
    prev = processes[0]
    processes.pop(0)
    time_line_processes.append(prev)
    x_ticks.append(x_ticks[len(x_ticks) - 1] + prev['burst_time'])

    # calculate waiting time
    for i in range(len(processes)):
        for p in processes_times:
            if p['name'] == processes[i]['name']:
                if x_ticks[len(x_ticks) - 2] >= p['arrival_time']:
                    p['waiting_time'] += prev['burst_time']
                elif x_ticks[len(x_ticks) - 1] > p['arrival_time']:
                    p['waiting_time'] += x_ticks[len(x_ticks) - 1] - p['arrival_time']

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            if prev['burst_time'] >= processes[i]['arrival_time']:
                processes[i]['arrival_time'] = 0
            else:
                processes[i]['arrival_time'] -= prev['burst_time']

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    return processes


def priority_np(processes): 
    for i in range(len(processes)):
        processes[i] = processes[i].copy()   
    time_line_processes = []

    processes_times = []
    for process in processes:
        p = {
            'name': process['name'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'waiting_time': 0
        }
        processes_times.append(p)

    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    x_ticks = [processes[0]['arrival_time']]     # Shift time to lowest arrival time
    
    n = len(processes)

    i = n
    # for counter in range(n):
    #     i += processes[counter]['burst_time']
    # burst_total = i

    while i > 0:
        processes = handle_priority_np(processes,time_line_processes,x_ticks,processes_times)
        i-=1


    total_waiting_time = 0
    for p in processes_times:
        total_waiting_time += p['waiting_time']

    
    average_waiting_time = total_waiting_time / n
    processes_names = []

    for i in range(0, len(time_line_processes)):
        processes_names.append(time_line_processes[i]['name'])


    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)



def handle_priority_p(processes,time_line_processes,x_ticks,processes_times):
    # check if the first arrival is not 0
    if len(x_ticks) == 1 and x_ticks[0] > 0:
        for i in range(len(processes)):
            if processes[i]['arrival_time'] > x_ticks[0]:
                processes[i]['arrival_time'] -= x_ticks[0]
            else:
                processes[i]['arrival_time'] = 0
    
    # get the last executed process
    processes[0]['burst_time'] -= 1
    prev = processes[0]
    
    # manipulate the gantt chart
    if len(time_line_processes) == 0 or prev['name'] != time_line_processes[len(time_line_processes) - 1]['name']:  
        time_line_processes.append(prev)
        x_ticks.append(x_ticks[len(x_ticks) - 1] + 1)

    else:
        x_ticks[len(x_ticks) - 1] += 1

    # calculate waiting time
    for i in range(1, len(processes)):
        if processes[i]['arrival_time'] == 0:
            for p in processes_times:
                if p['name'] == processes[i]['name']:
                    p['waiting_time'] += 1
                    break

    # if the process has finished
    if prev['burst_time'] == 0:
        processes.pop(0)
    

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            processes[i]['arrival_time'] -= 1

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    return processes


def priority_p(processes): 
    for i in range(len(processes)):
        processes[i] = processes[i].copy()   
    time_line_processes = []

    processes_times = []
    for process in processes:
        p = {
            'name': process['name'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'waiting_time': 0
        }
        processes_times.append(p)

    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['priority'], k['burst_time']))
    x_ticks = [processes[0]['arrival_time']]     # Shift time to lowest arrival time
    
    n = len(processes)

    i = 0
    for counter in range(n):
        i += processes[counter]['burst_time']
    

    while i > 0:
        processes = handle_priority_p(processes,time_line_processes,x_ticks,processes_times)
        i-=1


    total_waiting_time = 0
    for p in processes_times:
        total_waiting_time += p['waiting_time']

    
    average_waiting_time = total_waiting_time / n
    processes_names = []

    for i in range(0, len(time_line_processes)):
        processes_names.append(time_line_processes[i]['name'])


    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)

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
    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)

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

def handle_SJF(processes,time_line_processes,x_ticks,processes_times):
    # check if the first arrival is not 0
    if len(x_ticks) == 1 and x_ticks[0] > 0:
        for i in range(len(processes)):
            if processes[i]['arrival_time'] > x_ticks[0]:
                processes[i]['arrival_time'] -= x_ticks[0]
            else:
                processes[i]['arrival_time'] = 0
    
    # get the last executed process
    processes[0]['burst_time'] -= 1
    prev = processes[0]
    
    # manipulate the gantt chart
    if len(time_line_processes) == 0 or prev['name'] != time_line_processes[len(time_line_processes) - 1]['name']:  
        time_line_processes.append(prev)
        x_ticks.append(x_ticks[len(x_ticks) - 1] + 1)

    else:
        x_ticks[len(x_ticks) - 1] += 1

    # calculate waiting time
    for i in range(1, len(processes)):
        if processes[i]['arrival_time'] == 0:
            for p in processes_times:
                if p['name'] == processes[i]['name']:
                    p['waiting_time'] += 1
                    break

    # if the process has finished
    if prev['burst_time'] == 0:
        processes.pop(0)
    

    # handle the different arrival times
    for i in range(len(processes)):
        if processes[i]['arrival_time'] > 0:
            processes[i]['arrival_time'] -= 1

    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['burst_time']))
    return processes


def SJF_P(processes): 
    for i in range(len(processes)):
        processes[i] = processes[i].copy()   
    time_line_processes = []

    processes_times = []
    for process in processes:
        p = {
            'name': process['name'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'waiting_time': 0
        }
        processes_times.append(p)

    # make sure that the processes is sorted base on their priority
    processes = sorted(processes, key=lambda k: (k['arrival_time'], k['burst_time']))
    x_ticks = [processes[0]['arrival_time']]     # Shift time to lowest arrival time
    
    n = len(processes)

    i = 0
    for counter in range(n):
        i += processes[counter]['burst_time']


    while i > 0:
        processes = handle_SJF(processes,time_line_processes,x_ticks,processes_times)
        i-=1


    total_waiting_time = 0
    for p in processes_times:
        total_waiting_time += p['waiting_time']

    
    average_waiting_time = total_waiting_time / n
    processes_names = []

    for i in range(0, len(time_line_processes)):
        processes_names.append(time_line_processes[i]['name'])


    return round(average_waiting_time, 2), processes_names, np.asarray(x_ticks)

# colors
colors = ['black' , 'aqua' , 'orange','teal' , 'chocolate','maroon','darkmagenta','gold','orchid' , 'green' , 'palegreen' , 'gray' , 'greenyellow' ,'yellow' , 'deeppink' ,'darkviolet' , 'blue' , 'darkblue' ,'darkcyan' , 'crimson' ,'red', 'olive','turquoise']

def assign_colors(processes):
    colors_of_processes = dict()
    used_colors = dict()
    for process in processes:
        color = random.choice(colors)
        while color in used_colors:
            color = random.choice(colors)
        used_colors[color] = None
        colors_of_processes[process] = color
    return colors_of_processes  

def gantt_chart(processes, x_ticks):
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    processes_names = sorted(list(set(processes)))
    colors_of_processes = assign_colors(processes)  

    processes_start = []

    for i in range(len(processes_names)):
        p = {
            'name': processes_names[i],
            'start': i + 1
        }
        processes_start.append(p)

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes line')
    gnt.set_ylim(0, 3)
    # Setting ticks on x-axis
    gnt.set_xticks([2*i for i in range(max(x_ticks) + 4)])
    # gnt.set_yticks([0.5 * i for i in range(1,len(processes_names)+ 1)])
    gnt.set_yticks([1,2,3])
    # Setting graph attribute
    gnt.grid(True)

    facecolors = [colors_of_processes[process_name] for process_name in processes]
    # Declaring a bar in schedule
    for i in range(len(processes)):
        start = 0
        for process_start in processes_start:
            if process_start['name'] == processes[i]:
                start = process_start['start'] 
                break
        # gnt.broken_barh([(x_ticks[i], x_ticks[i + 1]-x_ticks[i])], (0.5*(start-len(processes_names)/20), len(processes_names)/20), color = facecolors[i], label='p'+str(i+1))
        gnt.broken_barh([(x_ticks[i], x_ticks[i + 1]-x_ticks[i])],(0.75,0.5), color = facecolors[i], label=processes[i])
        # plt.legend(facecolors[i],labels='p'+str(i+1))
        plt.legend(loc='upper right')
    # gnt.set_yticklabels(processes_names)
    print(processes)
    plt.show()

root = tk.Tk()
root.title('CPU scheduling algorithms')
root.geometry("500x500")

# Storing all CPU scheduling algorithms in a list.
scheduling_algorithms = [
    "First-Come, First-Served",
    "Shorted-Job-First Preemptive",
    "Shorted-Job-First Non Preemptive",
    "Round Robin",
    "Priority Preemptive",
    "Priority Non Preemptive"
]

algorithm_functions = {
    "First-Come, First-Served" : FCFS,
    "Shorted-Job-First Preemptive" : SJF_P,
    "Shorted-Job-First Non Preemptive" : SJF,
    "Round Robin" : roundrobin,
    "Priority Preemptive" : priority_p,
    "Priority Non Preemptive" : priority_np,
    
}

# This list will contain widgets to be deleted
global widgets
widgets = []

def show_widgets(event):
    global widgets
    for widget in widgets[:]:
        widget.destroy()
        widgets.remove(widget)
    
    # storing process information in a list of dictionary
    process_details = []

    # Frame for the process number.
    process_frame = tk.LabelFrame(root, padx=5, pady=5)

    # Frame for the information/detials of each process.
    process_details_frame = tk.LabelFrame(root, padx=10, pady=10)

    # Frame for the algorithm waiting time.
    waiting_time_frame = tk.LabelFrame(root, padx=5, pady=5)

    # Input field for the number of avaliable processes.
    process_name_label = tk.Label(process_frame, text = 'Enter number of processes: ').grid(row=0, column=0, padx=5)
    process_number_entry = tk.Entry(process_frame, width=15, borderwidth=5)
    process_number_entry.grid(row=0, column=1, padx=5)
  
    # Input field for time quantum in case of round robin.
    global time_quantum_entry
    if selected_algorithm.get() == "Round Robin":
        time_quantum_label = tk.Label(process_frame, text = 'Enter time quantum:').grid(row=1, column=0, padx=5)
        time_quantum_entry = tk.Entry(process_frame, width=15, borderwidth=5)
        time_quantum_entry.grid(row=1, column=1, padx=5)
    
    global count
    count = 1

    def process_details_widgets():
        # display process number 
        global process_number_label
        process_number_label = tk.Label(process_details_frame, text = 'Process #{}'.format(count))
        process_number_label.grid(row=0, column=1)

        # entry for process name
        process_name_label = tk.Label(process_details_frame, text = 'Enter process name:').grid(row=1, column=0, padx=5)
        global process_name_entry
        process_name_entry = tk.Entry(process_details_frame, width=15, borderwidth=5)
        process_name_entry.grid(row=1, column=1, padx=5)

        # entry for arrival time
        arrival_time_label = tk.Label(process_details_frame, text = 'Enter process arrival time:').grid(row=2, column=0, padx=5)
        global arrival_time_entry
        arrival_time_entry = tk.Entry(process_details_frame, width=15, borderwidth=5)
        arrival_time_entry.grid(row=2, column=1, padx=5)

        # entry for brust time
        burst_time_label = tk.Label(process_details_frame, text = 'Enter process brust time:').grid(row=3, column=0, padx=5)
        global burst_time_entry
        burst_time_entry = tk.Entry(process_details_frame, width=15, borderwidth=5)
        burst_time_entry.grid(row=3, column=1, padx=5)

        #entry for process priority
        global priority_entry
        if selected_algorithm.get() == "Priority Non Preemptive" or selected_algorithm.get() == "Priority Preemptive":
            burst_time_label = tk.Label(process_details_frame, text = 'Enter process priority:').grid(row=4, column=0, padx=5)
            priority_entry = tk.Entry(process_details_frame, width=15, borderwidth=5)
            priority_entry.grid(row=4, column=1, padx=5)
        
        process_details_button = tk.Button(process_details_frame, text="submit", command=submit_process_details)
        process_details_button.grid(row=5, column=1, pady=10)
     
    def call_gantt_chart(processes, x_ticks):
        gantt_chart(processes,x_ticks)

    def execution_gantt_chart():
        algorithm_function = algorithm_functions[selected_algorithm.get()]
        if algorithm_function.__name__ == 'roundrobin':
            average_waiting_time,processes,x_ticks = algorithm_function(process_details, int(time_quantum) )
        else:
            average_waiting_time,processes,x_ticks = algorithm_function(process_details)


        average_waiting_time_label = tk.Label(waiting_time_frame, text='Waiting time = {}'.format(average_waiting_time)).grid(row=0, column=0, padx=5)
        execution_button = tk.Button(waiting_time_frame, text="View Gantt Chart", command= lambda:call_gantt_chart(processes, x_ticks))
        execution_button.grid(row = 1, column=1, pady=10)
        waiting_time_frame.pack()
    
    def delete_details_frame():
        process_details_frame.pack_forget()
        process_details_frame.destroy()
        execution_gantt_chart()

    def clearInputEntries():
        process_name_entry.delete(0, 'end')
        arrival_time_entry.delete(0, 'end')
        burst_time_entry.delete(0, 'end')
        if selected_algorithm.get() == "Priority Non Preemptive" or selected_algorithm.get() == "Priority Preemptive":
            priority_entry.delete(0, 'end')
    
    def isValidInput():
        arrival_time = arrival_time_entry.get()
        burst_time = burst_time_entry.get()

        if not arrival_time.isdigit():
            response = messagebox.showerror("Error", "Enter a positive number for the arrival time.")
            if response == 'ok':
                return False
        elif not burst_time.isdigit():
            response = messagebox.showerror("Error", "Enter a positive number for the brust time.")
            if response == 'ok':
                return False
        elif selected_algorithm.get() == "Priority Non Preemptive" or selected_algorithm.get() == "Priority Preemptive":
            priority = priority_entry.get()
            if not priority.isdigit():
                response = messagebox.showerror("Error", "Enter a positive number for the process priority.")
                if response == 'ok':
                    return False
        return True
        

    def submit_process_details():
        global count
        count += 1

        if not isValidInput():
            count -= 1
            clearInputEntries()
            return

        name = process_name_entry.get()
        arrival_time = arrival_time_entry.get()
        burst_time = burst_time_entry.get()

        if selected_algorithm.get() == "Priority Non Preemptive" or selected_algorithm.get() == "Priority Preemptive":
            priority = priority_entry.get()
            process_details.append (
                {
                    'name' : name,
                    'arrival_time' : int(arrival_time),
                    'burst_time' : int (burst_time),
                    'priority' : int(priority)
                }
            )
        else :
            process_details.append (
                {
                    'name' : name,
                    'arrival_time' : int(arrival_time),
                    'burst_time' : int (burst_time)
                }
            )
        process_number_label.config(text='Process #{}'.format(count))
        clearInputEntries()

        # Testing that process fields are stored in process_details list
        print(process_details)

        if count > process_number:
            delete_details_frame()
            return

    # Submit button for the entered process number.
    def submit_process_number():
        global process_number
        global time_quantum
        process_number = process_number_entry.get()
        if selected_algorithm.get() == "Round Robin":
            time_quantum = time_quantum_entry.get()
        if not process_number.isdigit():
            response = messagebox.showerror("Error", "Number of processes must be integer.")
            if response == 'ok':
                process_number_entry.delete(0, 'end')
                if selected_algorithm.get() == "Round Robin":
                    time_quantum_entry.delete(0, 'end')
                return
        elif selected_algorithm.get() == "Round Robin":
            if not time_quantum.isdigit():
                response = messagebox.showerror("Error", "Enter a positive number for the time quantum.")
                if response == 'ok':
                    process_number_entry.delete(0, 'end')
                    time_quantum_entry.delete(0, 'end')
                    return
        process_number = int(process_number)
        process_frame.pack_forget()
        process_frame.destroy()
        process_details_widgets()

    process_number_button = tk.Button(process_frame, text="submit", command=submit_process_number)
    process_number_button.grid(row = 2, column=1, pady=10)

    widgets = widgets[:] + [process_frame, process_details_frame, waiting_time_frame]
    for widget in widgets:
        widget.pack()

# Drop Down Menu
selected_algorithm = tk.StringVar()
selected_algorithm.set("Select an algorithm")

drop_menu = tk.OptionMenu(root, selected_algorithm , *scheduling_algorithms, command=show_widgets)
drop_menu.pack(pady=10)


root.mainloop()