#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/Twist.h>
#include <turtlesim/Spawn.h>
#include <math.h>
#include <std_msgs/Float64MultiArray.h>

#define Constrain(value, max, min)  ((value) > (max) ? (max) : ((value) < (min) ? (min) : (value)))
bool robot0_flag = false;   //robot0启动的标志位
typedef struct PID_Param Turtle_Param;
typedef struct Error Turtle_Error;
struct PID_Param
{
    double P;
    double I;
    double D;
//构造函数初始化结构体
    PID_Param(){
        P = 0;
        I = 0;
        D = 0;
    }
};
struct Error
{
    double error;
    double last_error;
    double sum_error;
    double sum_max;
    double sum_min;
//构造函数初始化结构体
    Error(){
        error = 0;
        last_error = 0;
        sum_error = 0;
        sum_max = 65535;
        sum_min = -65535;
    }
};
class Turtlebot_Trans
{
    public:
        Turtlebot_Trans() = default;
        Turtlebot_Trans(const double offset_x, const double offset_y) : 
            offset_x (offset_x), offset_y (offset_y) { }
        double linerr () const
            { return sqrt(pow(trans_x - offset_x, 2) + pow(trans_y - offset_y, 2)); }
        double angerr() const
            { return atan2(trans_y - offset_y, trans_x - offset_x); }
        double trans_x, trans_y;
    private:
        double offset_x, offset_y;
};
double Control_PID ( const Turtle_Param * PID, Turtle_Error * Err)
{
    double value;
    value = PID->P * Err->error + 
                    PID->I * Err->sum_error +
                    PID->D * (Err->error - Err->last_error);
    Err->last_error = Err->error;
    Err->sum_error += Err->error;
    Err->sum_error = Constrain(Err->sum_error, Err->sum_max, Err->sum_min);
    return value;
}
void Callback(const geometry_msgs::Twist::ConstPtr & msgs)
{
    ROS_INFO("robot0 starting!\n");
    robot0_flag = true;
}

int main (int argc, char ** argv)
{
    ros::init(argc, argv, "tb1_listener");
    ros::NodeHandle node("~");
    //定义变量
    tf::TransformListener listener;
    ros::Publisher pub = node.advertise<std_msgs::Float64MultiArray>("text_vel", 100);
    ros::Subscriber sub_cmdvel = node.subscribe("/tb3_0/cmd_vel", 1000, Callback);
    double offset_x, offset_y, linear_max, angular_max;
    
    std::string tb_name;
    Turtle_Param LinPar;
    Turtle_Param AngPar;
    Turtle_Error LinErr;
    Turtle_Error AngErr;
    //获取参数
    node.getParam("tb_param", tb_name);
    node.getParam("linear_x_max", linear_max);
    node.getParam("angular_z_max",angular_max );
    node.getParam("P_lin", LinPar.P);
    node.getParam("I_lin", LinPar.I);
    node.getParam("D_lin", LinPar.D);
    node.getParam("P_ang", AngPar.P);
    node.getParam("I_ang", AngPar.I);
    node.getParam("D_ang", AngPar.D);
    node.getParam("offset_x", offset_x);
    node.getParam("offset_y", offset_y);
    node.getParam("linerr_max", LinErr.sum_max);
    node.getParam("angerr_max", AngErr.sum_max);
    LinErr.sum_min = -LinErr.sum_max;
    AngErr.sum_min = -AngErr.sum_min;
    Turtlebot_Trans Turtle(offset_x, offset_y);
    ros::Publisher pub_vel = node.advertise<geometry_msgs::Twist>("/"+tb_name+"/cmd_vel", 100);
    while (! robot0_flag) //阻塞，判断第一个机器人是否开始运动
    {
        ros::spinOnce();
    }
    
    listener.waitForTransform(tb_name+"/pose", "/tb3_0/pose", ros::Time(0), ros::Duration(3.0) );
    ros::Rate rate(7);
    while(node.ok())
    {
        tf::StampedTransform transform;
        try{
            listener.waitForTransform(tb_name+"/pose", "/tb3_0/pose", ros::Time(0), ros::Duration(3.0) );
            listener.lookupTransform(tb_name+"/pose", "/tb3_0/pose", ros::Time(0), transform);
        }
        catch (tf::TransformException & ex){
            ROS_ERROR("%s", ex.what());
            ros::Duration(1).sleep();
            continue;
        }
        Turtle.trans_x = transform.getOrigin().x();
        Turtle.trans_y = transform.getOrigin().y();
        LinErr.error = Turtle.linerr();
        AngErr.error = Turtle.angerr();
        std_msgs::Float64MultiArray array;
        array.data.push_back(Control_PID(&LinPar, &LinErr));
        array.data.push_back(Control_PID(&AngPar, &AngErr));
        geometry_msgs::Twist msg_twist;
        msg_twist.angular.z = Constrain(array.data[1], angular_max, -angular_max);
        msg_twist.linear.x = Constrain(array.data[0], linear_max, -linear_max);
        pub_vel.publish(msg_twist);
        pub.publish(array);
        ROS_INFO("x is %lf \n", transform.getOrigin().x());
        ROS_INFO("y is %lf \n", transform.getOrigin().y());
        rate.sleep();
    }
    return 0;
}
