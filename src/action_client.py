import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from example_interfaces.action import Fibonacci  # Replace with your custom action definition

class CustomActionClient(Node):
    def __init__(self):
        super().__init__('custom_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'custom_action')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        
        self._action_client.wait_for_server()
        future = self._action_client.send_goal_async(goal_msg)
        
        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        result = future.result()
        if not result.accepted:
            self.get_logger().info('Goal rejected.')
            return
        
        self.get_logger().info('Goal accepted.')

def main(args=None):
    rclpy.init(args=args)
    node = CustomActionClient()
    node.send_goal(10)  # Example goal value
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
