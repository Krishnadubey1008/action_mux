import rclpy
from rclpy.node import Node

class GenericSubscriber(Node):
    def __init__(self, topic_name, message_type):
        super().__init__('generic_subscriber')
        
        self.subscription = self.create_subscription(
            message_type,
            topic_name,
            self.callback,
            10
        )
        
    def callback(self, msg):
        msg_type = type(msg)
        self.get_logger().info(f'Received message of type {msg_type}: {msg}')

def main(args=None):
    from std_msgs.msg import Int32  # Replace with desired message type
    
    rclpy.init(args=args)
    node = GenericSubscriber('goal_topic', Int32)  # Replace with desired topic name and type
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
