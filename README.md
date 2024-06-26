# ROS Project
**!!IMPORTANT!!
 in [chatgpt_node.py](https://github.com/Faris-Faiz/ROSProject/blob/main/scripts/chatgpt_node.py "chatgpt_node.py") under the scripts folder, please adjust the OpenAI Key as usual.**

This is the ROS Project for the Autonomous Robots assignment by our group.

Run these codes to test out the entire

    rosrun chatgpt_ros chatgpt_node.py
    rosrun chatgpt_ros tts_node.py

Run the code below to test out the ChatGPT Component

    rostopic pub /chatgpt_input std_msgs/String "Hello, ChatGPT!"
# Steps for running this project

 - type `roscore` in terminal
 - paste `roslaunch usb_cam usb_cam-test.launch` into the terminal to open the camera on the robot. If it doesn't work, try `run usb_cam usb_cam_node _video_device:=/dev/video2`
 - paste `roslaunch robot_vision_openvino yolo_ros.launch > /home/mustar/catkin_ws/src/ROSProject-main/scripts/text_files/yolo_output_test.txt` into terminal
 - paste `rosrun chatgpt_ros chatgpt_node.py` into terminal
 - paste `rosrun chatgpt_ros input_publisher.py` into terminal
 
 Prerequisites:
 
 - Make sure playsound is installed through `pip install playsound`
 - Ensure pip is installed through `sudo apt-get install python-pip`
