#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial

class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Change the port as needed

        self.get_logger().info('Motor Controller node initialized')

        self.command_sub = self.create_subscription(
            str,
            'motor_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):
        if msg.data in ['W', 'A', 'S', 'D', ' ']:
            self.control_motor(msg.data)
        else:
            self.get_logger().warn('Invalid command: %s', msg.data)

    def control_motor(self, command):
        self.ser.write(command.encode())
        self.get_logger().info('Sent command: %s', command)

def main(args=None):
    rclpy.init(args=args)
    node = MotorControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()