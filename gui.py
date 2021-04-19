from algorithms.roundrobin import roundrobin
from algorithms.priority_np import priority_np
from algorithms.priority_p import priority_p
from algorithms.FCFS import FCFS
from gantt_chart import gantt_chart

import tkinter as tk

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
    "Shorted-Job-First Preemptive" : None,
    "Shorted-Job-First Non Preemptive" : None,
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

    # Frame for waiting time.
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

    def submit_process_details():
        global count
        count += 1

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
        process_name_entry.delete(0, 'end')
        arrival_time_entry.delete(0, 'end')
        burst_time_entry.delete(0, 'end')
        if selected_algorithm.get() == "Priority Non Preemptive" or selected_algorithm.get() == "Priority Preemptive":
            priority_entry.delete(0, 'end')

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
        process_number = int(process_number)
        if selected_algorithm.get() == "Round Robin":
            time_quantum = time_quantum_entry.get()
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