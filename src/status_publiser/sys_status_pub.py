import rclpy
import psutil 
import platform
from rclpy.node import Node
from status_interfaces.msg import SysStatus

class SysStatusPub(Node):
    def __init__(self):
        super().__init__('sys_status_pub')
        self.publisher_ = self.create_publisher(SysStatus, 'sys_status', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        cpu_percent = psutil.cpu_percent()
        memory_info= psutil.virtual_memory()
        net_io_counters = psutil.net_io_counters()

        msg= SysStatus()
        msg.stamp = self.get_clock().now().to_msg()
        msg.hostname = platform.node()
        msg.cpu_percent = cpu_percent
        msg.memory_percent = memory_info.percent
        msg.memory_total = memory_info.total / 1024 / 1024  # Convert to MB
        msg.memory_available = memory_info.available / 1024 / 1024  # Convert to MB
        msg.net_sent = net_io_counters.bytes_sent / 1024 / 1024  # Convert to MB
        msg.net_recv = net_io_counters.bytes_recv / 1024 / 1024  # Convert to MB

        self.get_logger().info(f'Publishing: {str(msg)}')
        self.status_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    sys_status_pub = SysStatusPub()
    rclpy.spin(sys_status_pub)
    rclpy.shutdown()