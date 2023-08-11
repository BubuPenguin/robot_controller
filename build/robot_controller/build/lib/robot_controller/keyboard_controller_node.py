#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import termios
import tty

class KeyboardControllerNode(Node):
    def __init__(self):
        super().__init__('keyboard_controller')
        self.publisher_ = self.create_publisher(String, 'motor_command', 10)
        self.get_logger().info('Keyboard Controller node initialized')

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        while rclpy.ok():
            key = self.get_key()

            if ord(key) == 27:  # Check if the key is "Esc" (ASCII code 27)
                print("Esc key pressed. Exiting...")
                break

            if key == 'w':
                msg = String()
                msg.data = 'W'
                self.publisher_.publish(msg)
            elif key == 's':
                msg = String()
                msg.data = 'S'
                self.publisher_.publish(msg)
            elif key == 'a':
                msg = String()
                msg.data = 'A'
                self.publisher_.publish(msg)
            elif key == 'd':
                msg = String()
                msg.data = 'D'
                self.publisher_.publish(msg)
            elif key == ' ':
                msg = String()
                msg.data = ' '
                self.publisher_.publish(msg)

            # Print the pressed key to the terminal
            print(f'Pressed key: {key}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControllerNode()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
