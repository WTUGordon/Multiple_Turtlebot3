#include<ros/ros.h>
#include<cstdlib>
#include<multiple_turtlebot3_cpp/Interruption.h>

int main (int argc, char ** argv)
{
    ros::init(argc, argv, "delay_client");
    ros::NodeHandle node;
    ros::ServiceClient client  = node.serviceClient<multiple_turtlebot3_cpp::Interruption>("delay");
    multiple_turtlebot3_cpp::Interruption delay_srv;
    delay_srv.request.time = atof(argv[1]);
    if(client.call(delay_srv))
        ROS_INFO("Interruption Success %d, Delay Time %f \n",delay_srv.response.success, delay_srv.response.time);
    else
        ROS_INFO("Failed to call delay_service \n");
    return  0;
}