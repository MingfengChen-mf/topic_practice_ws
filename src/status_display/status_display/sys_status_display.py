import sys
import rclpy
from rclpy.node import Node
from status_interfaces.msg import SystemStatus
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import QTimer, Qt


class SysStatusDisplay(Node):
    def __init__(self, app):
        super().__init__('sys_status_display')
        self.app = app
        self.subscription = self.create_subscription(
            SystemStatus,
            'sys_status',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Initialize the PyQt5 label to visualize the system status
        self.label = QLabel('Waiting for status...')
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setStyleSheet('font-family: Monospace; font-size: 14px;')
        self.label.setMinimumSize(520, 260)
        self.label.show()

        # Process Qt events periodically so the window stays responsive
        self.qt_timer = QTimer()
        self.qt_timer.timeout.connect(self.app.processEvents)
        self.qt_timer.start(100)  # every 100 ms

    def listener_callback(self, msg):
        status_text = (f'======== Visualization of System Status ========\n'
                       f'Data Timestamp:         {msg.stamp.sec}.{msg.stamp.nanosec:09d} s\n'
                       f'Host Name:              {msg.host_name}\n'
                       f'CPU Usage:              {msg.cpu_percent:.2f} %\n'
                       f'Memory Usage:           {msg.memory_percent:.2f} %\n'
                       f'Total Memory:           {msg.memory_total:.2f} MB\n'
                       f'Available Memory:       {msg.memory_available:.2f} MB\n'
                       f'Network Data Sent:      {msg.net_sent:.2f} MB\n'
                       f'Network Data Received:  {msg.net_recv:.2f} MB')
        self.get_logger().info(status_text)
        self.label.setText(status_text)


def main(args=None):
    rclpy.init(args=args)
    app = QApplication(sys.argv)

    sys_status_display = SysStatusDisplay(app)

    # Spin ROS 2 in the Qt event loop so both stay responsive
    ros_timer = QTimer()
    ros_timer.timeout.connect(
        lambda: rclpy.spin_once(sys_status_display, timeout_sec=0))
    ros_timer.start(100)  # every 100 ms

    exit_code = app.exec_()
    sys_status_display.destroy_node()
    rclpy.shutdown()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
