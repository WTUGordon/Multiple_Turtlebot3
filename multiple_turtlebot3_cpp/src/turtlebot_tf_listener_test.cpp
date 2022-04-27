#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/Twist.h>
#include <turtlesim/Spawn.h>

int main (int argc, char ** argv)
{
    ros::init(argc, argv, "listener");
    ros::NodeHandle n;
    tf::TransformListener listener;
    tf::StampedTransform transform;
    listener.waitForTransform("/tb3_1/pose", "/tb3_0/pose", ros::Time(0), ros::Duration(3.0));
    ros::Rate rate(10);
    while(n.ok())
    {
        try{
            listener.waitForTransform("/tb3_1/pose", "/tb3_0/pose", ros::Time(0), ros::Duration(3.0));
            listener.lookupTransform("/tb3_1/pose", "/tb3_0/pose", ros::Time(0), transform);
        }
        catch (tf::TransformException & ex){
            ROS_ERROR("%s", ex.what());
            ros::Duration(1).sleep();
            continue;
        }
        ROS_INFO("x is %lf \n", transform.getOrigin().x());
        rate.sleep();
    }
    return 0;
}

