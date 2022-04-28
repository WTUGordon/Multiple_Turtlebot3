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
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('item', log_level=rospy.INFO)

    listener = tf.TransformListener() #TransformListener创建后就开始接受tf广播信息，最多可以缓存10s

    rate = rospy.Rate(10.0) #循环执行，更新频率是10hz
    robot1_last = [0, 0, 0]
    robot2_last = [0, 0, 0]
    robot3_last = [0, 0, 0]
    robot1_v_last = 0
    robot2_v_last = 0
    robot3_v_last = 0
    while not rospy.is_shutdown():
        try: 
            (robot1_trans, robot1_rot) = listener.lookupTransform('/robot1/What', '/map', rospy.Time())
            (robot2_trans, robot2_rot) = listener.lookupTransform('/robot2/What', '/map', rospy.Time())
            (robot3_trans, robot3_rot) = listener.lookupTransform('/robot3/What', '/map', rospy.Time())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        robot1_v = math.sqrt((robot1_trans[0] - robot1_last[0]) ** 2 + (robot1_trans[1] - robot1_last[1]) ** 2) * 10
        robot2_v = math.sqrt((robot2_trans[0] - robot2_last[0]) ** 2 + (robot2_trans[1] - robot2_last[1]) ** 2) * 10
        robot3_v = math.sqrt((robot3_trans[0] - robot3_last[0]) ** 2 + (robot3_trans[1] - robot3_last[1]) ** 2) * 10

        robot1_last = robot1_trans
        robot2_last = robot2_trans
        robot3_last = robot3_trans

        robot1_acc = (robot1_v - robot1_v_last) * 10
        robot2_acc = (robot2_v - robot2_v_last) * 10
        robot3_acc = (robot3_v - robot3_v_last) * 10

        robot3_v_last = robot3_v
        robot2_v_last = robot2_v
        robot1_v_last = robot1_v

        rospy.loginfo("Robot1's velocity is \n%f", (robot1_v ))
        rospy.loginfo("Robot2's velocity is \n%f", (robot2_v ))
        rospy.loginfo("Robot3's velocity is \n%f", (robot3_v ))
        rospy.loginfo("Robot1's acceleration is \n%f", (robot1_acc ))
        rospy.loginfo("Robot2's acceleration is \n%f", (robot2_acc ))
        rospy.loginfo("Robot3's acceleration is \n%f", (robot3_acc ))

        
        rate.sleep() #以固定频率执行
    
    