import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  # Replace with desired message type

class TestPublisher(Node):
    def __init__(self):
        super().__init__('test_publisher')
        
        self.publisher = self.create_publisher(Int32, 'goal_topic', 10)
        
    def publish_message(self, data):
        msg = Int32()
        msg.data = data  # Adapt based on your message type
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TestPublisher()
    
    try:
        while True:
            data = int(input("Enter a number to publish: "))
            node.publish_message(data)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()
