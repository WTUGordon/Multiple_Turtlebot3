#include<ros/ros.h>
#include<multiple_turtlebot3_cpp/Interruption.h>

bool delay (multiple_turtlebot3_cpp::Interruption::Request &req,
                        multiple_turtlebot3_cpp::Interruption::Response &res)
{
    bool inter_flag;
    ros::param::get("/tb2_listener/interruption_flag", inter_flag);
    if(!inter_flag)
        ros::param::set("/tb2_listener/interruption_flag", true);
    else
        return false;
    ros::param::get("/tb2_listener/interruption_flag", inter_flag);
    ROS_INFO("Interruption starting %d, time is %lf \n", inter_flag,  req.time);
    ros::Duration(req.time).sleep();
    res.time = req.time;
    res.success = true;
    ros::param::set("/tb2_listener/interruption_flag", false);
    ROS_INFO("Interruption ending \n");
    return true;
}
int main (int argc, char ** argv)
{
    ros::init(argc, argv, "delay_server");
    ros::NodeHandle node;
    ros::ServiceServer server = node.advertiseService("delay", delay);
    ROS_INFO("Ready to delay \n");
    ros::spin();
    return 0;
}
