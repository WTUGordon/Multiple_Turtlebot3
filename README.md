# multi_turtlebot3_navigation
四个终端运行：  
roslaunch multiple_turtlebot3_cpp multi_turtlebot3_gazebo.launch   
roslaunch multiple_turtlebot3_cpp navigation_three.launch  
roslaunch multiple_turtlebot3_cpp broadcaster.launch  
roslaunch multiple_turtlebot3_cpp running.launch

这是三辆Turtlebot3-Burger机器人做的领导跟随控制，Gazebo建立地图后，用一个机器人SLAM建图。 之后在地图上加载三辆Burger。 领导者接受路径规划算法，采用A-star和DWA结合的规划算法，指定目标点后，规划算法为领导者计算出合适路径，领导者开始移动。 两个Burger作为跟随者，初始位置随机，启动后马上跟随领导者运行，并保持固定间距。 

想要中断功能，再打开两个终端分别执行：
rosrun multiple_turtlebot3_cpp Delay_Server.cpp
rosrun multiple_turtlebot3_cpp Delay_Client.cpp 2.23
2.23表示第二个Burger中断时间（秒），2.23s后重新启动并追上前面的车队。
注意：如果中断时间过长，Burger可能永远无法追上了。