#!/usr/bin/env python
#coding=utf-8

import rospy

import math
import tf
import time
import geometry_msgs.msg
from std_msgs.msg import String
import logging
import sys, select, os
P_LINER_PARAMETER1 =   1.5   #1.5
I_LINER_PARAMETER1 =  0.04  #0.1
P_ANGULAR_PARAMETER1 =  2  #0.8
I_ANGULAR_PARAMETER1 =  0 #0.05
P_LINER_PARAMETER2 =   1.7  #1.5
I_LINER_PARAMETER2 =  0.04  #0.1
P_ANGULAR_PARAMETER2 =  2  #0.8
I_ANGULAR_PARAMETER2 =  0#0.05
D_ANGULAR_PARAMETER = 0
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios


def getKey():
    if os.name == 'nt':
        return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
    
if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('item', log_level=rospy.INFO)

    listener = tf.TransformListener() #TransformListener创建后就开始接受tf广播信息，最多可以缓存10s

    #Publisher 函数第一个参数是话题名称，第二个参数 数据类型，现在就是我们定义的msg 最后一个是缓冲区的大小
    tb3_1_vel = rospy.Publisher('tb3_1/cmd_vel', geometry_msgs.msg.Twist, queue_size=10)
    tb3_2_vel = rospy.Publisher('tb3_2/cmd_vel', geometry_msgs.msg.Twist, queue_size=10)
    rate = rospy.Rate(10.0) #循环执行，更新频率是10hz
    count = 0
    con_flag = 1
    sum_linerror = 0
    sum_angerror = 0
    linear_rho = 0
    angular_rho = 0
    sum_linerror1 = 0
    sum_angerror1 = 0
    linear_rho1 = 0
    angular_rho1 = 0
    con_flag1 = 1
    count1 = 0
    last_angerr = 0
    last_trans0 = 0
    last_trans1 = 0
    key_flag = 0
    while not rospy.is_shutdown():
        try: 
            #得到以tb3_1为坐标原点的tb3_0的姿态信息(平移和旋转)
            (trans, rot) = listener.lookupTransform('/tb3_1/pose', '/tb3_0/pose', rospy.Time()) #查看相对的tf,返回平移和旋转  turtle2跟着turtle1变换
            (trans1,rot1) = listener.lookupTransform('/tb3_2/pose', '/tb3_0/pose', rospy.Time())
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        #trans[0] is x_axis deviation   trans[1] is y_axis deviation
        angular = math.atan2(trans[1] , trans[0] - 0.25) #角度变换 计算出前往tb3_0的角速度 atan2(double y,double x) 返回的是原点至点(x,y)的方位角，即与 x 轴的夹角
        linear = math.sqrt((trans[0] - 0.25) ** 2 + (trans[1]) ** 2) #平移变换 计算出前往tb3_0的线速度
        #linear = (trans[0] - 0.2) + (trans[1])

        angular1 = math.atan2(trans1[1], trans1[0]-0.5)
        linear1 = math.sqrt((trans1[0] - 0.5) ** 2 + (trans1[1]) ** 2)

        msg = geometry_msgs.msg.Twist()
        linear_error = linear      #linear error
        angular_error = angular   #angular error

        key = getKey()
        if (key == '1') : #pause
            con_flag1 = 1
        elif (key == '2') : #connect
            con_flag = 0
            con_flag1 = 0
            sum_error = 0
            sum_linerror = 0
            sum_angerror = 0
            count = 0
            linear_rho = 2 * abs(trans[0] - 0.32) + 0.2
            angular_rho = 2 * abs(trans[1] - 0.3) + 0.2
        elif key == '3': #first start
            con_flag = 0
            sum_linerror = 0
            sum_angerror = 0
            last_angerr = 0
            count = 0
            count1 = 0
            last_trans0 = 0
            last_trans1 = 0
            linear_rho = 2 * (trans[0] - 0.32) + 0.2
            angular_rho = 2 * (trans[1] - 0.3) + 0.2
            linear_rho1 = 2 * (trans1[0] - 0.3) + 0.2
            angular_rho1 = 2 * (trans1[1] + 0.3) + 0.2
            sum_linerror1 = 0
            sum_angerror1 = 0
            con_flag1 = 0
            twist = geometry_msgs.msg.Twist()
            twist.linear.x = 0.1   #0.15
            twist.angular.z = 0.04
        elif key == '4':
            con_flag1 = 1
            con_flag = 1
        else:
            if(key == '\x03'):
                break

        count = count + 1
        count1 = count1 + 1

        linear_r = linear_rho * math.exp(-0.1 * count) + 0.05
        angular_r = angular_rho * math.exp(-0.05 * count) + 0.03
       
        sum_linerror = sum_linerror + linear_error # linear error accumulation
        sum_angerror = sum_angerror + angular_error #anguler error accumulation
        if(sum_linerror > 3): #integral limit
            sum_linerror = 3
        if(sum_angerror > 3):
            sum_angerror = 3
        
        diff_angerror = angular_error - last_angerr
        last_angerr = angular_error
        msg.linear.x = linear_error * P_LINER_PARAMETER1 + sum_linerror * I_LINER_PARAMETER1
        msg.angular.z = angular_error * P_ANGULAR_PARAMETER1 + sum_angerror * I_ANGULAR_PARAMETER1 + diff_angerror * D_ANGULAR_PARAMETER
       
        if(msg.linear.x > 0.3):
            msg.linear.x = 0.3
        if(msg.linear.x < -0.3):
            msg.linear.x = -0.3
        if(msg.angular.z > 0.3):
            msg.angular.z = 0.3
        if(msg.angular.z < -0.3):
            msg.angular.z = -0.3

        if(con_flag > 0):  #uncontinuous flag  publish zero
            msg.linear.x = 0
            msg.angular.z = 0


        msg1 = geometry_msgs.msg.Twist()

        linear_r1 = linear_rho1 * math.exp(-0.1 * count1) + 0.05
        angular_r1 = angular_rho1 * math.exp(-0.05 * count1) + 0.03

        sum_linerror1 = sum_linerror1 + linear1 # linear error accumulation
        sum_angerror1 = sum_angerror1 + angular1 #anguler error accumulation

        if(sum_linerror1 > 3): #integral limit
            sum_linerror1 = 3
        if(sum_linerror1 < -3): #integral limit
            sum_linerror1 = -3
        if(sum_angerror1 > 3):
            sum_angerror1 = 3
        if(sum_angerror1 < -3):
            sum_angerror1 = -3

        msg1.linear.x = linear1 * P_LINER_PARAMETER2 + sum_linerror1 * I_LINER_PARAMETER2
        msg1.angular.z = angular1 * P_ANGULAR_PARAMETER2 + sum_angerror1 * I_ANGULAR_PARAMETER2

        if(msg1.linear.x > 0.3):
            msg1.linear.x = 0.3
        if(msg1.linear.x < -0.3):
            msg1.linear.x = -0.3
        if(msg1.angular.z > 0.3):
            msg1.angular.z = 0.3
        if(msg1.angular.z < -0.3):
            msg1.angular.z = -0.3
        
        left1 = msg.linear.x + msg.angular.z
        right1 = msg.linear.x - msg.angular.z
        left2 = msg1.linear.x + msg1.angular.z
        right2 = msg1.linear.x - msg1.angular.z
        # if(count1 > 100):
        #     msg1.linear.x = msg1.linear.x * 0.6 + 0.02 + 0.01 * math.cos(0.01 * count1)
        #     msg1.angular.z = msg1.angular.z * 0.8 + 0.002 + 0.002 * math.sin(0.01 * count1)
        #     I_LINER_PARAMETER2 = 0.05
        # if(count1 > 100):
        #     left2 = left2 * 0.5 + 0.01 + 0.01 * math.cos(0.01 * count1)
        #     right2 = right2 * 0.8 + 0.002 + 0.002 * math.sin(0.01 * count1)

        if(con_flag1 > 0):  #uncontinuous flag  publish zero
            msg1.linear.x = 0
            msg1.angular.z = 0

        if ((count%1) == 0):  #1s period
            
            rospy.loginfo("liner error is \n%f", linear_error)
            if(con_flag > 0):
                rospy.loginfo("angular error error error is \n%f", (0.0))
            else:
                rospy.loginfo("angular error error error is \n%f", angular_error)
            rospy.loginfo("linear integral error is \n%f", sum_linerror)
            rospy.loginfo("angular integral error is \n%f", sum_angerror)
            rospy.loginfo("linear constrains is \n%f", linear_r)
            rospy.loginfo("angular constrains is \n%f", angular_r)
            if(con_flag > 0):
                rospy.loginfo("Trans_0 is \n%f", (0.0))
                rospy.loginfo("Trans_1 is \n%f", (0.0))
            else:
                rospy.loginfo("Trans_0 is \n%f", (trans[0] ))
                rospy.loginfo("Trans_1 is \n%f", (trans[1] ))
            
            rospy.loginfo("liner error is \n%f", linear1)
            if(con_flag1 > 0):
                rospy.loginfo("angular error error error is \n%f", (0.0))
            else:
                rospy.loginfo("angular error error error is \n%f", angular1)
            rospy.loginfo("linear integral error is \n%f", sum_linerror1)
            rospy.loginfo("angular integral error is \n%f", sum_angerror1)
            rospy.loginfo("linear constrains is \n%f", linear_r1)
            rospy.loginfo("angular constrains is \n%f", angular_r1)
            if(con_flag1 > 0):
                rospy.loginfo("Trans_0 is \n%f", (0.0))
                rospy.loginfo("Trans_1 is \n%f", (0.0))
            else:
                rospy.loginfo("Trans1_0 is \n%f", (trans1[0] ))
                rospy.loginfo("Trans1_1 is \n%f", (trans1[1] )) 
            rospy.loginfo("msg linear1 is \n%f", left1)
            rospy.loginfo("msg linear2 is \n%f", right1)
            rospy.loginfo("msg1 linear1 is \n%f", left2)
            rospy.loginfo("msg1 linear2 is \n%f", right2)
        

        
        tb3_2_vel.publish(msg1)
        tb3_1_vel.publish(msg) #向/tb3_1/cmd_vel话题发布新坐标  (即tb3_1根据/tb3_1/cmd_vel的数据来控制tb3_1移动)
        
        rate.sleep() #以固定频率执行
        
        
