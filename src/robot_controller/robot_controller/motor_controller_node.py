#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String

class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change the port as needed

        self.get_logger().info('Motor Controller node initialized')

        self.command_sub = self.create_subscription(
            String,
            'motor_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg: String):
        self.control_motor(msg.data)
        print(f'Pressed key: {msg.data}')

    def control_motor(self, command):
        self.ser.write(command.encode())
        #print(f'Sending data: {command}')

def main(args=None):
    rclpy.init(args=args)
    node = MotorControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()