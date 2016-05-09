import time
import math
from sys import argv
import sys

##image grid size (10,10)
grid = [[0]*11 for _ in range(11)]
position_x = 6
position_y = 0
position_z = 0
dest_x = 5
dest_y = 10
dest_z = 0
depth = 0
max_depth = 1
left_count = 0
right_count = 0
#####################################################################
def fil_in_grid(x1,y1,x2,y2, depth1, object_counter):
    global left_count, right_count, depth
    print ":::::::::::::::::::::::::::::::::::::::::::::::::::::: "
    print "( " + str(x1) + " , " + str(y1) + " ), ( " + str(x2) + " , " + str(y2) + " )" + " object_counter: " + str(object_counter) +  " depth: " + str(depth)
    x_min = min(x1, x2)
    y_min = min(x1, x2)
    x_max = max(x1, x2)
    y_max = max(x1, x2)
    depth = depth1


    for x in range(x_min, x_max+1):
        for y in range(y_min,y_max+1):
            grid[x][y] = depth
            if x <= 5:
                left_count = left_count + 1
            else:
                right_count = right_count + 1
    print ":::::::::::::::::::::::::::::::::::::::::::::::::::::: "
def state2(left_or_right):
        global position_x, position_y, position_z
        if(left_or_right == 0):
            print "turning right"
            position_x += math.sin(math.pi/6)*depth
            position_y += math.cos(math.pi/6)*depth
            position_x = abs(position_x)
            position_y = abs(position_y)
        else:
            print "turning left"
            position_x += math.sin(math.pi/6)*depth
            position_y += math.cos(math.pi/6)*depth
            position_x = abs(position_x)
            position_y = abs(position_y)
            print position_y

        print "Current Position: " + "( " + str(position_x) + " , " + str(position_y) + " , " + str(position_z) + " )"






def state1(inputs, length):
    print "count of objects " + str(inputs[0])
    pixel_counter = 0
    object_counter = 1
    for i in range(1, length):
        if pixel_counter == 4:
            #print "( " + str(inputs[i-3]) + " , " + str(inputs[i-2]) + " ), ( " + str(inputs[i-1]) + " , " + str(inputs[i]) + " )"
            fil_in_grid(inputs[i-4], inputs[i-3],inputs[i-2],inputs[i-1],inputs[i],object_counter)
            pixel_counter = 0
            object_counter = object_counter + 1
        else:
            pixel_counter = pixel_counter + 1
    print "left count: " + str(left_count) + "    right count: " + str(right_count)
    for x in range(11):
        for y in range(11):
            print grid[x][y] ,
        print
    if right_count >= left_count:
        state2(1)
    else:
        state2(0)

def state_no_obj_in_front():
    global position_x, position_y, max_depth
    dif_x = dest_x - position_x
    dif_y = dest_y - position_y
    distance_btw_points = math.sqrt( pow((dest_y - position_y),2) + pow((dest_x - position_x),2))
    if distance_btw_points < 1.0:
        depth = distance_btw_points
    else:
        depth = 1.0

    angle = abs(math.atan( dif_y / dif_x))
    position_x += math.sin(angle) * depth
    position_y += math.cos(angle) * depth
    print "Destination Position: " + "( " + str(dest_x) + " , " + str(dest_y) + " , " + str(dest_z) + " )"

def check_position():
    print "checking position"
    dif_x = dest_x - position_x
    dif_y = dest_y - position_y
    if (dif_x <1 and  dif_y <1 ):
        print "at Destination"
        sys.exit("At Destination")


#####################################################################
print "Type the filename again:"
filename = raw_input("> ")

inputs = []
state1_go = 0
text = open(filename)
line = text.readline()
count = 0
print "Current Position: " + "( " + str(position_x) + " , " + str(position_y) + " , " + str(position_z) + " )"
#print ":::::::::::::::::::::::::::::::::::::::::::::::::::::: "
while line:
    #print line + " the string"
    #print str(len(line)) + " the count"
    #print line[:10] + " bit 1 throught 10"
    #print line[10] + " bit 11"
    while line[10] == "1":
        num = int(line[:10],2)
        state1_go = 1
#    print " number version of binary: " +  str(num) + " bit 11: " + line[10]
        #if line[10] == "1":
#        print "state 1 bitches"
        inputs.append(num)
        #count = count + 1
        #print "count: " + str(count)
    #else:
#        print "next line bitch"
    #print ":::::::::::::::::::::::::::::::::::::::::::::::::::::: "
        line = text.readline()
#print len(inputs)
    if state1_go == 1:
        state1(inputs, len(inputs))
        state1_go = 0
    else:
        state_no_obj_in_front()
    print " Else Current Position: " + "( " + str(position_x) + " , " + str(position_y) + " , " + str(position_z) + " )"
    check_position()
    line = text.readline()



#import mraa     # For accessing the GPIO

'''pins = [0]*12
binary_pins = [""] * 4 ##

def state0():
    pin[11].write(1)
    bool = False
    while (bool == False):
        if pins[10] == 1 and pin[11] == 1:
            bool = True
            state1()

def state1():
    num_of_objects = []
    binary_number = ""
    for i in range(2,11):
        num_of_objects[i] = input("Enter your input pins: ")
        binary_number = binary_number + num_of_objects[i]
    number = int(binary_number)
    if number > 0:
        state2(number)
    state0()

def state2(number):
    numbers = [[0] * 2 for _ in range(number)]# [x1, y1, x2, y2] ##
    for num_of_values in range(number):
        for i in range(2):
            for j in range(10):
                binary_pins[i] += pins[j]
        number[num_of_values][i] = int(binary_number)
        binary_pins[i] = ""
    state(3)
def state3():
    pin[11].write(0)
    ### analysis of data
    print "done"
    state0()
'''
