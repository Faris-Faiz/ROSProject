#!/usr/bin/env python

import rospy
from std_msgs.msg import String

found_keywords = []  # List to store found keywords

def read_and_store():
    file_path = "/home/mustar/catkin_ws/src/ROSProject-main/scripts/text_files/yolo_output_test.txt"  # Update with your file path
    keywords = ['banana', 'apple', 'orange', 'broccoli', 'carrot']
    last_item = None

    try:
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.split(']: ')[-1].strip()  # Remove '[INFO] []'
                for keyword in keywords:
                    if keyword in cleaned_line:
                        item_name = keyword.capitalize()  # Capitalize first letter
                        if item_name != last_item:
                            last_item = item_name
                            found_keywords.append(item_name)  # Store keyword
                            break  # Exit keyword loop once found
    except IOError:
        rospy.logerr("Failed to read file: {}".format(file_path))

def generate_prompt(keyword):
    return "What are the Health Benefits and Nutritional Values of the fruit/vegetable {}? Please summarize to 2 sentences.".format(keyword.capitalize())

def talker():
    pub = rospy.Publisher('chatgpt_input', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown() and found_keywords:
        keyword = found_keywords.pop(0)  # Get and remove first keyword
        prompt = generate_prompt(keyword)
        rospy.loginfo("Publishing prompt: {}".format(prompt))
        pub.publish(prompt)
        rate.sleep()

    rospy.loginfo("No more keywords found or ROS shutdown.")

if __name__ == '__main__':
    rospy.init_node('input_publisher', anonymous=True)  # Initialize node with a unique name
    read_and_store()  # Read file and store found keywords
    talker()  # Publish prompts with keywords as input
