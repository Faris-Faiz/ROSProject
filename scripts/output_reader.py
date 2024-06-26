#!/usr/bin/env python

import rospy

def read_and_publish():
    file_path = "yolo_output_test.txt"  # Update this with your actual file path
    keywords = ['banana', 'apple', 'orange', 'broccoli', 'carrot']
    last_item = None

    try:
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.split(']: ')[-1].strip()  # Remove the '[INFO] []' part
                for keyword in keywords:
                    if keyword in cleaned_line:
                        item_name = keyword.capitalize()  # Capitalize the first letter
                        if item_name != last_item:
                            last_item = item_name
                            rospy.loginfo(item_name)  # Log item name to ROS
                            print(item_name)  # Print item name to terminal
                            break  # Exit the keyword loop once a match is found
    except IOError:
        rospy.logerr("Failed to read file: {}".format(file_path))

if __name__ == '__main__':
    rospy.init_node('output_reader_node', anonymous=True)
    read_and_publish()

