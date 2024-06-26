#!/usr/bin/env python

import rospy

def read_and_publish():
    file_path = "yolo_output_test.txt"  # Update this with your actual file path
    try:
        with open(file_path, 'r') as file:
            for line in file:
                rospy.loginfo(line.strip())  # Log each line to ROS
                print(line.strip())  # Print each line to terminal
    except IOError:
        rospy.logerr("Failed to read file: {}".format(file_path))

if __name__ == '__main__':
    rospy.init_node('output_reader_node', anonymous=True)
    read_and_publish()

