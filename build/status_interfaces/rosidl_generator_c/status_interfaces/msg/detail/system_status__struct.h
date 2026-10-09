// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from status_interfaces:msg/SystemStatus.idl
// generated code does not contain a copyright notice

#ifndef STATUS_INTERFACES__MSG__DETAIL__SYSTEM_STATUS__STRUCT_H_
#define STATUS_INTERFACES__MSG__DETAIL__SYSTEM_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'host_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/SystemStatus in the package status_interfaces.
typedef struct status_interfaces__msg__SystemStatus
{
  /// create time_sets
  builtin_interfaces__msg__Time stamp;
  /// system's name
  rosidl_runtime_c__String host_name;
  /// the usage rate of cpu
  float cpu_percent;
  /// the usage rate of internal storage
  float memory_percent;
  /// the total capacity of internal storage
  float memory_total;
  /// the remain available internal storage
  float memory_available;
  /// the total amount of data sent over the network
  double net_sent;
  /// the total amount of data received over the network
  double met_recv;
} status_interfaces__msg__SystemStatus;

// Struct for a sequence of status_interfaces__msg__SystemStatus.
typedef struct status_interfaces__msg__SystemStatus__Sequence
{
  status_interfaces__msg__SystemStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} status_interfaces__msg__SystemStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // STATUS_INTERFACES__MSG__DETAIL__SYSTEM_STATUS__STRUCT_H_
