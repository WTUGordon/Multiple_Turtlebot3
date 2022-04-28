// Generated by gencpp from file multiple_turtlebot3_cpp/InterruptionRequest.msg
// DO NOT EDIT!


#ifndef MULTIPLE_TURTLEBOT3_CPP_MESSAGE_INTERRUPTIONREQUEST_H
#define MULTIPLE_TURTLEBOT3_CPP_MESSAGE_INTERRUPTIONREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace multiple_turtlebot3_cpp
{
template <class ContainerAllocator>
struct InterruptionRequest_
{
  typedef InterruptionRequest_<ContainerAllocator> Type;

  InterruptionRequest_()
    : time(0.0)  {
    }
  InterruptionRequest_(const ContainerAllocator& _alloc)
    : time(0.0)  {
  (void)_alloc;
    }



   typedef double _time_type;
  _time_type time;





  typedef boost::shared_ptr< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> const> ConstPtr;

}; // struct InterruptionRequest_

typedef ::multiple_turtlebot3_cpp::InterruptionRequest_<std::allocator<void> > InterruptionRequest;

typedef boost::shared_ptr< ::multiple_turtlebot3_cpp::InterruptionRequest > InterruptionRequestPtr;
typedef boost::shared_ptr< ::multiple_turtlebot3_cpp::InterruptionRequest const> InterruptionRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator1> & lhs, const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator2> & rhs)
{
  return lhs.time == rhs.time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator1> & lhs, const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace multiple_turtlebot3_cpp

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "be5310e7aa4c90cdee120add91648cee";
  }

  static const char* value(const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbe5310e7aa4c90cdULL;
  static const uint64_t static_value2 = 0xee120add91648ceeULL;
};

template<class ContainerAllocator>
struct DataType< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "multiple_turtlebot3_cpp/InterruptionRequest";
  }

  static const char* value(const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 time\n"
;
  }

  static const char* value(const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct InterruptionRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::multiple_turtlebot3_cpp::InterruptionRequest_<ContainerAllocator>& v)
  {
    s << indent << "time: ";
    Printer<double>::stream(s, indent + "  ", v.time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MULTIPLE_TURTLEBOT3_CPP_MESSAGE_INTERRUPTIONREQUEST_H