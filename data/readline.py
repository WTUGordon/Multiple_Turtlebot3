# -*- coding: UTF-8 -*-

import xlwt
allxl = xlwt.Workbook()
sheet1 = allxl.add_sheet('Sheet1')
sheet1.write(0, 0, 'liner_error')
sheet1.write(0, 1, 'angular_error')
sheet1.write(0, 2, 'liner_con')
sheet1.write(0, 4, 'angular_con')
sheet1.write(0, 3, 'Trans_0')
sheet1.write(0, 5, 'Trans_1')

sheet1.write(0, 6, '1liner_error')
sheet1.write(0, 7, '1angular_error')
sheet1.write(0, 8, '1liner_con')
sheet1.write(0, 9, '1angular_con')
sheet1.write(0, 10, '1Trans_0')
sheet1.write(0, 11, '1Trans_1')

sheet1.write(0, 13, '1lift')
sheet1.write(0, 14, '1right')
sheet1.write(0, 15, '2lift')
sheet1.write(0, 16, '2right')
#files = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/robot_pointer-8.txt', 'r+')
files = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/robot_listener-1.txt', 'r+')
Trans0 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/trans0.txt', 'w')
Trans1 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/trans1.txt', 'w')
Trans0_con = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/trans0_con.txt', 'w')
Trans1_con = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/trans1_con.txt', 'w')

Trans01 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1trans0.txt', 'w')
Trans11 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1trans1.txt', 'w')
Trans0_con1 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1trans0_con.txt', 'w')
Trans1_con1 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1trans1_con.txt', 'w')

lift1 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1lift.txt', 'w')
right1 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/1right.txt', 'w')
lift2 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/2lift.txt', 'w')
right2 = open('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/2right.txt', 'w')

str = files.readline()
count = 1
i = 1
while str:
    if count == 2:
        sheet1.write(i, 0, str)
    if count == 4:
        sheet1.write(i, 1, str)
    if count == 10:
        sheet1.write(i, 2, str)
        Trans0_con.write(str)
    if count == 12:
        sheet1.write(i, 4, str)
        Trans1_con.write(str)
    if count == 14:
        sheet1.write(i, 3, str)
        Trans0.write(str)
    if count == 16:
        sheet1.write(i, 5, str)
        Trans1.write(str)
    
    if count == 18:
        sheet1.write(i, 6, str)
    if count == 20:
        sheet1.write(i, 7, str)
    if count == 26:
        sheet1.write(i, 8, str)
        Trans0_con1.write(str)
    if count == 28:
        sheet1.write(i, 10, str)
        Trans1_con1.write(str)
    if count == 30:
        sheet1.write(i, 9, str)
        Trans01.write(str)
    if count == 32:
        sheet1.write(i, 11, str)
        Trans11.write(str)

    if count == 34:
        sheet1.write(i, 13, str)
    if count == 36:
        sheet1.write(i, 14, str)
    if count == 38:
        sheet1.write(i, 15, str)
    if count == 40:
        sheet1.write(i, 16, str)
    count += 1
    if count == 41:
        count = 1
        i += 1
    str = files.readline()
allxl.save('/home/zch/catkin_ws/src/multi_turtlebot3/multi_turtlebot3_navigation/data/Excel.xls')

files.close()
Trans0.close()
Trans0_con.close()
Trans1.close()
Trans1_con1.close()
Trans01.close()
Trans0_con1.close()
Trans11.close()
Trans1_con1.close()
lift1.close()
right1.close()
lift2.close()
right2.close()


