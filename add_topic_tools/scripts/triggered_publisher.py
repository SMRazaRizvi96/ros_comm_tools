#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image

class TriggeredPublisher:
    def __init__(self):
        rospy.init_node('triggered_publisher_node')

        input_topic_name = rospy.get_param('~input_topic', '/camera/image_raw')
        output_topic_name = rospy.get_param('~output_topic', '/camera/image_raw/triggered')

        self.sub = rospy.Subscriber(input_topic_name, Image, self.callback)
        self.pub = rospy.Publisher(output_topic_name, Image, queue_size=10)

        self.last_img_msg = None

    def callback(self, msg):
        self.last_img_msg = msg

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            try:
                input("Press Enter to publish the last received image or Ctrl+C to exit...\n")
                if self.last_img_msg is not None:
                    self.pub.publish(self.last_img_msg)
            except KeyboardInterrupt:
                break
            rate.sleep()

if __name__ == "__main__":
    node = TriggeredPublisher()
    node.run()
