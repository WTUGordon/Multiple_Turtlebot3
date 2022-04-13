# multi_turtlebot3_navigation


这是三辆Turtlebot3-Burger机器人做的领导跟随控制，Gazebo建立地图后，用一个机器人SLAM建图。 之后在地图上加载三辆Burger。 领导者接受路径规划算法，采用A-star和DWA结合的规划算法，指定目标点后，规划算法为领导者计算出合适路径，领导者开始移动。 两个Burger作为跟随者，初始位置随机，启动后马上跟随领导者运行，并保持固定间距。 中间一个Burger会通讯中断停止不动，几秒钟后恢复动力会马上追上前面的车队。
