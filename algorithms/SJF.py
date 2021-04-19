# Splitting the list of dictionary into lists of lists#
My_list=[{'name':'p2','arrival_time':1,'priority':0,'burst_time':5 },{'name':'p3','arrival_time':7,'priority':5,'burst_time':8},{'name':'p1','arrival_time':0,'priority':2,'burst_time':9}]
n=len(My_list)
process_names = [i['name'] for i in My_list]
arrival_time=[i['arrival_time']for i in My_list]
burst_time=[i['burst_time']for i in My_list]
print(process_names)
print(arrival_time)
print(burst_time)
#Sorting the processes according to their arrival time
temp=[0]*n
for i in range(0,n):
    for j in range(i+1,n):
      if (My_list[i]['arrival_time']>My_list[j]['arrival_time']):
          temp=My_list[i]
          My_list[i]=My_list[j]
          My_list[j]=temp

print(My_list)
start_time=min(arrival_time)
print(start_time)
complete=0
t=0
min=999999
small=0
check = False
wt=[0]*n
# Process until all processes gets
    # completed
while (complete != n):
        for j in range(n):
            if ((My_list[j]['arrival_time'] <= t) and
                (burst_time[j] < min) and burst_time[j] > 0):
                min = burst_time[j]
                small = j
                check = True
        if (check == False):
            t += 1
            continue

        # Reduce remaining time by one
        burst_time[small] -= 1

        # Update minimum
        min = burst_time[small]
        if (min == 0):
            min = 999999999

        # If a process gets completely
        # executed
        if (burst_time[small] == 0):

            # Increment complete
            complete += 1
            check = False

            # Find finish time of current
            # process
            finish = t + 1

            # Calculate waiting time
            wt[small] = (finish - My_list[small]['arrival_time'] -
                                My_list[small]['burst_time'])

            if (wt[small] < 0):
                wt[small] = 0

        # Increment time
        t += 1

print(wt)
sum_of_waiting=0
for i in range(n):
    sum_of_waiting+=wt[i]
average_waiting_time=(sum_of_waiting)/n
print((average_waiting_time))