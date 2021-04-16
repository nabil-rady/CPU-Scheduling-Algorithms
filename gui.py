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

def showWidgets(event):
    # storing process information in a list of dictionary
    processDetails = []

    # Frame for the process number.
    processFrame = tk.LabelFrame(root, padx=5, pady=5)
    processFrame.pack(padx=5, pady=5)  

    # Input field for the number of avaliable processes.
    processNumberEntry = tk.Entry(processFrame, width=30, borderwidth=5)
    processNumberEntry.pack()
    processNumberEntry.insert(0, "Enter number of processes: ")

    def processDetailsWidgets():
        # Frame for the information/detials of each process.
        processDetialsFrame = tk.LabelFrame(root, padx=10, pady=10)
        processDetialsFrame.pack(padx=10, pady=10)

        # entry for process name
        processNameEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        processNameEntry.pack()
        processNameEntry.insert(0, "Enter process name: ")

        # entry for arrival time
        arrivalTimeEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        arrivalTimeEntry.pack()
        arrivalTimeEntry.insert(0, "Enter process arrival time: ")

        # entry for brust time
        brustTimeEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
        brustTimeEntry.pack()
        brustTimeEntry.insert(0, "Enter process brust time: ")

        if selectedAlgorithm.get() == schedulingAlgorithms[4] or selectedAlgorithm.get() == schedulingAlgorithms[5]:
            priorityTimeEntry = tk.Entry(processDetialsFrame, width=30, borderwidth=5)
            priorityTimeEntry.pack()
            priorityTimeEntry.insert(0, "Enter process priority: ")
        
        def submitProcessDetails():
            name = processNameEntry.get()
            arrivalTime = arrivalTimeEntry.get()
            brustTime = brustTimeEntry.get()

            if selectedAlgorithm.get() == schedulingAlgorithms[4] or selectedAlgorithm.get() == schedulingAlgorithms[5]:
                priority = priorityTimeEntry.get()
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

            processDetialsFrame.pack_forget()
            processDetialsFrame.destroy()
        
        processDetailsButton = tk.Button(processDetialsFrame, text="submit", command=submitProcessDetails)
        processDetailsButton.pack()


    # Submit button for the entered process number.
    def submitProcessNumber():
        global processNumber
        processNumber = processNumberEntry.get()
        processFrame.pack_forget()
        processFrame.destroy()
        processDetailsWidgets()

    processNumberButton = tk.Button(processFrame, text="submit", command=submitProcessNumber)
    processNumberButton.pack()


# Drop Down Menu
selectedAlgorithm = tk.StringVar()
selectedAlgorithm.set(schedulingAlgorithms[0])

dropMenu = tk.OptionMenu(root, selectedAlgorithm, *schedulingAlgorithms, command=showWidgets)
dropMenu.pack(pady=10)

root.mainloop()