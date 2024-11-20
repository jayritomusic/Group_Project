import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ASTR19_F24_group_project_data.txt",
                     dtype=[('myint','i8'),('mystring','S5'),('myfloat','f8')])

day = []
time = []
height = []

#print(data)
#print(data.shape)

for i in range(82):
    day.append(data[i][0])
    time.append(data[i][1].decode("utf-8"))
    height.append(data[i][2])
    
    
print(day)
print('')
print(time)
print('')
print(day)
print(height)

def convert_time(time_value):
    #separate time into hours and minutes
    hours, minutes = time_value.split(':')
    #turn them into a number
    hours = float(hours)
    minutes = float(minutes)
    #turn into hour decimal
    hours = hours+minutes/60
    #turn into days
    return hours/24

#make empty list for x axis
t = []
#loop data set
for i in range (len(time)):
    #convert time elements
    time_converted = convert_time(time[i])
    #add each converted time to that same day element. Add to xaxis list. 
    t.append(day[i]+time_converted)

print(t)

##graph data, putting points on relevant data
plt.plot(t, height, 'o-')

plt.savefig('time-height.png', bbox_inches="tight", facecolor='white') 