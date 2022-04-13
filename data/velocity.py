# -*- coding: UTF-8 -*-

import xlwt
allxl = xlwt.Workbook()
sheet1 = allxl.add_sheet('Sheet1')
sheet1.write(0, 0, 'robot1_velocity')
sheet1.write(0, 1, 'robot2_velocity')
sheet1.write(0, 2, 'robot3_velocity')
sheet1.write(0, 4, 'robot1_acc')
sheet1.write(0, 5, 'robot2_acc')
sheet1.write(0, 6, 'robot3_acc')

#files = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/robot_pointer-8.txt', 'r+')
files = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/robot_listener_velocity-1.txt', 'r+')
R1_v = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R1_v.txt', 'w')
R2_v = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R2_v.txt', 'w')
R3_v = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R3_v.txt', 'w')
R1_a = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R1_a.txt', 'w')
R2_a = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R2_a.txt', 'w')
R3_a = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/R3_a.txt', 'w')

str = files.readline()
count = 1
i = 1
while str:
    if count == 2:
        sheet1.write(i, 0, str)
    if count == 4:
        sheet1.write(i, 1, str)
    if count == 6:
        sheet1.write(i, 2, str)
        R3_v.write(str)
    if count == 8:
        sheet1.write(i, 4, str)
        R1_a.write(str)
    if count == 10:
        sheet1.write(i, 5, str)
        R1_v.write(str)
    if count == 12:
        sheet1.write(i, 6, str)
        R2_v.write(str)
    
    count += 1
    if count == 13:
        count = 1
        i += 1
    str = files.readline()
allxl.save('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/velocity_data/Excel.xls')

files.close()
R1_v.close()
R3_v.close()
R2_v.close()
R2_a.close()
R3_a.close()
R1_a.close()



