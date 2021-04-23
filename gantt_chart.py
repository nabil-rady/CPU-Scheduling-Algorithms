# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt 
import random
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