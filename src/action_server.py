import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from example_interfaces.action import Fibonacci  # Replace with your custom action definition
from std_msgs.msg import Int32  # Replace with your topic message type

class CustomActionServer(Node):
    def __init__(self):
        super().__init__('custom_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'custom_action',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )
        self._current_goal_handle = None
        self._subscriber = self.create_subscription(
            Int32,  # Replace with your topic message type
            'goal_topic',
            self.topic_callback,
            10
        )
        self.get_logger().info("Action Server initialized.")

    def goal_callback(self, goal_request):
        self.get_logger().info('Received goal request.')
        return rclpy.action.GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Cancel request received.')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        self._current_goal_handle = goal_handle
        self.get_logger().info(f'Executing goal: {goal_handle.request.order}')
        
        for i in range(5):  # Simulate 5 seconds of work
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled.')
                return Fibonacci.Result()
            self.get_logger().info(f'Processing... {i+1}/5')
            await rclpy.task.sleep(1.0)  # Simulate processing delay
        
        goal_handle.succeed()
        self.get_logger().info('Goal succeeded.')
        return Fibonacci.Result()

    def topic_callback(self, msg):
        if self._current_goal_handle:
            self.get_logger().info('Aborting current goal due to new message.')
            self._current_goal_handle.abort()
        
        new_goal = Fibonacci.Goal()
        new_goal.order = msg.data  # Adapt based on your message type
        self.get_logger().info(f'Sending new goal: {new_goal.order}')

def main(args=None):
    rclpy.init(args=args)
    node = CustomActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
