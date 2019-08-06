// Generated by gencpp from file begginer_tutorials/AddTwoInts.msg
// DO NOT EDIT!


#ifndef BEGGINER_TUTORIALS_MESSAGE_ADDTWOINTS_H
#define BEGGINER_TUTORIALS_MESSAGE_ADDTWOINTS_H

#include <ros/service_traits.h>


#include <begginer_tutorials/AddTwoIntsRequest.h>
#include <begginer_tutorials/AddTwoIntsResponse.h>


namespace begginer_tutorials
{

struct AddTwoInts
{

typedef AddTwoIntsRequest Request;
typedef AddTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTwoInts
} // namespace begginer_tutorials


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::begginer_tutorials::AddTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::begginer_tutorials::AddTwoInts&) { return value(); }
};

template<>
struct DataType< ::begginer_tutorials::AddTwoInts > {
  static const char* value()
  {
    return "begginer_tutorials/AddTwoInts";
  }

  static const char* value(const ::begginer_tutorials::AddTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::begginer_tutorials::AddTwoIntsRequest> should match 
// service_traits::MD5Sum< ::begginer_tutorials::AddTwoInts > 
template<>
struct MD5Sum< ::begginer_tutorials::AddTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::begginer_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::begginer_tutorials::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::begginer_tutorials::AddTwoIntsRequest> should match 
// service_traits::DataType< ::begginer_tutorials::AddTwoInts > 
template<>
struct DataType< ::begginer_tutorials::AddTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::begginer_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::begginer_tutorials::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::begginer_tutorials::AddTwoIntsResponse> should match 
// service_traits::MD5Sum< ::begginer_tutorials::AddTwoInts > 
template<>
struct MD5Sum< ::begginer_tutorials::AddTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::begginer_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::begginer_tutorials::AddTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::begginer_tutorials::AddTwoIntsResponse> should match 
// service_traits::DataType< ::begginer_tutorials::AddTwoInts > 
template<>
struct DataType< ::begginer_tutorials::AddTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::begginer_tutorials::AddTwoInts >::value();
  }
  static const char* value(const ::begginer_tutorials::AddTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // BEGGINER_TUTORIALS_MESSAGE_ADDTWOINTS_H