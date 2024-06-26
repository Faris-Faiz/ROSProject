#!/usr/bin/env python

import rospy
from robot_control_msgs.msg import Feedback  # Assuming Feedback message type

def callback(msg):
    if msg.action == "detect" and msg.target == "object":
        rospy.loginfo("Received target object: {}".format(msg.results.object.name))

def relay_node():
    rospy.init_node('relay_node', anonymous=True)
    rospy.Subscriber("/vision_to_control", Feedback, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        relay_node()
    except rospy.ROSInterruptException:
        pass

