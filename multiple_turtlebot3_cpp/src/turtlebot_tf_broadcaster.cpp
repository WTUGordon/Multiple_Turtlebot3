#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <turtlesim/Pose.h>
#include <sstream>
#include <nav_msgs/Odometry.h>
std::string tb_name;
void Callback( const  nav_msgs::OdometryConstPtr& msg)
{
  static tf::TransformBroadcaster br;
  geometry_msgs::TransformStamped stam_trans;
  stam_trans.header.stamp = ros::Time::now();
  stam_trans.header.frame_id = "/map";
  stam_trans.child_frame_id = tb_name+"/pose";
  stam_trans.transform.translation.x = msg->pose.pose.position.x;
  stam_trans.transform.translation.y = msg->pose.pose.position.y;
  stam_trans.transform.translation.z = 0.0;
  stam_trans.transform.rotation.x = msg->pose.pose.orientation.x;
  stam_trans.transform.rotation.y = msg->pose.pose.orientation.y;
  stam_trans.transform.rotation.z = msg->pose.pose.orientation.z;
  stam_trans.transform.rotation.w = msg->pose.pose.orientation.w;
  br.sendTransform(stam_trans);
}
int main (int argc, char ** argv)
{
  ros::init(argc, argv, "broadcaster_tf");
  ros::NodeHandle node("~");
  node.getParam("tb_param", tb_name);
  ROS_INFO("turtlebot_name is %s", tb_name.c_str());
  ros::Subscriber sub = node.subscribe(tb_name+"/odom", 100, &Callback);
  ros::spin();
  return 0;
}


