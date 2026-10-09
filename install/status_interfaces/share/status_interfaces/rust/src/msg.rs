#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to status_interfaces__msg__SystemStatus

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SystemStatus {
    /// create time_sets
    pub stamp: builtin_interfaces::msg::Time,

    /// system's name
    pub host_name: std::string::String,

    /// the usage rate of cpu
    pub cpu_percent: f32,

    /// the usage rate of internal storage
    pub memory_percent: f32,

    /// the total capacity of internal storage
    pub memory_total: f32,

    /// the remain available internal storage
    pub memory_available: f32,

    /// the total amount of data sent over the network
    pub net_sent: f64,

    /// the total amount of data received over the network
    pub met_recv: f64,

}



impl Default for SystemStatus {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SystemStatus::default())
  }
}

impl rosidl_runtime_rs::Message for SystemStatus {
  type RmwMsg = super::msg::rmw::SystemStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
        host_name: msg.host_name.as_str().into(),
        cpu_percent: msg.cpu_percent,
        memory_percent: msg.memory_percent,
        memory_total: msg.memory_total,
        memory_available: msg.memory_available,
        net_sent: msg.net_sent,
        met_recv: msg.met_recv,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
        host_name: msg.host_name.as_str().into(),
      cpu_percent: msg.cpu_percent,
      memory_percent: msg.memory_percent,
      memory_total: msg.memory_total,
      memory_available: msg.memory_available,
      net_sent: msg.net_sent,
      met_recv: msg.met_recv,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
      host_name: msg.host_name.to_string(),
      cpu_percent: msg.cpu_percent,
      memory_percent: msg.memory_percent,
      memory_total: msg.memory_total,
      memory_available: msg.memory_available,
      net_sent: msg.net_sent,
      met_recv: msg.met_recv,
    }
  }
}


