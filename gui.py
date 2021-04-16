from roundrobin import roundrobin
from priority_np import priority_np
from priority_p import priority_p

import Tkinter as tk

root = tk.Tk()
root.title('CPU scheduling algorithms')
root.geometry("500x500")

# Storing all CPU scheduling algorithms in a list.
schedulingAlgorithms = [
    "First-Come, First-Served",
    "Shorted-Job-First Preemptive",
    "Shorted-Job-First Non Preemptive",
    "Round Robin",
    "Priority Preemptive",
    "Priority Non Preemptive"
]

 # This list will contain widgets to be deleted
global widgets
widgets = []

def showWidgets(event):
    global widgets
    for widget in widgets[:]:
        widget.destroy()
        widgets.remove(widget)
    
    # storing process information in a list of dictionary
    processDetails = []

    # Frame for the process number.
    processFrame = tk.LabelFrame(root, padx=5, pady=5)

    # Frame for the information/detials of each process.
    processDetialsFrame = tk.LabelFrame(root, padx=10, pady=10)

    # Input field for the number of avaliable processes.
    processNumberEntry = tk.Entry(processFrame, width=30, borderwidth=5)
    processNumberEntry.pack()
    processNumberEntry.insert(0, "Enter number of processes: ")

    def process_details_widgets():
        # entry for process name
        global processNameEntry
        processNameEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        processNameEntry.pack()
        processNameEntry.insert(0, "Enter process name: ")

        # entry for arrival time
        global arrivalTimeEntry
        arrivalTimeEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        arrivalTimeEntry.pack()
        arrivalTimeEntry.insert(0, "Enter process arrival time: ")

        # entry for brust time
        global brustTimeEntry
        brustTimeEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        brustTimeEntry.pack()
        brustTimeEntry.insert(0, "Enter process brust time: ")

        #entry for process priority
        global priorityEntry
        if selectedAlgorithm.get() == schedulingAlgorithms[4] or selectedAlgorithm.get() == schedulingAlgorithms[5]:
            priorityEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
            priorityEntry.pack()
            priorityEntry.insert(0, "Enter process priority: ")
        
        processDetailsButton = tk.Button(processDetialsFrame, text="submit", command=submitProcessDetails)
        processDetailsButton.pack()
        
    def submitProcessDetails():
        name = processNameEntry.get()
        arrivalTime = arrivalTimeEntry.get()
        brustTime = brustTimeEntry.get()

        if selectedAlgorithm.get() == schedulingAlgorithms[4] or selectedAlgorithm.get() == schedulingAlgorithms[5]:
            priority = priorityEntry.get()
            processDetails.append (
                {
                    'name' : name[20:],
                    'arrival_time' : int(arrivalTime[27:]),
                    'brust_time' : int (brustTime[25:]),
                    'priority' : int(priority[23:])
                }
            )
        else :
            processDetails.append (
                {
                    'name' : name[20:],
                    'arrival_time' : int(arrivalTime[27:]),
                    'brust_time' : int (brustTime[25:])
                }
            )
        processNameEntry.delete(20, 'end')
        arrivalTimeEntry.delete(27, 'end')
        brustTimeEntry.delete(25, 'end')
        if selectedAlgorithm.get() == schedulingAlgorithms[4] or selectedAlgorithm.get() == schedulingAlgorithms[5]:
            priorityEntry.delete(23, 'end')
        
    # Submit button for the entered process number.
    def submitProcessNumber():
        global processNumber
        processNumber = processNumberEntry.get()
        processFrame.pack_forget()
        processFrame.destroy()
        process_details_widgets()

    processNumberButton = tk.Button(processFrame, text="submit", command=submitProcessNumber)
    processNumberButton.pack()

    widgets = widgets[:] + [processFrame, processDetialsFrame]
    for widget in widgets:
        widget.pack()


# Drop Down Menu
selectedAlgorithm = tk.StringVar()
selectedAlgorithm.set(schedulingAlgorithms[0])

dropMenu = tk.OptionMenu(root, selectedAlgorithm, *schedulingAlgorithms, command=showWidgets)
dropMenu.pack(pady=10)

root.mainloop()