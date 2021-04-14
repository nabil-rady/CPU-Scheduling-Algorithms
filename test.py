# Use this file to test 
from roundrobin import roundrobin

print(*roundrobin([5,4,2,1],2,arrival_times=[5,1,1,1]))
